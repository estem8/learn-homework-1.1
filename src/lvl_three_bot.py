
import requests

def send_message(chat_id):
    method = 'sendMessage'
    text = f'Текст для отправки обратно'
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    data = {"chat_id": chat_id, "text": text}
    print(data)
    requests.post(url, data=data)