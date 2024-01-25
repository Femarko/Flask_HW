import requests

# response = requests.post(
#     'http://127.0.0.1:5000/adv',
#     json={
#         "title": "some title 2",
#         "description": "some description 2",
#         "author": "some author 2"
#     }
# )

response = requests.get('http://127.0.0.1:5000/adv/1')

print(response.status_code)
print(response.text)