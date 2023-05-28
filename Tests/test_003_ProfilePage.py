import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Logs.log_file import log_class
from PageObjects.LaunchPage import LaunchPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ProfilePage import ProfilePage


@pytest.mark.usefixtures("setup")
class Test_ProfilePage():
    baseUrl = "https://practice.expandtesting.com/notes/app"
    app_title = "My Notes"
    account_details_success_message = "Profile updated successful"
    password_update_success_message = "The password was successfully updated"
    name = "johnny"
    phone_number = 1234567891
    company_name = 'abcd'
    current_password = 123456
    new_password = 1234567
    confirm_password = 1234567
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

    def test_update_profile(self):
        wait = WebDriverWait(self.driver, 10)
        self.profile = ProfilePage(self.driver)
        self.profile.click_profile_button()
        self.profile.update_username(self.name)
        self.profile.update_phone_number(self.phone_number)
        self.profile.update_company_name(self.company_name)
        self.profile.click_update_profile_button()
        assert self.account_details_success_message == self.profile.update_profile_success_validation(), "Failed Test"

    def test_update_password(self):
        wait = WebDriverWait(self.driver, 10)
        self.profile = ProfilePage(self.driver)
        self.profile.click_change_password_link()
        self.profile.enter_current_password(self.current_password)
        self.profile.enter_new_password(self.new_password)
        self.profile.enter_confirm_password(self.confirm_password)
        self.profile.click_update_password_button()
        assert self.password_update_success_message == self.profile.update_password_success_validation(), "Failed Test"
        self.profile.go_back_to_home_page()
