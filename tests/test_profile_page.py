import datafile
from pages.profile_page import ProfilePage
import auxiliary_functions
from tests.locators import Locators
import allure


class TestProfilePage:

    @allure.title('Проверка: можно перейти в профиль по клику на кнопку Личный кабинет')
    def test_redirect_to_profile_page_via_header_button_success(self, driver):
        profile = ProfilePage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        profile.open_page(Locators.url_login_page)
        profile.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        profile.fill_in_a_field(Locators.locator_login_page_input_email, login)
        profile.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        profile.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        profile.click_element(Locators.locator_login_page_login_button)
        profile.wait_until_element_is_clickable(Locators.locator_order_page_profile_button)
        profile.click_element(Locators.locator_order_page_profile_button)
        profile.wait_until_element_is_clickable(Locators.locator_profile_page_order_history_button)

        assert profile.check_if_element_is_on_page(Locators.locator_profile_page_order_history_button) == True

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: можно перейти из профиля в раздел История заказов')
    def test_redirect_from_profile_to_feed_success(self, driver):
        profile = ProfilePage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        profile.open_page(Locators.url_login_page)
        profile.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        profile.fill_in_a_field(Locators.locator_login_page_input_email, login)
        profile.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        profile.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        profile.click_element(Locators.locator_login_page_login_button)
        profile.wait_until_element_is_clickable(Locators.locator_order_page_profile_button)
        profile.click_element(Locators.locator_order_page_profile_button)
        profile.wait_until_element_is_clickable(Locators.locator_profile_page_order_history_button)
        profile.click_element(Locators.locator_profile_page_order_history_button)

        assert profile.show_current_url() == Locators.url_order_page

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: можно выйти из аккаунта по кнопке Выход')
    def test_logout_from_profile_page_success(self, driver):
        profile = ProfilePage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        profile.open_page(Locators.url_login_page)
        profile.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        profile.fill_in_a_field(Locators.locator_login_page_input_email, login)
        profile.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        profile.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        profile.click_element(Locators.locator_login_page_login_button)
        profile.wait_until_element_is_clickable(Locators.locator_order_page_profile_button)
        profile.click_element(Locators.locator_order_page_profile_button)
        profile.wait_until_element_is_clickable(Locators.locator_profile_page_order_history_button)
        profile.click_element(Locators.locator_profile_page_logout_button)
        profile.wait_until_element_is_clickable(Locators.locator_login_page_login_button)

        assert profile.show_current_url() == Locators.url_login_page

        auxiliary_functions.delete_user(token)
