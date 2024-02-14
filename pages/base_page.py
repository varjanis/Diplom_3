from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import allure


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
        return self.find_page(locator).click()

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

    @allure.step('Дождаться, чтобы на элемент можно было кликнуть')
    def wait_until_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

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

    @allure.step('Дождаться, когда не будет виден заданный текст элемента')
    def wait_for_text_not_to_be_present(self, locator, text):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.none_of(expected_conditions.text_to_be_present_in_element(
                locator, text)))


