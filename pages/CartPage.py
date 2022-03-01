from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.BasePage import BasePage


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.basePage = BasePage(driver)
        self.place_order_button = {"by": By.CSS_SELECTOR, "value": f'button[data-target="#orderModal"]'}
        self.order_name = {"by": By.ID, "value": "name"}
        self.order_country = {"by": By.ID, "value": "country"}
        self.order_city = {"by": By.ID, "value": "city"}
        self.order_credit_card = {"by": By.ID, "value": "card"}
        self.order_month = {"by": By.ID, "value": "month"}
        self.order_year = {"by": By.ID, "value": "year"}
        self.order_purchase_button = {"by": By.XPATH, "value": f'//button[text()="Purchase"]'}
        self.order_success_message = {"by": By.CLASS_NAME, "value": "sweet-alert"}
        self.order_success_message_title = {"by": By.XPATH, "value": "/html/body/div[10]/h2"}
        self.order_success_message_body = {"by": By.CLASS_NAME, "value": "text-muted"}

    def click_on_place_order(self):
        place_order_button = self.driver.find_element(self.place_order_button["by"], self.place_order_button["value"])
        place_order_button.click()

    def enter_order_customer_name(self, customer_name):
        customer_name_input = self.driver.find_element(self.order_name["by"], self.order_name["value"])
        customer_name_input.clear()
        customer_name_input.send_keys(customer_name)

    def enter_order_country(self, order_country):
        order_country_input = self.driver.find_element(self.order_country["by"], self.order_country["value"])
        order_country_input.clear()
        order_country_input.send_keys(order_country)

    def enter_order_city(self, order_city):
        order_city_input = self.driver.find_element(self.order_city["by"], self.order_city["value"])
        order_city_input.clear()
        order_city_input.send_keys(order_city)

    def enter_order_credit_card(self, order_credit_card):
        order_credit_card_input = self.driver.find_element(self.order_credit_card["by"],
                                                           self.order_credit_card["value"])
        order_credit_card_input.clear()
        order_credit_card_input.send_keys(order_credit_card)

    def enter_order_month(self, order_month):
        order_month_input = self.driver.find_element(self.order_month["by"], self.order_month["value"])
        order_month_input.clear()
        order_month_input.send_keys(order_month)

    def enter_order_year(self, order_year):
        order_year_input = self.driver.find_element(self.order_year["by"], self.order_year["value"])
        order_year_input.clear()
        order_year_input.send_keys(order_year)

    def click_on_purchase(self):
        purchase_button = self.driver.find_element(self.order_purchase_button["by"],
                                                   self.order_purchase_button["value"])
        purchase_button.click()

    def get_order_message(self):
        try:
            self.driver.find_element(
                self.order_success_message["by"],
                self.order_success_message["value"]
            )
            order_success_message_title = self.driver.find_element(
                self.order_success_message_title["by"],
                self.order_success_message_title["value"]
            ).text
            order_success_message_body = self.driver.find_element(
                self.order_success_message_body["by"],
                self.order_success_message_body["value"]
            ).text
            print(order_success_message_title)
            print(order_success_message_body)
        except NoSuchElementException:
            self.basePage.get_alert()
