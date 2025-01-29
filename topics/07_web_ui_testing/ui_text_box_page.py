from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"

        """Page locators"""
        self.full_name_input = (By.ID, "userName")
        self.email_input = (By.ID, "userEmail")
        self.current_address_input = (By.ID, "currentAddress")
        self.permanent_address_input = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")

        """Output locators"""
        self.output_name = (By.ID, "name")
        self.output_email = (By.ID, "email")
        self.output_current_address = (By.XPATH, "//p[@id='currentAddress']")
        self.output_permanent_address = (By.XPATH, "//p[@id='permanentAddress']")

    def open(self):
        """Opening the Text Box page"""
        self.driver.get(self.url)

    def fill_form(self, full_name, email, current_address, permanent_address):
        """Filling the provided data"""
        self.driver.find_element(*self.full_name_input).send_keys(full_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.current_address_input).send_keys(current_address)
        self.driver.find_element(*self.permanent_address_input).send_keys(permanent_address)

    def submit(self):
        """Clicking submit button"""
        self.driver.find_element(*self.submit_button).click()

    def get_output_text(self):
        """Retrieving displayed output"""
        return {
            "name": self.driver.find_element(*self.output_name).text,
            "email": self.driver.find_element(*self.output_email).text,
            "current_address": self.driver.find_element(*self.output_current_address).text,
            "permanent_address": self.driver.find_element(*self.output_permanent_address).text
        }
