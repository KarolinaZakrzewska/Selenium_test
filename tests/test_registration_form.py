from selenium import webdriver
from pages.registration_form import RegistrationForm
import unittest
from selenium.webdriver.support.select import Select

class TestRegistrationForm:
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    driver.maximize_window()
    driver.implicitly_wait(3)

    def test_email_input_validation(self):
        RegistrationForm.set_email(self)

    def test_click_button_create_account_validation(self):
        RegistrationForm.click_button_create_account(self)

    def test_first_name_input_validation(self):
        RegistrationForm.set_first_name(self)

    def test_last_name_input_validation(self):
        RegistrationForm.set_last_name(self)

    def test_password_input_validation(self):
        RegistrationForm.set_password(self)

    def test_date_birth_select_validation(self):
        RegistrationForm.set_date_birth(self)

    def test_first_name_address_or_equal_first_name_input_validation(self):
        RegistrationForm.set_first_name_address_or_equal_first_name_input(self)

    def test_last_name_address_or_equal_last_name_input_validation(self):
        RegistrationForm.set_last_name_address_or_equal_last_name_input(self)

    def test_city_input_validation(self):
        RegistrationForm.set_city(self)

    def test_state_select_validation(self):
        RegistrationForm.set_state(self)

    def test_postal_code_input_validation(self):
        RegistrationForm.set_postal_code(self)

    def test_country_input_validation(self):
        RegistrationForm.set_country(self)

    def test_phone_input_validation(self):
        RegistrationForm.set_phone(self)

    def test_alias_input_validation(self):
        RegistrationForm.set_alias(self)

    def test_click_register_validation(self):
        RegistrationForm.set_register(self)

    def test_error_message_validation(self):
        RegistrationForm.error_message(self)

    def tearDown(self):
        self.driver.quit()

if __name__== "__main__":
    unittest.main(verbosity = 2)
