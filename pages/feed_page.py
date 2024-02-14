from pages.base_page import BasePage
from tests.locators import Locators
import allure


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Дождаться, когда будет виден номер заказа')
    def wait_for_order_number(self):
        return self.wait_for_text_not_to_be_present(Locators.locator_order_page_order_number, '9999')

    @allure.step('Перетащить в заказ флуоресцентную булочку')
    def drag_and_drop_fluorescent_bun(self):
        return self.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation,
                                         Locators.locator_order_page_slot_for_upper_bun)

    @allure.step('Кликнуть на кнопку Оформить заказ')
    def click_order_button(self):
        return self.click_element(Locators.locator_order_page_order_button)

    @allure.step('Дождаться, когда появится текст о том, что заказ оформлен')
    def wait_until_successful_order_text_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_successful_order)

    @allure.step('Получить номер заказа')
    def get_order_number_text(self):
        return self.get_text_of_a_locator(Locators.locator_order_page_order_number)

    @allure.step('Дождаться, когда на крестик поп-апа заказа можно будет кликнуть')
    def wait_until_popup_cross_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_successful_order_cross)

    @allure.step('Закрыть поп-ап заказа')
    def close_order_popup(self):
        return self.click_element(Locators.locator_successful_order_cross)

    @allure.step('Открыть ленту заказов')
    def open_feed(self):
        return self.click_element(Locators.locator_order_page_order_feed_button)

    @allure.step('Дождаться, когда будет видно заголовок ленты заказов')
    def wait_until_feed_header_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_order_page_order_feed_header)

    @allure.step('Открыть самый последний заказ')
    def open_most_recent_order_popup(self):
        return self.click_element(Locators.locator_feed_first_order)

    @allure.step('Получить класс локатора самого последнего заказа')
    def get_class_of_the_most_recent_popup_locator(self):
        return self.get_class_of_a_locator(Locators.locator_feed_popup_section_popup_open)

    @allure.step('Дождаться, когда будет видно поп-ап самого последнего заказа')
    def wait_for_most_recent_order_popup_to_be_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_feed_first_order_popup)

    @allure.step('Дождаться, когда будет видно список готовых заказов')
    def wait_for_list_of_ready_orders(self):
        return self.wait_until_element_is_visible(Locators.locator_feed_orders_ready)

    @allure.step('Получить номер заказа "в работе"')
    def get_in_progress_order_number(self):
        return self.get_text_of_a_locator(Locators.locator_feed_orders_in_progress_number)

    @allure.step('Получить номер самого последнего заказа')
    def get_number_of_the_most_recent_order(self):
        return self.get_text_of_a_locator(Locators.locator_feed_number_of_most_recent_order)

    @allure.step('Получить общее количество заказов')
    def get_total_orders_number(self):
        return self.get_text_of_a_locator(Locators.locator_feed_total_orders_number)

    @allure.step('Получить количество заказов за сегодня')
    def get_today_orders_number(self):
        return self.get_text_of_a_locator(Locators.locator_feed_today_orders_number)


