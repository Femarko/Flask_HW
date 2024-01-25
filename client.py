import requests

response = requests.post(
    'http://127.0.0.1:5000/adv',
    json={
        "title": "some title 3",
        "description": "some description 3",
        "author": "some author 3"
    }
)
print(response.status_code)
print(response.text)