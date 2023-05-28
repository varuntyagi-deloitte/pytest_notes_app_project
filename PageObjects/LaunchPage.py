from selenium.webdriver.common.by import By


class LaunchPage:
    launch_page_login_button_link_text = "Login"
    launch_page_create_Account_button_css_selector = ".btn.btn-outline-secondary.btn-lg.px-4"

    def __init__(self, driver):
        self.driver = driver

    '''Action methods for LaunchPage Class'''

    def click_login_button_on_launch_page(self):
        self.driver.find_element(By.LINK_TEXT, self.launch_page_login_button_link_text).click()

    def click_create_account_button_on_launch_page(self):
        self.driver.find_element(By.CSS_SELECTOR, self.launch_page_create_Account_button_css_selector).click()

    def title_validation(self):
        title = self.driver.title
        return title