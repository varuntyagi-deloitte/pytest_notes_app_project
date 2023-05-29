from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait
import pytest

from Logs.log_file import log_class
from PageObjects.LaunchPage import LaunchPage
from PageObjects.LoginPage import LoginPage
from utilities.readexcel import read_data_by_value as read


@pytest.mark.usefixtures("setup")
class Test_Login(log_class):
    baseUrl = "https://practice.expandtesting.com/notes/app"
    app_title = "My Notes"
    email = "abcd6@gmail.com"
    password = 123456

    def test_launch(self):
        log = self.test_log()
        wait = WebDriverWait(self.driver, 10)
        self.launch = LaunchPage(self.driver)
        log.info("The app is launched")
        self.driver.get(read("Launch_Sheet", "base_url"))
        assert self.app_title == self.launch.title_validation(), log.error("The title does not match")
        log.info("The title matching is successful")
        self.launch.click_login_button_on_launch_page()

    def test_login(self):
        log = self.test_log()
        wait = WebDriverWait(self.driver, 10)
        self.login = LoginPage(self.driver)
        log.info("The login test is started")
        self.login.enter_email_address(read("Login_Sheet", "email"))
        self.login.enter_password(read("Login_Sheet", "password"))
        self.login.click_login_button()
        assert self.login.login_success_validation() == True, log.error("The login is unsuccessful")
        log.info("Login successful")

    # def test_invalid_email_login(self):
    #     log = self.test_log()
    #     wait = WebDriverWait(self.driver, 10)
    #     self.login = LoginPage(self.driver)
    #     log.info("The Invalid Login test is started")
    #     self.login.enter_email_address(read("Login_Sheet", "email_invalid"))
    #     self.login.enter_password(read("Login_Sheet", "password"))
    #     self.login.click_login_button()
    #     try:
    #         assert self.login.login_success_validation() == True, log.error("Login Failed")
    #     except:
    #         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #         self.driver.save_screenshot(".\\Screenshots\\" + "login_failure_{now}.png")
    #
    # def test_invalid_password_login(self):
    #     log = self.test_log()
    #     wait = WebDriverWait(self.driver, 10)
    #     self.login = LoginPage(self.driver)
    #     log.info("The Invalid Login test is started")
    #     self.login.enter_email_address(read("Login_Sheet", "email"))
    #     self.login.enter_password(read("Login_Sheet", "password_invalid"))
    #     self.login.click_login_button()
    #     try:
    #         assert self.login.login_success_validation() == True, log.error("Login Failed")
    #     except:
    #         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #         self.driver.save_screenshot(f".\\Screenshots\\login_failure_{now}.png")
