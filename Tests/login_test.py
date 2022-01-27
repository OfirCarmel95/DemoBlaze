import pytest
from Base.WebDriverSetup import WebDriverSetup
from Base.read_json_data import read_data
from Pages.BasePage import BasePage
from time import sleep


@pytest.mark.usefixtures('set_up')
class TestLogin(WebDriverSetup):
    @pytest.mark.demoblaze
    @pytest.mark.parametrize("username, password", read_data("../data_files/login_data.json"))
    def test_login(self, username, password):
        driver = self.driver
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

