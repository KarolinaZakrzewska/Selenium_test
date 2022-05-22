# import niezbednych bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
#wylaczenie komunikatu o bledzie w pycharm
import warnings
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
from time import sleep
from selenium.webdriver.support.select import Select

# dane testowe
email = "fsdgfgd@wp.pl"
sex = "F" # or "M" for male
first_name = ""
lastname = "Ryba"
password = "Abcde123456!"
birthdate = "1996-12-27"
address = "Grzybowska 56"
city = "Warsaw"
postal_code = "02123"
state = "Texas"
phone = "123234234"
alias = "warszawski"

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        # czekanie bezwarunkowe
        self.driver.implicitly_wait(10)

    def testNoNameEntered(self):
        driver = self.driver
        # 1 Kliknij "sign in"
        sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in_a.click()

        #2 Wpisz email
        email_input = driver.find_element(By.ID, "email_create")
        email_input.send_keys(email)

        # 3 Wybierz "Create account"
        create_account_btn = driver.find_element(By.ID, "SubmitCreate")
        create_account_btn.click()

        # 4 Wybierz plec
        # Wybierz Mrs
        if sex == "F":
            driver.find_element(By.ID, "id_gender2").click()
        # Wybierz Mr
        else:
            driver.find_element(By.ID, "id_gender1").click()

        # 5 Sprawdz czy pole "first name" jest puste
        customer_first_name = driver.find_element(By.ID, "customer_firstname").get_attribute("value")
        self.assertEqual(first_name, customer_first_name)

        # 6 Wpisz nazwisko
        last_name_input = driver.find_element(By.ID, "customer_lastname")
        last_name_input.send_keys(lastname)

        # 7 Sprawdz czy email jest taki sam jaki był podany przy weryfikacji
        personal_info_email = driver.find_element(By.ID, "email").get_attribute("value")
        self.assertEqual(email, personal_info_email)

        # 8 Wpisz haslo
        driver.find_element(By.ID, "passwd").send_keys(password)

        # 9 Wybierz date urodzenia
        birthday_list= birthdate.split("-")
        birthday = str(int(birthday_list[2]))
        birthmonth = birthday_list[1]
        birthyear = birthday_list[0]

        days_s = Select(driver.find_element(By.ID, "days"))
        days_s.select_by_value(birthday)

        months_s = Select(driver.find_element(By.ID, "months"))
        months_s.select_by_value(birthmonth)

        years_s = Select(driver.find_element(By.ID, "years"))
        years_s.select_by_value(birthyear)

        # 10 Sprawdz pole "first name" dla adresu
        address_firstname_input = driver.find_element(By.ID, "firstname")
        address_firstname_fact = address_firstname_input.get_attribute("value")
        # Przewiń do elementu
        address_firstname_input.location_once_scrolled_into_view
        self.assertEqual(customer_first_name, address_firstname_fact)

        # 11 Sprawdz pole "last name"
        address_lastname_fact = driver.find_element(By.ID, "lastname").get_attribute("value")
        self.assertEqual(lastname, address_lastname_fact)

        # 12 Wpisz adres
        addres_input = driver.find_element(By.ID, "address1")
        addres_input.send_keys(address)

        # 13 Wpisz miasto
        city_input = driver.find_element(By.ID, "city")
        city_input.send_keys(city)

        # 14 Wpisz kod pocztowy
        postal_code_input = driver.find_element(By.ID, "postcode")
        postal_code_input.send_keys(postal_code)

        # 15 wybierz stan
        state_select = Select(driver.find_element(By.ID, "id_state"))
        state_select.select_by_visible_text(state)

        # 16 wpisz nr telefonu komorkowego
        phone_input = driver.find_element(By.ID, "phone_mobile")
        phone_input.send_keys(phone)

        # 17 wpisz alias adresu
        address_alias = driver.find_element(By.ID, "alias")
        address_alias.clear()
        address_alias.send_keys(alias)

        # 17 kliknij register
        register_btn = driver.find_element(By.ID, "submitAccount")
        register_btn.click()

        sleep(4)

        # oczekiwany rezultat
        info_error_number = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p')

        # sprawdzamy poprawnosc komunikatu o liczbie bledow
        self.assertEqual("There is 1 error", info_error_number.text)

        # sprawdzenie poprawnosci tresci bledu
        error_messages = driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]//li')
        self.assertEqual("firstname is required.", error_messages[0].text)

        # spij 4 sekundy, zebym widzial co sie dzieje
        sleep(4)

    def tearDown(self):
        self.driver.quit()

if __name__== "__main__":
    unittest.main(verbosity = 2)
