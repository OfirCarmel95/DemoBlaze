from locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = Locators.add_to_cart_button

    def click_on_add_to_cart(self):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.add_to_cart_button))
        ).click()
