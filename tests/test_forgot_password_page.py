from pages.forgot_password_page import ForgotPasswordPage
import auxiliary_functions
from tests.locators import Locators
import allure


class TestForgotPasswordPage:

    @allure.title('Проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_redirect_to_forgot_password_page_via_forgot_password_button_success(self, driver):
        password_page = ForgotPasswordPage(driver)
        user_data = auxiliary_functions.create_user()
        token = auxiliary_functions.get_user_token(user_data)

        password_page.open_page(Locators.url_login_page)
        password_page.wait_until_element_is_clickable(Locators.locator_login_page_forgot_password_link)
        password_page.click_element(Locators.locator_login_page_forgot_password_link)

        assert password_page.show_current_url() == Locators.url_forgot_password_page

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: ввод почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_press_forgot_password_button_success(self, driver):
        password_page = ForgotPasswordPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()["user"]["email"]
        token = auxiliary_functions.get_user_token(user_data)

        password_page.open_page(Locators.url_login_page)
        password_page.wait_until_element_is_clickable(Locators.locator_login_page_forgot_password_link)
        password_page.click_element(Locators.locator_login_page_forgot_password_link)
        password_page.wait_until_element_is_clickable(Locators.locator_forgot_password_page_revoke_button)
        password_page.fill_in_a_field(Locators.locator_forgot_password_page_email_field, login)
        password_page.wait_until_element_is_clickable(Locators.locator_forgot_password_page_revoke_button)
        password_page.click_element(Locators.locator_forgot_password_page_revoke_button)
        password_page.wait_until_element_is_visible(Locators.locator_forgot_password_page_password_field)

        assert password_page.check_if_element_is_on_page(Locators.locator_forgot_password_page_password_field) == True

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_eye_in_password_field_makes_it_active_success(self, driver):
        password_page = ForgotPasswordPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        password_page.open_page(Locators.url_login_page)
        password_page.wait_until_element_is_clickable(Locators.locator_login_page_forgot_password_link)
        password_page.click_element(Locators.locator_login_page_forgot_password_link)
        password_page.wait_until_element_is_clickable(Locators.locator_forgot_password_page_revoke_button)
        password_page.fill_in_a_field(Locators.locator_forgot_password_page_email_field, login)
        password_page.wait_until_element_is_clickable(Locators.locator_forgot_password_page_revoke_button)
        password_page.click_element(Locators.locator_forgot_password_page_revoke_button)
        password_page.wait_until_element_is_visible(Locators.locator_forgot_password_page_password_field)
        password_page.fill_in_a_field(Locators.locator_forgot_password_page_password_field, auxiliary_functions.generate_random_password())
        password_page.click_element(Locators.locator_forgot_password_page_eye_icon)

        assert 'input_status_active' in driver.find_element(*Locators.locator_label_password_div_field).get_attribute("class")

        auxiliary_functions.delete_user(token)
