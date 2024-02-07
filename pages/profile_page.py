from pages.base_page import BasePage
from tests.locators import Locators
import allure


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    @allure.step('Дождаться, когда будет видена кнопка История заказов')
    def wait_until_order_history_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_profile_page_order_history_button)

    @allure.step('Убедиться, что на странице отображается кнопка История заказов')
    def check_if_order_history_button_is_on_page(self):
        return self.check_if_element_is_on_page(Locators.locator_profile_page_order_history_button)

    @allure.step('Кликнуть на кнопку История заказов')
    def click_order_history_button(self):
        return self.click_element(Locators.locator_profile_page_order_history_button)

    @allure.step('Кликнуть на кнопку Выход')
    def click_logout_button(self):
        return self.click_element(Locators.locator_profile_page_logout_button)
