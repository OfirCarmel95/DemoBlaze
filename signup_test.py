import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from read_json_data import read_data


class TestSignUp:
    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.demoBlazeUrl = "https://www.demoblaze.com/"
        yield
        self.driver.close()
        self.driver.quit()

    @pytest.mark.parametrize("username, password", read_data("data_files/signup_data.json"))
    @pytest.mark.demoblaze
    def test_sign_up(self, test_setup, username, password):
        print("getting demo blaze url...")
        self.driver.get(self.demoBlazeUrl)
        self.driver.implicitly_wait(1)
        print("click on sign up button...")
        sign_up_button = self.driver.find_element(By.ID, "signin2")
        sign_up_button.click()
        self.driver.implicitly_wait(1)
        print("filling username...")
        username_field = self.driver.find_element(By.ID, "sign-username")
        username_field.send_keys(username)
        self.driver.implicitly_wait(1)
        print("filling password...")
        password_field = self.driver.find_element(By.ID, "sign-password")
        password_field.send_keys(password)
        self.driver.implicitly_wait(1)
        print("submitting details...")
        submit_button = self.driver.find_element(By.XPATH, f'//*[@id="signInModal"]/div/div/div[3]/button[2]')
        submit_button.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        print(alert_text)
        assert alert_text == "Sign up successful."