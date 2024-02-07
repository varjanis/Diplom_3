from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import datafile
from tests.locators import Locators
import allure
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, locator):
        self.driver.get(locator)

    @allure.step('Открыть страницу логина')
    def open_login_page(self):
        return self.open_page(datafile.url_login_page)

    @allure.step('Дождаться, когда появится поле логина')
    def wait_until_email_field_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_login_page_input_email)

    @allure.step('Заполнить поле логин')
    def fill_in_login(self, login):
        return self.fill_in_a_field(Locators.locator_login_page_input_email, login)

    @allure.step('Заполнить поле пароль')
    def fill_in_password(self, password):
        return self.fill_in_a_field(Locators.locator_login_page_input_password, password)

    @allure.step('Дождаться, когда кнопка Войти станет кликабельна')
    def wait_until_login_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_login_page_login_button)

    @allure.step('Кликнуть на кнопку Войти')
    def click_login_button(self):
        return self.click_element(Locators.locator_login_page_login_button)

    @allure.step('Дождаться, когда будет видно кнопку Оформить заказ')
    def wait_until_order_button_is_visible(self):
        return self.wait_until_element_is_visible(Locators.locator_order_page_order_button)

    @allure.step('Кликнуть на кнопку Конструктор')
    def click_constructor_button(self):
        return self.click_element(Locators.locator_order_page_constructor_button)

    @allure.step('Дождаться, когда будет кликабельна кнопка Оформить заказ')
    def wait_until_order_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_order_button)

    @allure.step('Дождаться, когда будет кликабельна кнопка Конструктор')
    def wait_until_constructor_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_constructor_button)

    @allure.step('Дождаться, когда кнопка Личный кабинет будет кликабельна')
    def wait_until_profile_button_is_clickable(self):
        return self.wait_until_element_is_clickable(Locators.locator_order_page_profile_button)

    @allure.step('Кликнуть на кнопку Личный кабинет')
    def click_profile_button(self):
        return self.click_element(Locators.locator_order_page_profile_button)

    @allure.step('Показать текущий url')
    def show_current_url(self):
        return self.driver.current_url

    @allure.step('Найти страницу или элемент')
    def find_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на страницу или элемент')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Заполнить поле текстовым значением')
    def fill_in_a_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Проверить, что элемент есть на странице')
    def check_if_element_is_on_page(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Проверить, кликабелен ли элемент')
    def check_if_element_is_enabled(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_enabled()

    @allure.step('Прокрутить страницу до нужного элемента')
    def scroll_page_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Дождаться загрузки элемента')
    def wait_until_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Подождать 3 секунды')
    def wait_3_seconds(self):
        time.sleep(3)

    @allure.step('Дождаться, чтобы на элемент можно было кликнуть')
    def wait_until_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Установить новое окно')
    def assert_window(self):
        assert len(self.driver.window_handles) == 1

    @allure.step('Открыть и проверить новое окно')
    def check_window(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, elementlocator, targetlocator):

        drag = self.wait_until_element_is_clickable(elementlocator)
        drop = self.wait_until_element_is_clickable(targetlocator)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step('Получить класс элемента')
    def get_class_of_a_locator(self, locator):
        return self.driver.find_element(*locator).get_attribute("class")

    @allure.step('Получить текст элемента')
    def get_text_of_a_locator(self, locator):
        return self.driver.find_element(*locator).text


