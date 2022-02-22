import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from base.read_json_data import read_data
import os
cwd = os.getcwd()

class WebDriverSetup:
    @pytest.fixture()
    def read_test_conf_data(self):
        self.data = read_data("./base/test_conf.json")
        self.website_url, self.browser = self.data[0]

    @pytest.fixture(autouse=True)
    def set_up(self, read_test_conf_data):
        if self.browser.casefold() == "Chrome".casefold():
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif self.browser.casefold() == "Firefox".casefold():
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser.casefold() == "Internet Explorer".casefold():
            self.driver = webdriver.Ie(executable_path=IEDriverManager().install())
        elif self.browser.casefold() == "Opera".casefold():
            self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        else:
            raise ValueError("Invalid browser value")

        self.driver.implicitly_wait(10)
        self.driver.get(self.website_url)
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()

