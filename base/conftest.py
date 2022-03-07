import pytest
import os
from applitools.selenium import Eyes, BatchInfo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager
from base.read_json_data import read_data
from dotenv import load_dotenv
cwd = os.getcwd()

class Setup:
    @pytest.fixture(scope="module")
    def batch_info(self):
        return BatchInfo("Some general Test cases name")

    @pytest.fixture(autouse=True, name="eyes", scope="function")
    def eyes_setup(self, batch_info):
        self.eyes = Eyes()
        load_dotenv()
        self.eyes.api_key = os.getenv("APPLITOOLS_API_KEY")
        self.eyes.configure.batch = batch_info
        yield self.eyes
        # If the test was aborted before eyes.close was called, ends the test as aborted.
        self.eyes.abort()

    @pytest.fixture(params=read_data("./base/test_conf.json"))
    def read_test_conf_data(self, request):
        self.website_url, self.browser, self.remote = request.param

    @pytest.fixture(autouse=True)
    def set_up(self, read_test_conf_data):
        if self.remote:
            if self.browser.casefold() == "Chrome".casefold():
                options = webdriver.ChromeOptions()
            elif self.browser.casefold() == "Firefox".casefold():
                options = webdriver.FirefoxOptions()
            elif self.browser.casefold() == "Internet Explorer".casefold():
                options = webdriver.IeOptions()
            elif self.browser.casefold() == "Opera".casefold():
                options = webdriver.Opera()
            else:
                raise ValueError("Invalid browser value")
            self.driver = webdriver.Remote(
                options=options,
                command_executor="http://localhost:4444/wd/hub",
            )
        else:
            if self.browser.casefold() == "Chrome".casefold():
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            elif self.browser.casefold() == "Firefox".casefold():
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            elif self.browser.casefold() == "Internet Explorer".casefold():
                self.driver = webdriver.Ie(service=Service(IEDriverManager().install()))
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

