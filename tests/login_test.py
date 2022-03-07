import pytest
from applitools.selenium import Target
from base.conftest import Setup
from base.read_json_data import read_data
from pages.BasePage import BasePage
from time import sleep



@pytest.mark.usefixtures('set_up')
class TestLogin(Setup):
    @pytest.mark.demoblaze
    @pytest.mark.usefixtures('eyes')
    @pytest.mark.parametrize("username, password", read_data("./data_files/login_data.json"))
    def test_login(self, username, password):
        driver = self.driver
        eyes = self.eyes
        eyes.open(driver, "Demoblaze", "Login test", {"width": 2560, "height": 1440})
        eyes.check("Login Window test", Target.window())
        basePage = BasePage(driver)
        print("click on login button...")
        basePage.click_on_login()
        print("filling username...")
        basePage.enter_login_username(username)
        print("filling password...")
        basePage.enter_login_password(password)
        sleep(1.5)
        print("submitting details...")
        basePage.submit_login()
        basePage.get_welcome_user_message(username)
        eyes.check("Logged in", Target.window())
        eyes.close(False)
