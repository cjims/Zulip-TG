import zulip
import requests
import time

client = zulip.Client(config_file="zuliprc")  # TG bot 的設定

# TG bot的設定
TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = ''

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    })

# 建立事件佇列
print("📡 註冊事件佇列中...")
queue = client.register(event_types=["message"])
print("🔍 register() response:", queue)

queue_id = queue["queue_id"]
last_id = queue["last_event_id"]

print("✅ 成功註冊事件佇列，開始監聽新訊息...")

# 持續監聽新訊息
try:
    while True:
        res = client.get_events(queue_id=queue_id, last_event_id=last_id, dont_block=False)
        for event in res.get("events", []):
            last_id = event["id"]
            if event["type"] == "message":
                msg = event["message"]
                content = msg["content"]
                sender = msg["sender_full_name"]
                stream = msg["display_recipient"] if isinstance(msg["display_recipient"], str) else "Private"
                topic = msg.get("subject", "")
                text = f"[{stream} / {topic}] {sender}: {content}"
                print("➡️ 發送到 Telegram:", text)
                send_to_telegram(text)
except KeyboardInterrupt:
    print("🛑 手動中止")
