import requests

response = requests.post(
    'http://127.0.0.1:5000/adv',
    json={
        "title": "some title 1",
        "description": "some description 1",
        "author": "some author 1"
    }
)

response = requests.get('http://127.0.0.1:5000/adv/1')

# response = requests.patch(
#     'http://127.0.0.1:5000/adv/2',
#     json={
#         "title": "newtitle",
#         "description": "newdescription",
#         "author": "newauthor"
#     }
# )

# response = requests.delete('http://127.0.0.1:5000/adv/1')


print(response.status_code)
print(response.text)