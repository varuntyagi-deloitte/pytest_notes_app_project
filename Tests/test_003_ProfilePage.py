import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Logs.log_file import log_class
from PageObjects.LaunchPage import LaunchPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ProfilePage import ProfilePage
from utilities.readexcel import read_data_by_value as read


@pytest.mark.usefixtures("setup")
class Test_ProfilePage(log_class):

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

    def test_update_profile(self):
        log = self.test_log()
        wait = WebDriverWait(self.driver, 10)
        log.info("The profile update has started")
        self.profile = ProfilePage(self.driver)
        self.profile.click_profile_button()
        self.profile.update_username(read("Profile_Sheet", "name"))
        self.profile.update_phone_number(read("Profile_Sheet", "phone"))
        self.profile.update_company_name(read("Profile_Sheet", "company"))
        self.profile.click_update_profile_button()
        assert read("Profile_Sheet",
                    "acc_success_message") == self.profile.update_profile_success_validation(), "Failed Test"
        log.info("Profile update finished successfully")

    def test_update_password(self):
        log = self.test_log()
        wait = WebDriverWait(self.driver, 10)
        self.profile = ProfilePage(self.driver)
        log.info("Password Update started")
        self.profile.click_change_password_link()
        self.profile.enter_current_password(read("Login_Sheet", "password"))
        self.profile.enter_new_password(read("Profile_Sheet", "new_password"))
        self.profile.enter_confirm_password(read("Profile_Sheet", "new_password"))
        self.profile.click_update_password_button()
        assert read("Profile_Sheet",
                    "pass_success_message") == self.profile.update_password_success_validation(), "Failed Test"
        log.info("Password updated successfully")
        self.profile.go_back_to_home_page()
