from selenium.webdriver.support.wait import WebDriverWait
import pytest

from Logs.log_file import log_class
from PageObjects.LaunchPage import LaunchPage
from PageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class Test_Login():
    baseUrl = "https://practice.expandtesting.com/notes/app"
    app_title = "My Notes"
    email = "abcd6@gmail.com"
    password = 123456

    def test_launch(self):
        wait = WebDriverWait(self.driver, 10)
        self.launch = LaunchPage(self.driver)
        self.driver.get(self.baseUrl)
        assert self.app_title == self.launch.title_validation(), "Failed Test"
        self.launch.click_login_button_on_launch_page()

    def test_login(self):
        wait = WebDriverWait(self.driver, 10)
        self.login = LoginPage(self.driver)
        self.login.enter_email_address(self.email)
        self.login.enter_password(self.password)
        self.login.click_login_button()
        assert self.login.login_success_validation() == True, "Failed Test"
