from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import allure
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, locator):
        self.driver.get(locator)

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
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))

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

    def drag_and_drop_element(self, elementlocator, targetlocator):
        #action_chains = ActionChains(self.driver)
        #action_chains.drag_and_drop(elementlocator, targetlocator).perform()

        drag = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(elementlocator))
        drop = WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(targetlocator))
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()


