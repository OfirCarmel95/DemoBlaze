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
    @pytest.fixture(params=read_data("./base/test_conf.json"))
    def read_test_conf_data(self, request):
        self.website_url, self.browser, self.remote = request.param

    @pytest.fixture(autouse=True)
    def set_up(self, read_test_conf_data):
        if self.remote:
            if self.browser.casefold() == "Chrome".casefold():
                dc = webdriver.DesiredCapabilities.CHROME
            elif self.browser.casefold() == "Firefox".casefold():
                dc = webdriver.DesiredCapabilities.FIREFOX
            elif self.browser.casefold() == "Internet Explorer".casefold():
                dc = webdriver.DesiredCapabilities.INTERNETEXPLORER
            elif self.browser.casefold() == "Opera".casefold():
                dc = webdriver.DesiredCapabilities.OPERA
            else:
                raise ValueError("Invalid browser value")
            self.driver = webdriver.Remote(
                desired_capabilities=dc,
                command_executor="http://localhost:4444/wd/hub",
            )
        else:
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
        if not self.remote:
            self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()

