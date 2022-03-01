from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = {"by": By.LINK_TEXT, "value": "Add to cart"}

    def click_on_add_to_cart(self):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((
                self.add_to_cart_button["by"],
                self.add_to_cart_button["value"]
            ))
        ).click()
