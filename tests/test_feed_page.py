from pages.feed_page import FeedPage
import allure


class TestFeedPage:
    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_clicked_popup_opens_success(self, driver, setup_user):
        feed = FeedPage(driver)

        login, password = setup_user

        feed.open_login_page()
        feed.wait_until_email_field_is_visible()
        feed.fill_in_login(login)
        feed.fill_in_password(password)
        feed.click_login_button()
        feed.wait_until_order_button_is_visible()
        feed.open_feed()
        feed.wait_until_feed_header_is_visible()
        feed.open_most_recent_order_popup()
        feed.wait_for_most_recent_order_popup_to_be_visible()

        assert 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5' == feed.get_class_of_the_most_recent_popup_locator()

    @allure.title('Проверка: заказы пользователя из разд. «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_visible_in_feed_success(self, driver, setup_user):
        feed = FeedPage(driver)

        login, password = setup_user

        feed.open_login_page()
        feed.wait_until_email_field_is_visible()
        feed.fill_in_login(login)
        feed.fill_in_password(password)
        feed.click_login_button()
        feed.wait_until_order_button_is_visible()

        feed.drag_and_drop_fluorescent_bun()
        feed.click_order_button()
        feed.wait_until_successful_order_text_is_visible()
        feed.wait_for_order_number()
        order_number = feed.get_order_number_text()
        feed.close_order_popup()
        feed.open_feed()
        feed.wait_for_list_of_ready_orders()

        assert '#0' + order_number == feed.get_number_of_the_most_recent_order()


    @allure.title('Проверка: после оформления заказа его номер появляется в разделе В работе')
    def test_users_order_number_visible_in_in_progress_section_success(self, driver, setup_user):
        feed = FeedPage(driver)

        login, password = setup_user

        feed.open_login_page()
        feed.wait_until_email_field_is_visible()
        feed.fill_in_login(login)
        feed.fill_in_password(password)
        feed.click_login_button()
        feed.wait_until_order_button_is_visible()
        feed.drag_and_drop_fluorescent_bun()
        feed.click_order_button()
        feed.wait_until_successful_order_text_is_visible()
        feed.wait_for_order_number()
        order_number = feed.get_order_number_text()
        feed.close_order_popup()
        feed.open_feed()
        feed.wait_for_list_of_ready_orders()

        assert '0' + order_number == feed.get_in_progress_order_number()


    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_created_all_orders_counter_increases_success(self, driver, setup_user):
        feed = FeedPage(driver)

        login, password = setup_user

        feed.open_login_page()
        feed.wait_until_email_field_is_visible()
        feed.fill_in_login(login)
        feed.fill_in_password(password)
        feed.click_login_button()
        feed.wait_until_order_button_is_visible()

        feed.open_feed()
        feed.wait_for_list_of_ready_orders()
        total_orders_number_before = feed.get_total_orders_number()
        feed.click_constructor_button()
        feed.drag_and_drop_fluorescent_bun()
        feed.click_order_button()
        feed.wait_until_popup_cross_is_clickable()
        feed.close_order_popup()
        feed.open_feed()
        feed.wait_for_list_of_ready_orders()

        total_orders_number_after = feed.get_total_orders_number()

        assert total_orders_number_after > total_orders_number_before


    @allure.title('Проверка: при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_created_all_orders_counter_increases_success(self, driver, setup_user):
        feed = FeedPage(driver)

        login, password = setup_user

        feed.open_login_page()
        feed.wait_until_email_field_is_visible()
        feed.fill_in_login(login)
        feed.fill_in_password(password)
        feed.click_login_button()
        feed.wait_until_order_button_is_visible()

        feed.open_feed()
        feed.wait_for_list_of_ready_orders()
        today_orders_number_before = feed.get_today_orders_number()
        feed.click_constructor_button()
        feed.drag_and_drop_fluorescent_bun()
        feed.click_order_button()
        feed.wait_until_popup_cross_is_clickable()
        feed.close_order_popup()
        feed.open_feed()
        feed.wait_for_list_of_ready_orders()

        today_orders_number_after = feed.get_today_orders_number()

        assert today_orders_number_after > today_orders_number_before




