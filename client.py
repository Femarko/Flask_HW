import requests

# response = requests.post(
#     'http://127.0.0.1:5000/adv',
#     json={
#         "title": "some title 7",
#         "description": "some description 7",
#         "author": "some author 7"
#     }
# )

response = requests.get('http://127.0.0.1:5000/adv/10')

print(response.status_code)
print(response.text)