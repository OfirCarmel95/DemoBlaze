from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.login_button = {"by": By.ID, "value": "login2"}
        self.login_username = {"by": By.ID, "value": "loginusername"}
        self.login_password = {"by": By.ID, "value": "loginpassword"}
        self.login_submit_button = {"by": By.XPATH, "value": f'//*[@id="logInModal"]/div/div/div[3]/button[2]'}
        self.name_of_user = {"by": By.ID, "value": "nameofuser"}
        self.signup_button = {"by": By.ID, "value": "signin2"}
        self.signup_username = {"by": By.ID, "value": "sign-username"}
        self.signup_password = {"by": By.ID, "value": "sign-password"}
        self.signup_submit_button = {"by": By.XPATH, "value": f'//*[@id="signInModal"]/div/div/div[3]/button[2]'}
        self.contact_button = {"by": By.XPATH, "value": f'//*[@id="navbarExample"]/ul/li[2]/a'}
        self.contact_email = {"by": By.ID, "value": "recipient-email"}
        self.contact_name = {"by": By.ID, "value": "recipient-name"}
        self.contact_message = {"by": By.ID, "value": "message-text"}
        self.contact_submit_button = {"by": By.XPATH, "value": f'//*[@id="exampleModal"]/div/div/div[3]/button[2]'}
        self.go_to_cart_button = {"by": By.ID, "value": "cartur"}

    def click_on_login(self):
        login_button = self.driver.find_element(self.login_button["by"], self.login_button["value"])
        login_button.click()

    def enter_login_username(self, username):
        login_username = self.driver.find_element(self.login_username["by"], self.login_username["value"])
        login_username.clear()
        login_username.send_keys(username)

    def enter_login_password(self, password):
        login_password = self.driver.find_element(self.login_password["by"], self.login_password["value"])
        login_password.clear()
        login_password.send_keys(password)

    def submit_login(self):
        submit_login_button = self.driver.find_element(self.login_submit_button["by"],
                                                       self.login_submit_button["value"])
        submit_login_button.click()

    def get_welcome_user_message(self, username):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(
                (self.name_of_user["by"], self.name_of_user["value"]),
                f'Welcome {username}')
        )
        print(f'Welcome {username}')

    def click_on_signup(self):
        signup_button = self.driver.find_element(self.signup_button["by"], self.signup_button["value"])
        signup_button.click()

    def enter_signup_username(self, username):
        signup_username = self.driver.find_element(self.signup_username["by"], self.signup_username["value"])
        signup_username.clear()
        signup_username.send_keys(username)

    def enter_signup_password(self, password):
        signup_password = self.driver.find_element(self.signup_password["by"], self.signup_password["value"])
        signup_password.clear()
        signup_password.send_keys(password)

    def submit_signup(self):
        submit_signup_button = self.driver.find_element(self.signup_submit_button["by"],
                                                        self.signup_submit_button["value"])
        submit_signup_button.click()

    def assert_signup(self, ):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        print(alert_text)
        assert alert_text == "Sign up successful."

    def click_on_contact(self):
        contact_button = self.driver.find_element(self.contact_button["by"], self.contact_button["value"])
        contact_button.click()

    def enter_contact_email(self, email):
        contact_email = self.driver.find_element(self.contact_email["by"], self.contact_email["value"])
        contact_email.clear()
        contact_email.send_keys(email)

    def enter_contact_name(self, name):
        contact_name = self.driver.find_element(self.contact_name["by"], self.contact_name["value"])
        contact_name.clear()
        contact_name.send_keys(name)

    def enter_contact_message(self, message):
        contact_message = self.driver.find_element(self.contact_message["by"], self.contact_message["value"])
        contact_message.clear()
        contact_message.send_keys(message)

    def submit_contact(self):
        contact_submit_button = self.driver.find_element(
            self.contact_submit_button["by"],
            self.contact_submit_button["value"]
        )
        contact_submit_button.click()

    def go_to_cart_page(self):
        go_to_cart_button = self.driver.find_element(self.go_to_cart_button["by"], self.go_to_cart_button["value"])
        go_to_cart_button.click()

    def get_alert(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        print(alert.text)
        alert.accept()

    def click_on_product(self, product_name):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, product_name))
        ).click()
