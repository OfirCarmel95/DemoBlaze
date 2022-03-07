import pytest
from applitools.selenium import Target
from base.conftest import Setup
from base.read_json_data import read_data
from pages.BasePage import BasePage
from time import sleep


@pytest.mark.usefixtures('set_up')
class TestSignUp(Setup):
    @pytest.mark.usefixtures("eyes")
    @pytest.mark.parametrize("username, password", read_data("./data_files/signup_data.json"))
    @pytest.mark.demoblaze
    def test_sign_up(self, username, password):
        driver = self.driver
        eyes = self.eyes
        eyes.open(driver, "Demoblaze", "Signup test", {"width": 2560, "height": 1440})
        eyes.check("Signup Window test", Target.window())
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
        eyes.check("Signed up", Target.window())
        eyes.close(False)