import requests

response = requests.post(
    'http://127.0.0.1:5000/adv',
    json={
        "title": "some title 5",
        # "description": "some description 5",
        # "author": "some author 5"
    }
)

# response = requests.get('http://127.0.0.1:5000/adv/3')

# response = requests.patch(
#     'http://127.0.0.1:5000/adv/4',
#     json={
#         "title": "newtitle",
#         "description": "newdescription",
#         "author": "newauthor"
#     }
# )

# response = requests.delete('http://127.0.0.1:5000/adv/6')


print(response.status_code)
print(response.headers)
print(response.text)