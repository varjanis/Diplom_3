from pages.forgot_password_page import ForgotPasswordPage
import datafile
import allure


class TestForgotPasswordPage:

    @allure.title('Проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_redirect_to_forgot_password_page_via_forgot_password_button_success(self, driver):
        password_page = ForgotPasswordPage(driver)

        password_page.open_login_page()
        password_page.wait_until_forgot_password_link_is_clickable()
        password_page.click_forgot_password_link()

        assert password_page.show_current_url() == datafile.url_forgot_password_page


    @allure.title('Проверка: ввод почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_press_forgot_password_button_success(self, driver, setup_user):
        password_page = ForgotPasswordPage(driver)

        login, password = setup_user

        password_page.open_login_page()
        password_page.wait_until_forgot_password_link_is_clickable()
        password_page.click_forgot_password_link()
        password_page.wait_until_revoke_button_is_clickable()
        password_page.fill_in_login(login)
        password_page.wait_until_revoke_button_is_clickable()
        password_page.click_password_revoke_button()
        password_page.wait_until_password_field_is_visible()

        assert password_page.check_if_password_field_is_on_page()


    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_eye_in_password_field_makes_it_active_success(self, driver, setup_user):
        password_page = ForgotPasswordPage(driver)

        login, password = setup_user

        password_page.open_login_page()
        password_page.wait_until_forgot_password_link_is_clickable()
        password_page.click_forgot_password_link()
        password_page.wait_until_revoke_button_is_clickable()
        password_page.fill_in_login(login)
        password_page.wait_until_revoke_button_is_clickable()
        password_page.click_password_revoke_button()
        password_page.wait_until_password_field_is_visible()
        password_page.fill_in_new_password()
        password_page.click_eye_icon()

        assert 'input_status_active' in password_page.get_class_of_a_password_div_locator()


