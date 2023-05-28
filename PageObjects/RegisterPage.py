from selenium.webdriver.common.by import By

from Config.config import TestData


class RegisterPage:
    email_textbox_id = "email"
    name_textbox_id = "name"
    password_textbox_id = "password"
    confirmPassword_textbox_id = "confirmPassword"
    register_button_css_Selector = ".btn.btn-lg.btn-primary.d-block.w-100"
    success_message_validation_css_selector = '.alert.alert-success>b'
    login_link_on_successful_registration = '.text-decoration-none.me-3'

    '''Constructor of the Register Page Class'''

    def __init__(self, driver):
        self.driver = driver
        # self.driver.get(TestData.base_url)

    '''Page Actions for Register Page'''

    '''Click the Create Account Button on Launch page'''

    def enter_email_address(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_username(self, name):
        self.driver.find_element(By.ID, self.name_textbox_id).send_keys(name)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirmPassword_textbox_id).send_keys(confirm_password)

    def click_register_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.register_button_css_Selector).click()

    def assert_register_success_message(self):
        alert_success_message = self.driver.find_element(By.CSS_SELECTOR,
                                                         self.success_message_validation_css_selector).text
        return alert_success_message

    def click_login_button_on_successful_registration(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_link_on_successful_registration).click()

