import requests

# response = requests.post(
#     'http://127.0.0.1:5000/adv',
#     json={
#         "title": "some title 9",
#         "description": "some description 9",
#         "author": "some author 9"
#     }
# )

# response = requests.get('http://127.0.0.1:5000/adv/3')

# response = requests.patch(
#     'http://127.0.0.1:5000/adv/5',
#     json={
#         "title": "new title 5",
#         "description": "new description 5",
#         "author": "new author 5"
#     }
# )

response = requests.delete('http://127.0.0.1:5000/adv/7')


print(response.status_code)
print(response.text)