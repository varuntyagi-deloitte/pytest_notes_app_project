import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Logs.log_file import log_class
from PageObjects.LaunchPage import LaunchPage
from PageObjects.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup")
class Test_Register():
    baseUrl = "https://practice.expandtesting.com/notes/app"
    email = "abcd96@gmail.com"
    name = "john doe"
    password = 123456
    confirmPassword = 123456
    register_success_message = "User account created successfully"
    app_title = "My Notes"

    def test_launch(self):
        wait = WebDriverWait(self.driver, 10)
        self.launch = LaunchPage(self.driver)
        self.driver.get(self.baseUrl)
        assert self.app_title == self.launch.title_validation(), "Failed Test"
        self.launch.click_create_account_button_on_launch_page()

    def test_register(self):
        wait = WebDriverWait(self.driver, 10)
        self.register = RegisterPage(self.driver)
        self.register.enter_email_address(self.email)
        self.register.enter_username(self.name)
        self.register.enter_password(self.password)
        self.register.enter_confirm_password(self.confirmPassword)
        self.register.click_register_button()
        time.sleep(2)
        assert "User account created successfully" == self.register.assert_register_success_message(), "Assertion Failed"
        self.register.click_login_button_on_successful_registration()
