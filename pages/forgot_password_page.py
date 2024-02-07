from pages.base_page import BasePage
from tests.locators import Locators
import auxiliary_functions
import allure


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Дождаться, когда будет кликабельна кнопка Восстановить пароль')
    def wait_until_forgot_password_link_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_login_page_forgot_password_link)

    @allure.step('Кликнуть на кнопку Восстановить пароль')
    def click_forgot_password_link(self):
        return self.click_element(Locators.locator_login_page_forgot_password_link)

    @allure.step('Дождаться, когда будет кликабельна кнопка Восстановить')
    def wait_until_revoke_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_forgot_password_page_revoke_button)

    @allure.step('Заполнить логин')
    def fill_in_login(self, login):
        return self.fill_in_a_field(Locators.locator_forgot_password_page_email_field, login)

    @allure.step('Кликнуть на кнопку Восстановить')
    def click_password_revoke_button(self):
        return self.click_element(Locators.locator_forgot_password_page_revoke_button)

    @allure.step('Дождаться, когда будет видно поле пароль')
    def wait_until_password_field_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_forgot_password_page_password_field)

    @allure.step('Убедиться, что поле пароль есть на странице')
    def check_if_password_field_is_on_page(self):
        return self.check_if_element_is_on_page(Locators.locator_forgot_password_page_password_field)

    @allure.step('Заполнить поле пароль')
    def fill_in_new_password(self):
        return self.fill_in_a_field(Locators.locator_forgot_password_page_password_field, auxiliary_functions.generate_random_password())

    @allure.step('Кликнуть на иконку "показать пароль"')
    def click_eye_icon(self):
        return self.click_element(Locators.locator_forgot_password_page_eye_icon)

    @allure.step('Получить класс элемента div локатора поля пароля')
    def get_class_of_a_password_div_locator(self):
        return self.get_class_of_a_locator(Locators.locator_label_password_div_field)