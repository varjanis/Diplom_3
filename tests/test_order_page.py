from pages.order_page import OrderPage
from pages.login_page import LoginPage
import allure


class TestOrderPage:

    @allure.title('Проверка: переход по кнопке «Конструктор»')
    def test_redirect_via_constructor_button_success(self, driver, setup_user):
        order_page = OrderPage(driver)
        login_page = LoginPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()

        order_page.wait_until_profile_button_is_clickable()
        order_page.click_profile_button()
        order_page.wait_until_constructor_button_is_clickable()
        order_page.click_constructor_button()
        order_page.wait_until_order_button_is_clickable()

        assert order_page.check_if_order_button_is_on_page()

    @allure.title('Проверка: переход по кнопке «Лента заказов»')
    def test_redirect_via_order_feed_button_success(self, driver, setup_user):
        order_page = OrderPage(driver)
        login_page = LoginPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_profile_button_is_clickable()
        order_page.click_profile_button()
        order_page.wait_until_feed_button_is_clickable()
        order_page.click_feed_button()
        order_page.wait_until_feed_header_is_visible()

        assert order_page.check_if_feed_header_is_on_page()

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_popup_appears_success(self, driver, setup_user):
        order_page = OrderPage(driver)
        login_page = LoginPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_order_button_is_clickable()
        order_page.click_fluorescent_bun()

        assert order_page.check_if_fluorescent_bun_popup_is_on_page()

    @allure.title('Проверка: всплывающее окно закрывается кликом по крестику')
    def test_ingredient_popup_closes_success(self, driver, setup_user):
        order_page = OrderPage(driver)
        login_page = LoginPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_fluorescent_bun_is_clickable()
        order_page.click_fluorescent_bun()
        order_page.wait_until_fluorescent_bun_popup_cross_is_clickable()
        order_page.click_fluorescent_bun_popup_cross()
        order_page.wait_until_fluorescent_bun_is_clickable()

        assert 'Modal_modal__P3_V5' == order_page.get_class_of_a_fluorescent_bun_popup_locator()

    @allure.title('Проверка: при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_added_counter_increases_success(self, driver, setup_user):
        order_page = OrderPage(driver)
        login_page = LoginPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_order_button_is_clickable()
        order_page.drag_and_drop_fluorescent_bun()

        assert order_page.get_text_of_a_fluorescent_bun_counter() == '2'

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    def test_logged_in_user_makes_order_success(self, driver, setup_user):
        order_page = OrderPage(driver)
        login_page = LoginPage(driver)

        login, password = setup_user

        login_page.open_login_page()
        login_page.wait_until_email_field_is_visible()
        login_page.fill_in_login(login)
        login_page.fill_in_password(password)
        login_page.wait_until_login_button_is_clickable()
        login_page.click_login_button()
        order_page.wait_until_order_button_is_clickable()
        order_page.drag_and_drop_fluorescent_bun()
        order_page.click_order_button()
        order_page.wait_until_successful_order_text_is_visible()

        assert order_page.check_if_successful_order_is_on_page()


