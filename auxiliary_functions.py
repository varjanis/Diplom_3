import requests
import random
import string
import datafile


def generate_random_password():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


def generate_random_email():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(7))
    return f'{random_string}@mail.ru'


def generate_random_name(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_user():
    email = generate_random_email()
    name = generate_random_name()
    password = datafile.user_password

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(datafile.register_endpoint, data=payload)

    return response


def get_user_token(response):

    token = response.json()["accessToken"]
    return token


def delete_user(token):

    response = requests.delete(datafile.user_endpoint, headers={'Authorization': token})
    print('Тестовый пользователь успешно удалён')
    return response




