# from typing import Protocol

import requests


# response = requests.post(
#     'http://127.0.0.1:5000/adv',
#     json={
#         "title": "twenty five",
#         "description": "twenty five",
#         "author": "twenty five"
#     }
# )

# response = requests.get('http://127.0.0.1:5000/adv/24')

response = requests.patch(
    'http://127.0.0.1:5000/adv/12',
    json={
        "title": "fifteen",
        "description": "fifteen",
        "author": "fifteen"
    }
)

# response = requests.delete('http://127.0.0.1:5000/adv/1')


print(response.status_code)
print(response.headers)
print(response.text)

# class Coffe:
#     def smell(self):
#         return "self"
#
#
#
# class Tea:
#     def smell(self):
#         return "ssss"
#
#
# class Smth:
#     def smth(self):
#         return f"smth"
#
#
# class Pro(Protocol):
#     def smell(self):
#         raise NotImplementedError
#
#
# def tdt(some_inst: Pro):
#     return "cdfgfdg"
#
# smth = Smth()
# tea = Tea()
# coffe = Coffe()
#
# tdt(tea)
# tdt(Coffe())
# tdt(Smth())


# from typing import Protocol
# class Human:
#     def say(self) -> str:
#         return 'Hi!'
#
#
# class Duck:
#     def say(self) -> str:
#         return 'Quack'
#
#
# class CanSay(Protocol):
#     def say(self) -> str: ...
#
#
# def say_and_print(instance: CanSay) -> None:
#     print(instance.say())
#
#
# human = Human()
# duck = Duck()
# say_and_print(human)  # ok
# say_and_print(duck)  # ok
# say_and_print(1)  # not ok :(

# class Duck:
#     def can_say(self):
#         pass
#
# class Human:
#     def can_say(self):
#         pass
#
#
# class CannotSay:
#     pass
#
#
# class CnSay(Protocol):
#     def can_say(self):
#         pass
#
# def say_smth(inst: CnSay):
#     pass
#
#
# duck = Duck()
# human = Human()
# cannot_say = CannotSay()
#
# say_smth(duck)
# say_smth(human)
# say_smth(cannot_say)
#
