from selenium.webdriver.common.by import By


class Locators:


    # локаторы страницы восстановления пароля

    locator_forgot_password_page_login_link = (By.XPATH, './/a[@class="Auth_link__1fOlj" and @href="/login"]')
    locator_forgot_password_page_revoke_button = (By.XPATH, './/button[text()="Восстановить"]')
    locator_forgot_password_page_email_field = (By.XPATH, './/input[@class="text input__textfield text_type_main-default"]')
    locator_forgot_password_page_password_field = (By.XPATH, './/input[@type="password"]')
    locator_forgot_password_page_eye_icon = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    locator_label_password_field = (By.XPATH, './/label[text()="Пароль"]')
    locator_label_password_div_field = (By.XPATH, './/label[text()="Пароль"]/parent::div')

    # локаторы страницы авторизации

    locator_login_page_input_email = (By.XPATH, './/input[@name="name"]')
    locator_login_page_input_password = (By.XPATH, './/input[@type="password"]')
    locator_login_page_login_button = (By.XPATH, './/button[text()="Войти"]')
    locator_login_page_forgot_password_link = (By.XPATH, './/a[@href="/forgot-password"]')

    # локаторы главной страницы

    locator_order_page_order_button = (By.XPATH,
        './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    locator_order_page_profile_button = (By.XPATH, './/p[text()="Личный Кабинет"]')
    locator_order_page_constructor_button = (By.XPATH, './/p[text()="Конструктор"]')
    locator_order_page_order_feed_button = (By.XPATH, './/a[@href="/feed"]')
    locator_order_page_order_feed_header = (By.XPATH, './/h1[text()="Лента заказов"]')

    # локаторы страницы заказа

    locator_order_page_ingredient_fluorescent_bun = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    locator_order_page_fluorescent_bun_popup = (By.XPATH, './/ul[@class="Modal_modal__statsList__6cEm5"]')
    locator_order_page_fluorescent_bun_popup_cross = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    locator_order_page_fluorescent_bun_popup_modal_section = (By.XPATH, './/section[@class="Modal_modal__P3_V5"]')
    locator_fluorescent_bun_counter = (By.XPATH, './/p[@class="counter_counter__num__3nue1"]')
    locator_order_page_slot_for_upper_bun = (By.XPATH, './/li[@class="BurgerConstructor_basket__listItem__aWMu1 mr-4"]')
    locator_order_page_ingredient_fluorescent_bun_transportation = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]')
    locator_successful_order = (By.XPATH, './/p[@class="undefined text text_type_main-medium mb-15"]')
    locator_order_page_order_number = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    locator_successful_order_cross = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    locator_successful_order_tick = (By.XPATH, './/img[@class="Modal_modal__image__2nh17"]')

    # локаторы страницы лента заказов

    locator_feed_first_order = (By.XPATH, './/a[@class ="OrderHistory_link__1iNby"]')
    locator_feed_first_order_popup = (By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
    locator_feed_popup_section_popup_closed = (By.XPATH, './/section[@class ="Modal_modal__P3_V5"]')
    locator_feed_popup_section_popup_open = (By.XPATH, './/section[@class ="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    locator_feed_orders_in_progress = (By.XPATH, './/p[@class="text text_type_main-medium"]')
    locator_feed_orders_ready = (By.XPATH, './/li[@class ="text text_type_digits-default mb-2"]')
    locator_feed_number_of_most_recent_order = (By.XPATH, './/div[@class="OrderHistory_textBox__3lgbs mb-6"]/p[@class="text text_type_digits-default"]')
    locator_feed_orders_in_progress_number = (By.XPATH, './/li[@class ="text text_type_digits-default mb-2"]')
    locator_feed_total_orders_number = (By.XPATH, '(//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[1]')
    locator_feed_today_orders_number = (By.XPATH, '(//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[2]')

    # локаторы страницы профиля (личный кабинет пользователя)

    locator_profile_page_header_logo = (By.XPATH, './/a[@href = "/"]')
    locator_profile_page_constructor_button = (By.XPATH, './/a[@class="AppHeader_header__link__3D_hX" and @href="/"]')
    locator_profile_page_order_history_button = (By.XPATH, './/a[text()="История заказов"]')
    locator_profile_page_logout_button = (By.XPATH, './/button[@type="button" and text()="Выход"]')
    locator_order_history_my_recent_order = (By.XPATH, './/a[@class ="OrderHistory_link__1iNby"]')
    locator_order_history_my_recent_order_number = (By.XPATH, './/p[@class="text text_type_digits-default"]')



