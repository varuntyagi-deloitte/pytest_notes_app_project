import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Logs.log_file import log_class
from PageObjects.LaunchPage import LaunchPage
from PageObjects.RegisterPage import RegisterPage
from utilities.Random_email import random_email as email
from utilities.readexcel import read_data_by_value as read


@pytest.mark.usefixtures("setup")
class Test_Register(log_class):

    def test_launch(self):
        log = self.test_log()
        wait = WebDriverWait(self.driver, 10)
        self.launch = LaunchPage(self.driver)
        self.driver.get(read("Launch_Sheet", "base_url"))
        log.info("The App is launched for REGISTER PAGE")
        assert read("Launch_Sheet", "app_title") == self.launch.title_validation(), "Failed Test"
        log.info("App successfully launched")
        self.launch.click_create_account_button_on_launch_page()

    def test_register(self):
        log = self.test_log()
        wait = WebDriverWait(self.driver, 10)
        log.info("The registration Test is launched")
        self.register = RegisterPage(self.driver)
        self.register.enter_email_address(email)
        self.register.enter_username(read("Register_Sheet", "name"))
        self.register.enter_password(read("Login_Sheet", "password"))
        self.register.enter_confirm_password(read("Login_Sheet", "password"))
        self.register.click_register_button()
        time.sleep(2)
        assert read("Register_Sheet",
                    "reg_message") == self.register.assert_register_success_message(), "Assertion Failed"
        log.info("Registration test successfully completed")

    # def test_invalid_registration(self):
    #     log = self.test_log()
    #     wait = WebDriverWait(self.driver, 10)
    #     log.info("The Invalid registration Test is launched")
    #     self.register = RegisterPage(self.driver)
    #     self.register.enter_email_address(self.email)
    #     self.register.enter_username(self.name)
    #     self.register.enter_password(self.password)
    #     self.register.enter_confirm_password(self.confirmPassword)
    #     self.register.click_register_button()
    #     time.sleep(2)
    #     try:
    #         assert "User account created successfully" == self.register.assert_register_success_message(), log.error(
    #             "Registration failed")
    #     except:
    #         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #         self.driver.save_screenshot(".\\Screenshots\\" + "register_user_{now}.png")
