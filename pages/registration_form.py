from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#All selectors used in these methods
email_add_id = "email_create"
first_name_id = "customer_firstname"
create_account_id = "SubmitCreate"
last_name_id = "customer_lastname"
password_id = "passwd"
days_id = "days"
months_id = "months"
years_id = "years"
first_name_address_id = "firstname"
last_name_address_id = "lastname"
city_id = "city"
state_id = "id_state"
postal_code_id = "postcode"
country_id = "id_country"
phone_id = "phone_mobile"
alias_id = "alias"
register_id = "submitAccount"
error_message_one_defect_xpath = '//div[@class="alert alert-danger"]/p'
error_message_info_about_defect_xpath = '//div[@class="alert alert-danger"]//li'


#All variables
email_input = "tesxtddfd@gmail.com"
first_name_input = "ania"
last_name_input = "Ryba"
password_input = "Abcde123456!"
birthdate_select = "1996-12-27"
address_input = "Grzybowska 56"
city_input = "Warsaw"
state_select = "Texas"
postal_code_input = "02123"
country_select = "United States"
phone_input = "123234234"
alias_input = "warszawski"

class RegistrationForm:

  def __init__(self, driver):
    self.driver = driver

  def set_email(self):
    self.driver.find_element(By.ID, email_add_id).send_keys(email_input)

  def click_button_create_account(self):
    self.driver.find_element(By.ID, create_account_id).click()

  def set_first_name(self):
    self.driver.find_element(By.ID, first_name_id).send_keys(first_name_input)

  def set_last_name(self):
    self.driver.find_element(By.ID, last_name_id).send_keys(last_name_input)

  def set_password(self):
    self.driver.find_element(By.ID, password_id).send_keys(password_input)

  def set_date_birth(self):
    birthday_list = birthdate_select.split("-")
    birthday = str(int(birthday_list[2]))
    birthmonth = birthday_list[1]
    birthyear = birthday_list[0]

    days_s = Select(self.driver.find_element(By.ID, days_id))
    days_s.select_by_value(birthday)

    months_s = Select(self.driver.find_element(By.ID, months_id))
    months_s.select_by_value(birthmonth)

    years_s = Select(self.driver.find_element(By.ID, years_id))
    years_s.select_by_value(birthyear)

  def set_first_name_address_or_equal_first_name_input(self):
    assert self.driver.find_element(By.ID, first_name_address_id).get_attribute("value") == first_name_input, "Assertion passed, Expected first name with adress equal first name input"

  def set_last_name_address_or_equal_last_name_input(self):
    assert self.driver.find_element(By.ID, last_name_address_id).get_attribute("value") == last_name_input, "Assertion passed, Expected last name with adress equal last name input"

  def set_city(self):
    self.driver.find_element(By.ID, city_id).send_keys(city_input)

  def set_state(self):
    Select(self.driver.find_element(By.ID, state_id))
    self.driver.find_element(By.ID, state_id).send_keys(state_select)

  def set_postal_code(self):
    self.driver.find_element(By.ID, postal_code_id).send_keys(postal_code_input)

  def set_country(self):
    Select(self.driver.find_element(By.ID, country_id))
    self.driver.find_element(By.ID, country_id).send_keys(country_select)

  def set_phone(self):
    self.driver.find_element(By.ID, phone_id).send_keys(phone_input)

  def set_alias(self):
    self.driver.find_element(By.ID, alias_id).clear()
    self.driver.find_element(By.ID, alias_id).send_keys(alias_input)

  def set_register(self):
    self.driver.find_element(By.ID, register_id).click()

  def error_message_one_defect(self):
    assert (self.driver.find_element(By.XPATH, error_message_one_defect_xpath)).text == "There is 1 error", "Assertion passed, Expected last name with adress equal last name input"

  def error_message_info_about_defect(self):
    assert (self.driver.find_element(By.XPATH, error_message_info_about_defect_xpath)).text == "address1 is required.", "Assertion passed, Expected information to add address1"


