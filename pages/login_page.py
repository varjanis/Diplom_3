from pages.base_page import BasePage
from tests.locators import Locators
import datafile
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Открыть страницу логина')
    def open_login_page(self):
        return self.open_page(datafile.url_login_page)

    @allure.step('Дождаться, когда появится поле логина')
    def wait_until_email_field_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_login_page_input_email)

    @allure.step('Заполнить поле логин')
    def fill_in_login(self, login):
        return self.fill_in_a_field(Locators.locator_login_page_input_email, login)

    @allure.step('Заполнить поле пароль')
    def fill_in_password(self, password):
        return self.fill_in_a_field(Locators.locator_login_page_input_password, password)

    @allure.step('Дождаться, когда кнопка Войти станет кликабельна')
    def wait_until_login_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_login_page_login_button)

    @allure.step('Кликнуть на кнопку Войти')
    def click_login_button(self):
        return self.click_element(Locators.locator_login_page_login_button)
