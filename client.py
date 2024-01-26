import requests

# response = requests.post(
#     'http://127.0.0.1:5000/adv',
#     json={
#         "title": "some title 1",
#         "description": "some description 1",
#         "author": "some author 1"
#     }
# )

response = requests.get('http://127.0.0.1:5000/adv/1')

print(response.status_code)
print(response.text)