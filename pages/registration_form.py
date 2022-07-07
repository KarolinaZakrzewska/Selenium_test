from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.select import Select

#All selectors used in these methods
email_add_id = "email_create"
first_name_id = "customer_firstname"
create_account_id = "SubmitCreate"
last_name_id = "customer_lastname"
password_id = "passwd"
address_id = "address1"
first_name_address_id = "firstname"
last_name_address_id = "lastname"
city_id = "city"
state_id = "id_state"
postal_code_id = "postcode"
country_id = "id_country"
phone_id = "phone_mobile"
alias_id = "alias"
register_id = "submitAccount"
error_message_xpath = '//div[@class="alert alert-danger"]/p'


#All variables
#email_input = fake.email()
email_input = "testfd@gmail.com"
first_name_input = "ania"
last_name_input = "Ryba"
password_input = "Abcde123456!"
birthdate_select = "1996-12-27"
days = "days"
months = "months"
years = "years"
address_input = "Grzybowska 56"
city_input = "Warsaw"
state_select = "Texas"
postal_code_input = "02123"
country_select = "United States"
phone_input = "123234234"
alias_input = "warszawski"

class RegistrationForm:

  def set_email(self):
    driver = self.driver
    driver.find_element(By.ID, email_add_id).send_keys(email_input)

  def click_button_create_account(self):
    driver = self.driver
    driver.find_element(By.ID, create_account_id).click()

  def set_first_name(self):
    driver = self.driver
    driver.find_element(By.ID, first_name_id).send_keys(first_name_input)

  def set_last_name(self):
    driver = self.driver
    driver.find_element(By.ID, last_name_id).send_keys(last_name_input)

  def set_password(self):
    driver = self.driver
    driver.find_element(By.ID, password_id).send_keys(password_input)

  def set_date_birth(self):
    driver = self.driver

    birthday_list = birthdate_select.split("-")
    birthday = str(int(birthday_list[2]))
    birthmonth = birthday_list[1]
    birthyear = birthday_list[0]

    days_s = Select(driver.find_element(By.ID, days))
    days_s.select_by_value(birthday)

    months_s = Select(driver.find_element(By.ID, months))
    months_s.select_by_value(birthmonth)

    years_s = Select(driver.find_element(By.ID, years))
    years_s.select_by_value(birthyear)

  def set_first_name_address_or_equal_first_name_input(self):
    driver = self.driver
    assert driver.find_element(By.ID, first_name_address_id).get_attribute("value") == first_name_input, "Assertion passed, Expected first name with adress equal first name input"

  def set_last_name_address_or_equal_last_name_input(self):
    driver = self.driver
    assert driver.find_element(By.ID, last_name_address_id).get_attribute("value") == last_name_input, "Assertion passed, Expected last name with adress equal last name input"

  def set_address(self):
    driver = self.driver
    driver.find_element(By.ID, address_id).send_keys(address_input)

  def set_city(self):
    driver = self.driver
    driver.find_element(By.ID, city_id).send_keys(city_input)

  def set_state(self):
    driver = self.driver
    Select(driver.find_element(By.ID, state_id))
    driver.find_element(By.ID, state).send_keys(state_select)

  def set_postal_code(self):
    driver = self.driver
    driver.find_element(By.ID, postal_code).send_keys(postal_code_input)

  def set_country(self):
    driver = self.driver
    Select(driver.find_element(By.ID, country_id))
    driver.find_element(By.ID, country).send_keys(country_select)

  def set_phone(self):
    driver = self.driver
    driver.find_element(By.ID, phone_id).send_keys(phone_input)

  def set_alias(self):
    driver = self.driver
    driver.find_element(By.ID, alias_id).clear()
    driver.find_element(By.ID, alias_id).send_keys(alias_input)

  def set_register(self):
    driver = self.driver
    driver.find_element(By.ID, register_id).click()

  def error_message(self):
    driver = self.driver
    assert (driver.find_element(By.XPATH, error_message_xpath)).text == "There is 1 error", "Assertion passed, Expected last name with adress equal last name input"

    # error_messages = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]//li')
    # self.assertEqual("firstname is required.", error_messages[0].text)
