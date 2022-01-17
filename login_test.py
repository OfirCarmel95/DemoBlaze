import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_json_data import read_data

class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.demoBlazeUrl = "https://www.demoblaze.com/"
        yield
        self.driver.close()
        self.driver.quit()
    @pytest.mark.demoblaze
    @pytest.mark.parametrize("username, password", read_data("./data_files/login_data.json"))
    def test_login(self, test_setup, username, password):
        print("getting demo blaze url...")
        self.driver.get(self.demoBlazeUrl)
        self.driver.implicitly_wait(1)
        print("click on login button...")
        login_button = self.driver.find_element(By.ID, "login2")
        login_button.click()
        self.driver.implicitly_wait(1)
        print("filling username...")
        username_field = self.driver.find_element(By.ID, "loginusername")
        username_field.send_keys(username)
        self.driver.implicitly_wait(1)
        print("filling password...")
        password_field = self.driver.find_element(By.ID, "loginpassword")
        password_field.send_keys(password)
        self.driver.implicitly_wait(1)
        print("submitting details...")
        submit_button = self.driver.find_element(By.XPATH, f'//*[@id="logInModal"]/div/div/div[3]/button[2]')
        submit_button.click()
        self.driver.implicitly_wait(1)
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.ID, "nameofuser"), f'Welcome {username}'))
        print(f'Welcome {username}')

