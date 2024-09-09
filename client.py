import requests

response = requests.post(
    'http://127.0.0.1:5000/adv',
    json={
        "title": "one",
        "description": "one",
        "author": "one"
    }
)

# response = requests.get('http://127.0.0.1:5000/adv/1')

# response = requests.patch(
#     'http://127.0.0.1:5000/adv/1',
#     json={
#         "title": "totally new",
#         # "description": "some moddescription",
#         # "author": "newauthor"
#     }
# )

# response = requests.delete('http://127.0.0.1:5000/adv/1')


print(response.status_code)
print(response.headers)
print(response.text)