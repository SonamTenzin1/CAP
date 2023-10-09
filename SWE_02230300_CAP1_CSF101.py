import requests
from urllib.parse import quote
import time

#making the loop infinite
while True:

    def send_message(message):
        token = '6372306748:AAGJMdxyunQ7YnEgXQvblwXH9fytoGOC2O4'
        chat_id = '1677618396'
        message = quote(message)
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())

    send_message('remember to drink water')
    time.sleep(10)




