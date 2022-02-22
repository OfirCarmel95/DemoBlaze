import pytest
from base.WebDriverSetup import WebDriverSetup
from base.read_json_data import read_data
from pages.BasePage import BasePage
from time import sleep


@pytest.mark.usefixtures('set_up')
class TestSignUp(WebDriverSetup):
    @pytest.mark.parametrize("username, password", read_data("./data_files/signup_data.json"))
    @pytest.mark.demoblaze
    def test_sign_up(self, username, password):
        driver = self.driver
        basePage = BasePage(driver)
        print("click on sign up button...")
        basePage.click_on_signup()
        print("filling username...")
        basePage.enter_signup_username(username)
        print("filling password...")
        basePage.enter_signup_password(password)
        sleep(1)
        print("submitting details...")
        basePage.submit_signup()
        basePage.assert_signup()