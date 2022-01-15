import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        global demoBlazeUrl
        demoBlazeUrl = "https://www.demoblaze.com/"
        yield
        self.driver.close()
        self.driver.quit()

    @pytest.mark.parametrize("email, name, message",
                             [("example@gmail.com", "Random Full Name", "an example message"),
                              ("", "Random Full Name", "an example message")]
                             )
    def test_contact(self, test_setup, email, name, message):
        print("getting demo blaze url...")
        self.driver.get(demoBlazeUrl)
        self.driver.implicitly_wait(1)
        print("clicking on contact button...")
        contact_button = self.driver.find_element(By.XPATH, f'//*[@id="navbarExample"]/ul/li[2]/a')
        contact_button.click()
        self.driver.implicitly_wait(1)
        print("filling email...")
        email_field = self.driver.find_element(By.ID, "recipient-email")
        email_field.send_keys(email)
        self.driver.implicitly_wait(1)
        print("filling name...")
        name_field = self.driver.find_element(By.ID, "recipient-name")
        name_field.send_keys(name)
        self.driver.implicitly_wait(1)
        print("filling message...")
        message_field = self.driver.find_element(By.ID, "message-text")
        message_field.send_keys(message)
        print("submitting information...")
        submit_button = self.driver.find_element(By.XPATH, f'//*[@id="exampleModal"]/div/div/div[3]/button[2]')
        submit_button.click()
        self.driver.implicitly_wait(1)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        print(alert_text)
        alert.accept()
