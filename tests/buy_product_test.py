import pytest
from applitools.selenium import Target

from base.read_json_data import read_data
from base.conftest import Setup
from pages.BasePage import BasePage
from pages.ProductPage import ProductPage
from pages.CartPage import CartPage
from time import sleep


@pytest.mark.usefixtures('set_up')
class TestBuyProduct(Setup):
    @pytest.mark.demoblaze
    @pytest.mark.usefixtures("eyes")
    @pytest.mark.parametrize("product_name, customer_name, country, city, credit_card, month, year", read_data(
        "./data_files/buy_product_data.json"))
    def test_buy_product(self, product_name, customer_name, country, city, credit_card, month, year):
        driver = self.driver
        eyes = self.eyes
        eyes.open(driver, "Demoblaze", "Buy Product test", {"width": 2560, "height": 1440})
        eyes.check("Buy Product test Window test", Target.window())
        basePage = BasePage(driver)
        productPage = ProductPage(driver)
        cartPage = CartPage(driver)
        print("clicking on product...")
        basePage.click_on_product(product_name)
        print("adding product to cart...")
        productPage.click_on_add_to_cart()
        basePage.get_alert()
        print("clicking on cart link...")
        basePage.go_to_cart_page()
        print("clicking on place order...")
        cartPage.click_on_place_order()
        print("filling name...")
        cartPage.enter_order_customer_name(customer_name)
        print("filling country...")
        cartPage.enter_order_country(country)
        print("filling city...")
        cartPage.enter_order_city(city)
        print("filling credit card information...")
        cartPage.enter_order_credit_card(credit_card)
        print("filling month...")
        cartPage.enter_order_month(month)
        print("filling year...")
        cartPage.enter_order_year(year)
        print("clicking on purchase...")
        cartPage.click_on_purchase()
        sleep(1)
        cartPage.get_order_message()
        eyes.check("Product bought", Target.window())
        eyes.close(False)

