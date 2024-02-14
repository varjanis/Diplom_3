from pages.base_page import BasePage
from tests.locators import Locators
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Кликнуть на кнопку Конструктор')
    def click_constructor_button(self):
        return self.click_element(Locators.locator_order_page_constructor_button)

    @allure.step('Кликнуть на кнопку Личный кабинет')
    def click_profile_button(self):
        return self.click_element(Locators.locator_order_page_profile_button)

    @allure.step('Дождаться, когда будет кликабельна кнопка Оформить заказ')
    def wait_until_order_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_order_button)

    @allure.step('Дождаться, когда будет кликабельна кнопка Конструктор')
    def wait_until_constructor_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_constructor_button)

    @allure.step('Дождаться, когда кнопка Личный кабинет будет кликабельна')
    def wait_until_profile_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_profile_button)

    @allure.step('Дождаться, когда будет видно кнопку Оформить заказ')
    def wait_until_order_button_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_order_page_order_button)

    @allure.step('Убедиться, что кнопка Оформить заказ есть на странице')
    def check_if_order_button_is_on_page(self):
        return self.check_if_element_is_on_page(Locators.locator_order_page_order_button)

    @allure.step('Дождаться, чтобы кнопка Лента заказов стала кликабельной')
    def wait_until_feed_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_order_feed_button)

    @allure.step('Кликнуть на кнопку Лента заказов')
    def click_feed_button(self):
        return self.click_element(Locators.locator_order_page_order_feed_button)

    @allure.step('Дождаться, чтобы стал виден заголовок Ленты заказов')
    def wait_until_feed_header_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_order_page_order_feed_header)

    @allure.step('Убедиться, что заголовок ленты заказов есть на странице')
    def check_if_feed_header_is_on_page(self):
        return self.check_if_element_is_on_page(Locators.locator_order_page_order_feed_header)

    @allure.step('Кликнуть на флуоресцентную булочку')
    def click_fluorescent_bun(self):
        return self.click_element(Locators.locator_order_page_ingredient_fluorescent_bun)

    @allure.step('Убедиться, что поп-ап с флуоресцентной булочкой есть на странице')
    def check_if_fluorescent_bun_popup_is_on_page(self):
        return self.check_if_element_is_on_page(Locators.locator_order_page_fluorescent_bun_popup)

    @allure.step('Дождаться, чтобы флуоресцентная булочка стала кликабельной')
    def wait_until_fluorescent_bun_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_ingredient_fluorescent_bun)

    @allure.step('Дождаться, чтобы крестик для закрытия поп-апа флуоресцентной булочки стал кликабельным')
    def wait_until_fluorescent_bun_popup_cross_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_fluorescent_bun_popup_cross)

    @allure.step('Кликнуть на крестик поп-апа флуоресцентной булочки')
    def click_fluorescent_bun_popup_cross(self):
        return self.click_element(Locators.locator_order_page_fluorescent_bun_popup_cross)

    @allure.step('Определить класс локатора поп-апа флуоресцентной булочки')
    def get_class_of_a_fluorescent_bun_popup_locator(self):
        return self.get_class_of_a_locator(Locators.locator_order_page_fluorescent_bun_popup_modal_section)

    @allure.step('Перетащить в заказ флуоресцентную булочку')
    def drag_and_drop_fluorescent_bun(self):
        return self.drag_and_drop_element(Locators.locator_order_page_ingredient_fluorescent_bun_transportation,
                                          Locators.locator_order_page_slot_for_upper_bun)

    @allure.step('Получить текст счётчика флуоресцентной булочки')
    def get_text_of_a_fluorescent_bun_counter(self):
        return self.get_text_of_a_locator(Locators.locator_fluorescent_bun_counter)

    @allure.step('Кликнуть на кнопку Оформить заказ')
    def click_order_button(self):
        return self.click_element(Locators.locator_order_page_order_button)

    @allure.step('Дождаться, когда появится текст о том, что заказ оформлен')
    def wait_until_successful_order_text_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_successful_order)

    @allure.step('Убедиться, что сообщение об успешном формлении заказа есть на странице')
    def check_if_successful_order_is_on_page(self):
        return self.check_if_element_is_on_page(Locators.locator_successful_order)








