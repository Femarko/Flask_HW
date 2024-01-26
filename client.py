import requests

# response = requests.post(
#     'http://127.0.0.1:5000/adv',
#     json={
#         "title": "some title 5",
#         "description": "some description 5",
#         "author": "some author 5"
#     }
# )

response = requests.get('http://127.0.0.1:5000/adv/5')

print(response.status_code)
print(response.text)