import requests
import random
import string
import datafile
import allure

@allure.step('Сгенерировать случайный пароль')
def generate_random_password():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


@allure.step('Сгенерировать случайную почту')
def generate_random_email():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(7))
    return f'{random_string}@mail.ru'


@allure.step('Сгенерировать случайное имя')
def generate_random_name(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Создать тестового пользователя')
def create_user():
    email = generate_random_email()
    name = generate_random_name()
    password = generate_random_password()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(datafile.register_endpoint, data=payload)

    return response, password


@allure.step('Получить токен тестового пользователя')
def get_user_token(response):

    token = response.json()["accessToken"]
    return token


@allure.step('Удалить тестового пользователя')
def delete_user(token):

    response = requests.delete(datafile.user_endpoint, headers={'Authorization': token})
    print('Тестовый пользователь успешно удалён')
    return response




