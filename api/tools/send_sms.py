import requests


def send_sms(phone, code):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDg3NTg4NTYsImlhdCI6MTcwNjE2Njg1Niwicm9sZSI6InVzZXIiLCJzaWduIjoiNTQzOWFkYzQyMzVjYjNjZDIwMzNlZmIwOTFiYzg2NzI4NDIyNzA5NDcxNGM0NmRmOTc3MTNiOTM4ZjVkYmNjYiIsInN1YiI6IjEwNTMifQ.ksbZiw05Q9W8DMKPyW1hTimmkLDmVP22JSXQaMuYW7c"}
    data = {
        'mobile_phone': phone,
        'message': code,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }

    response = requests.post(url=url, data=data, headers=headers)
    return response
