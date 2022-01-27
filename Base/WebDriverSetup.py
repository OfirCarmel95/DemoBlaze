import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class WebDriverSetup:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome(service=Service("../drivers/chromedriver.exe"))
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
