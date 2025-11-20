# Zulip-TG

Zulip接收資訊後，即時在Telegram顯示

## **zuliprc**

依照zulip所需API接口，進行資訊填寫

## run

因為會放到windows底下的service背景執行，所以需下載nssm服務管理員(Non-Sucking Service Manager)

## 環境
### 安裝
```bash
pip install -r requirements.txt
```
### 設定
```bash
nssm set Zulip-TG_Service Application "C:\Users\AppData\Local\Programs\Python\Python312\python.exe"
nssm set Zulip-TG_Service AppParameters "C:\app\zutest.py"
nssm set Zulip-TG_Service AppDirectory "C:\app"
```

### 安裝、啟動
```bash
nssm install Zulip-TG_Service
nssm start Zulip-TG_Service

```


