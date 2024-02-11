import datafile
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
import allure


class TestProfilePage:

    @allure.title('Проверка: можно перейти в профиль по клику на кнопку Личный кабинет')
    def test_redirect_to_profile_page_via_header_button_success(self, driver, setup_user):
        profile = ProfilePage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_profile_button_is_clickable()
        order_page.click_profile_button()
        profile.wait_until_order_history_button_is_clickable()

        assert profile.check_if_order_history_button_is_on_page()


    @allure.title('Проверка: можно перейти из профиля в раздел История заказов')
    def test_redirect_from_profile_to_feed_success(self, driver, setup_user):
        profile = ProfilePage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_profile_button_is_clickable()
        order_page.click_profile_button()
        profile.wait_until_order_history_button_is_clickable()
        profile.click_order_history_button()

        assert profile.show_current_url() == datafile.url_order_page


    @allure.title('Проверка: можно выйти из аккаунта по кнопке Выход')
    def test_logout_from_profile_page_success(self, driver, setup_user):
        profile = ProfilePage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_profile_button_is_clickable()
        order_page.click_profile_button()
        profile.wait_until_order_history_button_is_clickable()
        profile.click_logout_button()
        login_page.wait_until_login_button_is_clickable()

        assert profile.show_current_url() == datafile.url_login_page


