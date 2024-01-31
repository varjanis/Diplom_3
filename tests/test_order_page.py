import datafile
import auxiliary_functions
from tests.locators import Locators
from pages.order_page import OrderPage
import allure


class TestOrderPage:

    @allure.title('Проверка: переход по кнопке «Конструктор»')
    def test_redirect_via_constructor_button_success(self, driver):
        order_page = OrderPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        order_page.open_page(Locators.url_login_page)
        order_page.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        order_page.fill_in_a_field(Locators.locator_login_page_input_email, login)
        order_page.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        order_page.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        order_page.click_element(Locators.locator_login_page_login_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_profile_button)
        order_page.click_element(Locators.locator_order_page_profile_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_constructor_button)
        order_page.click_element(Locators.locator_order_page_constructor_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_order_button)

        assert order_page.check_if_element_is_on_page(Locators.locator_order_page_order_button)

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: переход по кнопке «Лента заказов»')
    def test_redirect_via_order_feed_button_success(self, driver):
        order_page = OrderPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        order_page.open_page(Locators.url_login_page)
        order_page.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        order_page.fill_in_a_field(Locators.locator_login_page_input_email, login)
        order_page.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        order_page.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        order_page.click_element(Locators.locator_login_page_login_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_profile_button)
        order_page.click_element(Locators.locator_order_page_profile_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_order_feed_button)
        order_page.click_element(Locators.locator_order_page_order_feed_button)
        order_page.wait_until_element_is_visible(Locators.locator_order_page_order_feed_header)

        assert order_page.check_if_element_is_on_page(Locators.locator_order_page_order_feed_header)

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_popup_appears_success(self, driver):
        order_page = OrderPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        order_page.open_page(Locators.url_login_page)
        order_page.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        order_page.fill_in_a_field(Locators.locator_login_page_input_email, login)
        order_page.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        order_page.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        order_page.click_element(Locators.locator_login_page_login_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_order_button)
        order_page.click_element(Locators.locator_order_page_ingredient_fluorescent_bun)

        assert order_page.check_if_element_is_on_page(Locators.locator_order_page_fluorescent_bun_popup) == True

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: всплывающее окно закрывается кликом по крестику')
    def test_ingredient_popup_closes_success(self, driver):
        order_page = OrderPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        order_page.open_page(Locators.url_login_page)
        order_page.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        order_page.fill_in_a_field(Locators.locator_login_page_input_email, login)
        order_page.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        order_page.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        order_page.click_element(Locators.locator_login_page_login_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_ingredient_fluorescent_bun)
        order_page.click_element(Locators.locator_order_page_ingredient_fluorescent_bun)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_fluorescent_bun_popup_cross)
        order_page.click_element(Locators.locator_order_page_fluorescent_bun_popup_cross)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_ingredient_fluorescent_bun)

        assert 'Modal_modal__P3_V5' == driver.find_element(*Locators.locator_order_page_fluorescent_bun_popup_modal_section).get_attribute('class')

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_added_counter_increases_success(self, driver):
        order_page = OrderPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        order_page.open_page(Locators.url_login_page)
        order_page.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        order_page.fill_in_a_field(Locators.locator_login_page_input_email, login)
        order_page.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        order_page.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        order_page.click_element(Locators.locator_login_page_login_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_order_button)
        order_page.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation, Locators.locator_order_page_slot_for_upper_bun)

        assert driver.find_element(*Locators.locator_fluorescent_bun_counter).text == '2'

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    def test_logged_in_user_makes_order_success(self, driver):
        order_page = OrderPage(driver)
        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        order_page.open_page(Locators.url_login_page)
        order_page.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        order_page.fill_in_a_field(Locators.locator_login_page_input_email, login)
        order_page.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        order_page.wait_until_element_is_clickable(Locators.locator_login_page_login_button)
        order_page.click_element(Locators.locator_login_page_login_button)
        order_page.wait_until_element_is_clickable(Locators.locator_order_page_order_button)
        order_page.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation, Locators.locator_order_page_slot_for_upper_bun)
        order_page.click_element(Locators.locator_order_page_order_button)
        order_page.wait_until_element_is_visible(Locators.locator_successful_order)

        assert order_page.check_if_element_is_on_page(Locators.locator_successful_order) == True

        auxiliary_functions.delete_user(token)


