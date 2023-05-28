from selenium.webdriver.common.by import By


class LoginPage:
    email_textbox_id = 'email'
    password_textbox_id = 'password'
    login_button_css_Selector = 'form>div.form-group>button'
    login_success_validation_xpath = '//a[@data-testid="home"]'

    '''Constructor of the Login Page Class'''

    def __init__(self, driver):
        self.driver = driver

    '''Page Actions for the Login Page'''

    def enter_email_address(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css_Selector).click()

    def login_success_validation(self):
        result = self.driver.find_element(By.XPATH, self.login_success_validation_xpath).is_displayed()
        return bool(result)