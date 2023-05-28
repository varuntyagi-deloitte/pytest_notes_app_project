import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HomePage:
    add_note_button_xpath = '//button[@data-testid="add-new-note"]'
    select_category_id = 'category'
    title_textbox_id = 'title'
    description_textbox_id = "description"
    create_button_xpath = '//button[@data-testid="note-submit"]'
    edit_button_xpath = '//div[@data-testid="notes-list"]/div/div/div[4]/div/button[@data-testid="note-edit"]'
    title = "The note is edited"
    title_heading_in_notes_xpath = '//div[@data-testid="notes-list"]/div/div/div[@data-testid="note-card-title"]'
    no_note_validation_xpath = '//h4[@data-testid="no-notes-message"]'
    notes_created_validation = '//div[@data-testid="notes-list"]'
    checkbox_xpath = '//div[@data-testid="notes-list"]/div/div/div[4]/input'
    task_completion_message_class_name = 'info-text'
    search_textbox_id = 'search-note-input'
    logout_button_xpath = '//button[@data-testid="logout"]'
    launch_page_welcome_text_css_selector = '.fw-bold.lh-1'

    '''Constructor for the Home Page Class'''

    def __init__(self, driver):
        self.driver = driver

    '''Action methods for the Home Page'''

    def click_add_note_button(self):
        self.driver.find_element(By.XPATH, self.add_note_button_xpath).click()

    def select_category_of_the_note(self, category):
        select_category = Select(self.driver.find_element('id', self.select_category_id))
        select_category.select_by_value(category)

    def enter_title_of_note(self, title):
        self.driver.find_element(By.ID, self.title_textbox_id).send_keys(title)

    def enter_description_of_note(self, description):
        self.driver.find_element(By.ID, self.description_textbox_id).send_keys(description)

    def click_create_button(self):
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()

    def created_note_validation(self):
        result = self.driver.find_element(By.XPATH, self.notes_created_validation).is_displayed()
        return bool(result)

    def edit_the_note(self):
        elements = self.driver.find_elements(By.XPATH, self.edit_button_xpath)
        for i in elements:
            self.driver.execute_script("arguments[0].click();", i)
            self.enter_title(self.title)
            self.click_save_button()
            time.sleep(2)

    def enter_title(self, title):
        self.driver.find_element(By.ID, self.title_textbox_id).clear()
        self.driver.find_element(By.ID, self.title_textbox_id).send_keys(title)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()

    def edited_notes_validation(self):
        elements = self.driver.find_elements(By.XPATH, self.title_heading_in_notes_xpath)
        for i in elements:
            title_updated_text = i.text
            if title_updated_text == self.title:
                return True
            else:
                return False

    def check_checkbox_to_mark_test_as_complete(self):
        elements = self.driver.find_elements(By.XPATH, self.checkbox_xpath)
        for i in elements:
            self.driver.execute_script("arguments[0].click();", i)
            break

    def one_note_mark_as_completed_validation(self):
        result = self.driver.find_element(By.CLASS_NAME, 'info-text').is_displayed()
        return bool(result)
        # assert self.home.one_note_mark_as_completed_validation() == True, "Failed Test"

    def enter_search_text_in_search_box(self, text):
        self.driver.find_element(By.ID, self.search_textbox_id).clear()
        self.driver.find_element(By.ID, self.search_textbox_id).send_keys(text)

    def no_note_found_validation(self):
        no_note_validation = self.driver.find_element(By.XPATH, self.no_note_validation_xpath).text
        return no_note_validation
        # assert no_note_validation == "Couldn't find any notes"

    def note_found_validation(self):
        # search_text = self.driver.find_element(By.ID, self.search_textbox_id).text
        # elements = self.driver.find_elements(By.XPATH, self.title_heading_in_notes_xpath)
        # for i in elements:
        #     text = i.text
        #     if text == search_text:
        #         return True
        #     else:
        #         return False
        result = self.driver.find_element(By.XPATH, self.notes_created_validation).is_displayed()
        return bool(result)

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

    def logout_validation(self):
        logout_validation_message = self.driver.find_element(By.CSS_SELECTOR, self.launch_page_welcome_text_css_selector).text
        return logout_validation_message
        # assert logout_validation_message == "Welcome to Notes App"
