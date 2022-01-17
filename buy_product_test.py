import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from read_json_data import read_data


class TestBuyProduct:
    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.demoBlazeUrl = "https://www.demoblaze.com/"
        yield
        self.driver.close()
        self.driver.quit()

    @pytest.mark.parametrize("product_name, customer_name, country, city, credit_card, month, year", read_data("./data_files/buy_product_data.json"))
    @pytest.mark.demoblaze
    def test_buy_product(self, test_setup, product_name, customer_name, country, city, credit_card, month, year):
        print("getting demo blaze url...")
        self.driver.get(self.demoBlazeUrl)
        self.driver.implicitly_wait(3)
        print("clicking on product...")
        product_link = self.driver.find_element(By.LINK_TEXT, f'{product_name}')
        product_link.click()
        self.driver.implicitly_wait(1)
        print("adding product to cart...")
        add_to_cart_button = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_to_cart_button.click()
        self.driver.implicitly_wait(1)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        print(alert_text)
        alert.accept()
        print("clicking on cart link...")
        cart_link = self.driver.find_element(By.ID, "cartur")
        cart_link.click()
        self.driver.implicitly_wait(1)
        print("clicking on place order...")
        place_order_button = self.driver.find_element(By.CSS_SELECTOR, f'button[data-target="#orderModal"]')
        place_order_button.click()
        print("filling name...")
        name_field = self.driver.find_element(By.ID, "name")
        name_field.send_keys(customer_name)
        self.driver.implicitly_wait(1)
        print("filling country...")
        country_field = self.driver.find_element(By.ID, "country")
        country_field.send_keys(country)
        self.driver.implicitly_wait(1)
        print("filling city...")
        city_field = self.driver.find_element(By.ID, "city")
        city_field.send_keys(city)
        self.driver.implicitly_wait(1)
        print("filling credit card information...")
        credit_card_field = self.driver.find_element(By.ID, "card")
        credit_card_field.send_keys(credit_card)
        self.driver.implicitly_wait(1)
        print("filling month...")
        month_field = self.driver.find_element(By.ID, "month")
        month_field.send_keys(month)
        self.driver.implicitly_wait(1)
        print("filling year...")
        year_field = self.driver.find_element(By.ID, "year")
        year_field.send_keys(year)
        self.driver.implicitly_wait(1)
        print("clicking on purchase...")
        purchase_button = self.driver.find_element(By.XPATH, f'//button[text()="Purchase"]')
        purchase_button.click()
        self.driver.implicitly_wait(1)
        try:
            self.driver.find_element(By.CLASS_NAME, "sweet-alert")  # success message
            print(self.driver.find_element(By.XPATH, "/html/body/div[10]/h2").text)
            print(self.driver.find_element(By.CLASS_NAME, "text-muted").text)
        except NoSuchElementException:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            print(alert_text)
