import environ
import datetime
import requests

def send_message(message):
    url = "https://notify-api.line.me/api/notify"
    token = environ.TIMETABLE_TOKEN
    headers = {"Authorization" : "Bearer "+ token}
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)


'''

if __name__ == '__main__':
    send_message()

'''