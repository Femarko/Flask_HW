import requests

response = requests.post(
    'http://127.0.0.1:5000/adv',
    json={
        "title": "some title",
        "description": "some description",
        "author": "some author"
    }
)
print(response.status_code)
print(response.text)