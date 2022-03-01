from locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pages.BasePage import BasePage


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.basePage = BasePage(driver)
        self.place_order_button = Locators.place_order_button
        self.order_name = Locators.order_name
        self.order_country = Locators.order_country
        self.order_city = Locators.order_city
        self.order_credit_card = Locators.order_credit_card
        self.order_month = Locators.order_month
        self.order_year = Locators.order_year
        self.order_purchase_button = Locators.order_purchase_button

    def click_on_place_order(self):
        self.driver.find_element(By.CSS_SELECTOR, self.place_order_button).click()

    def enter_order_customer_name(self, customer_name):
        self.driver.find_element(By.ID, self.order_name).clear()
        self.driver.find_element(By.ID, self.order_name).send_keys(customer_name)

    def enter_order_country(self, order_country):
        self.driver.find_element(By.ID, self.order_country).clear()
        self.driver.find_element(By.ID, self.order_country).send_keys(order_country)

    def enter_order_city(self, order_city):
        self.driver.find_element(By.ID,self.order_city).clear()
        self.driver.find_element(By.ID,self.order_city).send_keys(order_city)

    def enter_order_credit_card(self, order_credit_card):
        self.driver.find_element(By.ID, self.order_credit_card).clear()
        self.driver.find_element(By.ID, self.order_credit_card).send_keys(order_credit_card)

    def enter_order_month(self, order_month):
        self.driver.find_element(By.ID, self.order_month).clear()
        self.driver.find_element(By.ID, self.order_month).send_keys(order_month)

    def enter_order_year(self, order_year):
        self.driver.find_element(By.ID, self.order_year).clear()
        self.driver.find_element(By.ID, self.order_year).send_keys(order_year)

    def click_on_purchase(self):
        self.driver.find_element(By.XPATH, self.order_purchase_button).click()

    def get_order_message(self):
        try:
            self.driver.find_element(By.CLASS_NAME, Locators.order_success_message)
            print(self.driver.find_element(By.XPATH, Locators.order_success_message_title).text)
            print(self.driver.find_element(By.CLASS_NAME, Locators.order_success_message_body).text)
        except NoSuchElementException:
            self.basePage.get_alert()
