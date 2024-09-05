import requests

response = requests.post(
    'http://127.0.0.1:5000/adv',
    json={
        "title": "smth new",
        "description": "smth new",
        "author": "smth new"
    }
)

# response = requests.get('http://127.0.0.1:5000/adv/17')

# response = requests.patch(
#     'http://127.0.0.1:5000/adv/16',
#     json={
#         "title": "totally new",
#         # "description": "some moddescription",
#         # "author": "newauthor"
#     }
# )

# response = requests.delete('http://127.0.0.1:5000/adv/14')


print(response.status_code)
print(response.headers)
print(response.text)