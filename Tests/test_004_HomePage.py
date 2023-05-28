import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Logs.log_file import log_class
from PageObjects.HomePage import HomePage
from PageObjects.LaunchPage import LaunchPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ProfilePage import ProfilePage


@pytest.mark.usefixtures("setup")
class Test_HomePage():
    baseUrl = "https://practice.expandtesting.com/notes/app"
    app_title = "My Notes"
    email = "abcd6@gmail.com"
    password = 123456
    title = "It's a title"
    description = "It's a description"
    valid_text = "The note is edited"
    invalid_text = "Varun"
    no_note_found_message = "Couldn't find any notes"
    launch_page_welcome_text = "Welcome to Notes App"
    delete_account_success_text = "Your account has been deleted. You should create a new account to continue."

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

    @pytest.mark.parametrize("category", ["Home", "Work", "Personal"])
    def test_create_notes(self, category):
        wait = WebDriverWait(self.driver, 10)
        self.home = HomePage(self.driver)
        self.home.click_add_note_button()
        self.home.select_category_of_the_note(category)
        self.home.enter_title_of_note(self.title)
        self.home.enter_description_of_note(self.description)
        self.home.click_create_button()
        time.sleep(1)
        assert self.home.created_note_validation() == True, "Failed Test"

    def test_edit_notes(self):
        wait = WebDriverWait(self.driver, 10)
        self.home = HomePage(self.driver)
        self.home.edit_the_note()
        assert self.home.edited_notes_validation() == True, "Failed Test"

    def test_mark_one_note_complete(self):
        wait = WebDriverWait(self.driver, 10)
        self.home = HomePage(self.driver)
        self.home.check_checkbox_to_mark_test_as_complete()
        time.sleep(2)
        assert self.home.one_note_mark_as_completed_validation() == True, "Failed Test"

    def test_search_invalid_notes(self):
        wait = WebDriverWait(self.driver, 10)
        self.home = HomePage(self.driver)
        self.home.enter_search_text_in_search_box(self.invalid_text)
        time.sleep(2)
        assert self.no_note_found_message == self.home.no_note_found_validation(), "Failed Test"

    def test_search_valid_notes(self):
        wait = WebDriverWait(self.driver, 10)
        self.home = HomePage(self.driver)
        self.home.enter_search_text_in_search_box(self.valid_text)
        assert self.home.note_found_validation() == True, "Failed Test"

    def test_logout_functionality(self):
        wait = WebDriverWait(self.driver, 10)
        self.home = HomePage(self.driver)
        self.home.click_logout_button()
        time.sleep(2)
        assert self.launch_page_welcome_text == self.home.logout_validation(), "Failed Test"

    def test_delete_account(self):
        wait = WebDriverWait(self.driver, 10)
        self.profile = ProfilePage(self.driver)
        self.profile.click_profile_button()
        self.profile.click_delete_account_button()
        assert self.delete_account_success_text == self.profile.delete_account_success_validation(), "Failed Test"