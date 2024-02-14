import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FS
import auxiliary_functions
import allure


DRIVER_PATH_CHROME = '../chromedriver'
DRIVER_PATH_FIREFOX = '../geckodriver'


@allure.step('Подключить драйвер')
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        service = FS(executable_path=DRIVER_PATH_FIREFOX)
        driver = webdriver.Firefox(service=service)
    elif request.param == 'chrome':
        service = Service(executable_path=DRIVER_PATH_CHROME)
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@allure.step('Задать тестового пользователя')
@pytest.fixture
def setup_user():

    user_data, password = auxiliary_functions.create_user()
    login = user_data.json()['user']['email']
    token = auxiliary_functions.get_user_token(user_data)

    yield login, password

    auxiliary_functions.delete_user(token)
