from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.login_button = Locators.login_button
        self.login_username = Locators.login_username
        self.login_password = Locators.login_password
        self.login_submit_button = Locators.login_submit_button
        self.name_of_user = Locators.name_of_user
        self.signup_button = Locators.signup_button
        self.signup_username = Locators.signup_username
        self.signup_password = Locators.signup_password
        self.signup_submit_button = Locators.signup_submit_button
        self.contact_button = Locators.contact_button
        self.contact_email = Locators.contact_email
        self.contact_name = Locators.contact_name
        self.contact_message = Locators.contact_message
        self.contact_submit_button = Locators.contact_submit_button
        self.go_to_cart_button = Locators.go_to_cart_button

    def click_on_login(self):
        self.driver.find_element(By.ID, self.login_button).click()

    def enter_login_username(self, username):
        self.driver.find_element(By.ID, self.login_username).clear()
        self.driver.find_element(By.ID, self.login_username).send_keys(username)

    def enter_login_password(self, password):
        self.driver.find_element(By.ID, self.login_password).clear()
        self.driver.find_element(By.ID, self.login_password).send_keys(password)

    def submit_login(self):
        self.driver.find_element(By.XPATH, self.login_submit_button).click()

    def get_welcome_user_message(self, username):
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, self.name_of_user), f'Welcome {username}')
        )
        print(f'Welcome {username}')

    def click_on_signup(self):
        self.driver.find_element(By.ID, self.signup_button).click()

    def enter_signup_username(self, username):
        self.driver.find_element(By.ID, self.signup_username).clear()
        self.driver.find_element(By.ID, self.signup_username).send_keys(username)

    def enter_signup_password(self, password):
        self.driver.find_element(By.ID, self.signup_password).clear()
        self.driver.find_element(By.ID, self.signup_password).send_keys(password)

    def submit_signup(self):
        self.driver.find_element(By.XPATH, self.signup_submit_button).click()

    def assert_signup(self, ):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        print(alert_text)
        assert alert_text == "Sign up successful."

    def click_on_contact(self):
        self.driver.find_element(By.XPATH, self.contact_button).click()

    def enter_contact_email(self, email):
        self.driver.find_element(By.ID, self.contact_email).clear()
        self.driver.find_element(By.ID, self.contact_email).send_keys(email)

    def enter_contact_name(self, name):
        self.driver.find_element(By.ID, self.contact_name).clear()
        self.driver.find_element(By.ID, self.contact_name).send_keys(name)

    def enter_contact_message(self, message):
        self.driver.find_element(By.ID, self.contact_message).clear()
        self.driver.find_element(By.ID, self.contact_message).send_keys(message)

    def submit_contact(self):
        self.driver.find_element(By.XPATH, self.contact_submit_button).click()

    def go_to_cart_page(self):
        self.driver.find_element(By.ID, self.go_to_cart_button).click()

    def get_alert(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        print(alert.text)
        alert.accept()

    def click_on_product(self, product_name):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, product_name))
        ).click()
