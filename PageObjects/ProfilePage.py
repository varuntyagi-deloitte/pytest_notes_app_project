from selenium.webdriver.common.by import By


class ProfilePage:
    profile_button_link_text = 'Profile'
    name_textbox_name = 'name'
    phone_textbox_name = 'phone'
    company_textbox_name = 'company'
    update_profile_button_css_Selector = '.form-group.mt-2.mb-3>button'
    success_message_class_name = 'toast-body'
    change_password_link_xpath = '//div[@class="col-md-9 col-lg-7"]/ul/li/button[@data-testid="change-password"]'
    current_password_textbox_name = 'currentPassword'
    new_password_textbox_name = 'newPassword'
    confirm_password_textbox_name = 'confirmPassword'
    update_password_button_css_selector = '.form-group.mb-3>button'
    link_to_home_id = 'Capa_1'
    delete_account_button_css_selector = 'data-testid="delete-account"'
    delete_account_success_message_xpath = '//div[@data-testid="alert-message"]'

    def __init__(self, driver):
        self.driver = driver

    '''Page Actions for the Profile Page'''

    def click_profile_button(self):
        self.driver.find_element(By.LINK_TEXT, self.profile_button_link_text).click()

    def update_username(self, name):
        self.driver.find_element(By.NAME, self.name_textbox_name).clear()
        self.driver.find_element(By.NAME, self.name_textbox_name).send_keys(name)

    def update_phone_number(self, phone):
        self.driver.find_element(By.NAME, self.phone_textbox_name).clear()
        self.driver.find_element(By.NAME, self.phone_textbox_name).send_keys(phone)

    def update_company_name(self, company):
        self.driver.find_element(By.NAME, self.company_textbox_name).clear()
        self.driver.find_element(By.NAME, self.company_textbox_name).send_keys(company)

    def click_update_profile_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.update_profile_button_css_Selector).click()

    def update_profile_success_validation(self):
        alert_message = self.driver.find_element(By.CLASS_NAME, self.success_message_class_name).text
        return alert_message

    def click_change_password_link(self):
        self.driver.find_element(By.XPATH, self.change_password_link_xpath).click()

    def enter_current_password(self, current_password):
        self.driver.find_element(By.NAME, self.current_password_textbox_name).send_keys(current_password)

    def enter_new_password(self, new_password):
        self.driver.find_element(By.NAME, self.new_password_textbox_name).send_keys(new_password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.NAME, self.confirm_password_textbox_name).send_keys(confirm_password)

    def click_update_password_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.update_password_button_css_selector)
        self.driver.execute_script("arguments[0].click();", element)

    def update_password_success_validation(self):
        alert_message = self.driver.find_element(By.CLASS_NAME, self.success_message_class_name).text
        return alert_message

    def go_back_to_home_page(self):
        self.driver.find_element(By.ID, self.link_to_home_id).click()

    def click_delete_account_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ).click()

    def delete_account_success_validation(self):
        delete_account_validation = self.driver.find_element(By.XPATH, self.delete_account_success_message_xpath).text
        return delete_account_validation
        #assert delete_account_validation == "Your account has been deleted. You should create a new account to continue.", "Failed Test"
