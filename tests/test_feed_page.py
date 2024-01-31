import datafile
import auxiliary_functions
from tests.locators import Locators
from pages.feed_page import FeedPage
import allure


class TestFeedPage:
    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_clicked_popup_opens_success(self, driver):
        feed = FeedPage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        feed.open_page(Locators.url_login_page)
        feed.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        feed.fill_in_a_field(Locators.locator_login_page_input_email, login)
        feed.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        feed.click_element(Locators.locator_login_page_login_button)
        feed.wait_until_element_is_visible(Locators.locator_order_page_order_button)
        feed.click_element(Locators.locator_order_page_order_feed_button)
        feed.wait_until_element_is_visible(Locators.locator_order_page_order_feed_header)
        feed.click_element(Locators.locator_feed_first_order)
        feed.wait_until_element_is_visible(Locators.locator_feed_first_order_popup)

        assert 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5' == driver.find_element(*Locators.locator_feed_popup_section_popup_open).get_attribute('class')

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: заказы пользователя из разд. «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_visible_in_feed_success(self, driver):
        feed = FeedPage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        feed.open_page(Locators.url_login_page)
        feed.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        feed.fill_in_a_field(Locators.locator_login_page_input_email, login)
        feed.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        feed.click_element(Locators.locator_login_page_login_button)
        feed.wait_until_element_is_visible(Locators.locator_order_page_order_button)

        feed.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation,
                                         Locators.locator_order_page_slot_for_upper_bun)
        feed.click_element(Locators.locator_order_page_order_button)
        feed.wait_until_element_is_visible(Locators.locator_successful_order)
        feed.wait_until_element_is_visible(Locators.locator_successful_order_tick)
        feed.wait_3_seconds()
        order_number = driver.find_element(*Locators.locator_order_page_order_number).text
        feed.click_element(Locators.locator_successful_order_cross)
        feed.click_element(Locators.locator_order_page_order_feed_button)
        feed.wait_until_element_is_visible(Locators.locator_feed_orders_ready)

        assert '#0' + order_number == driver.find_element(*Locators.locator_feed_number_of_most_recent_order).text

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: после оформления заказа его номер появляется в разделе В работе')
    def test_users_order_number_visible_in_in_progress_section_success(self, driver):
        feed = FeedPage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        feed.open_page(Locators.url_login_page)
        feed.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        feed.fill_in_a_field(Locators.locator_login_page_input_email, login)
        feed.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        feed.click_element(Locators.locator_login_page_login_button)
        feed.wait_until_element_is_visible(Locators.locator_order_page_order_button)

        feed.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation,
                                         Locators.locator_order_page_slot_for_upper_bun)
        feed.click_element(Locators.locator_order_page_order_button)
        feed.wait_until_element_is_visible(Locators.locator_successful_order)
        feed.wait_until_element_is_visible(Locators.locator_successful_order_tick)
        feed.wait_3_seconds()
        order_number = driver.find_element(*Locators.locator_order_page_order_number).text
        feed.click_element(Locators.locator_successful_order_cross)
        feed.click_element(Locators.locator_order_page_order_feed_button)
        feed.wait_until_element_is_visible(Locators.locator_feed_orders_ready)

        assert '0' + order_number == driver.find_element(*Locators.locator_feed_orders_in_progress_number).text

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_created_all_orders_counter_increases_success(self, driver):
        feed = FeedPage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        feed.open_page(Locators.url_login_page)
        feed.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        feed.fill_in_a_field(Locators.locator_login_page_input_email, login)
        feed.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        feed.click_element(Locators.locator_login_page_login_button)
        feed.wait_until_element_is_visible(Locators.locator_order_page_order_button)

        feed.click_element(Locators.locator_order_page_order_feed_button)
        feed.wait_until_element_is_visible(Locators.locator_feed_orders_ready)
        total_orders_number_before = driver.find_element(*Locators.locator_feed_total_orders_number).text
        feed.click_element(Locators.locator_order_page_constructor_button)
        feed.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation,
                                       Locators.locator_order_page_slot_for_upper_bun)
        feed.click_element(Locators.locator_order_page_order_button)
        feed.wait_until_element_is_clickable(Locators.locator_successful_order_cross)
        feed.click_element(Locators.locator_successful_order_cross)
        feed.click_element(Locators.locator_order_page_order_feed_button)
        feed.wait_until_element_is_visible(Locators.locator_feed_orders_ready)

        total_orders_number_after = driver.find_element(*Locators.locator_feed_total_orders_number).text

        assert total_orders_number_after > total_orders_number_before

        auxiliary_functions.delete_user(token)

    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_created_all_orders_counter_increases_success(self, driver):
        feed = FeedPage(driver)

        user_data = auxiliary_functions.create_user()
        login = user_data.json()['user']['email']
        token = auxiliary_functions.get_user_token(user_data)

        feed.open_page(Locators.url_login_page)
        feed.wait_until_element_is_visible(Locators.locator_login_page_input_email)
        feed.fill_in_a_field(Locators.locator_login_page_input_email, login)
        feed.fill_in_a_field(Locators.locator_login_page_input_password, datafile.user_password)
        feed.click_element(Locators.locator_login_page_login_button)
        feed.wait_until_element_is_visible(Locators.locator_order_page_order_button)

        feed.click_element(Locators.locator_order_page_order_feed_button)
        feed.wait_until_element_is_visible(Locators.locator_feed_orders_ready)
        today_orders_number_before = driver.find_element(*Locators.locator_feed_today_orders_number).text
        feed.click_element(Locators.locator_order_page_constructor_button)
        feed.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation,
                                   Locators.locator_order_page_slot_for_upper_bun)
        feed.click_element(Locators.locator_order_page_order_button)
        feed.wait_until_element_is_clickable(Locators.locator_successful_order_cross)
        feed.click_element(Locators.locator_successful_order_cross)
        feed.click_element(Locators.locator_order_page_order_feed_button)
        feed.wait_until_element_is_visible(Locators.locator_feed_orders_ready)

        today_orders_number_after = driver.find_element(*Locators.locator_feed_today_orders_number).text

        assert today_orders_number_after > today_orders_number_before

        auxiliary_functions.delete_user(token)


