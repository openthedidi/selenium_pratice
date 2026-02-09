from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    username_input_xpath = "//input[@name='mingZi']"
    password_input_name = "password"
    login_button_xpath = "//button[@type='submit']"
    error_message_xpath = "//cms-message-modal[@class='ng-star-inserted']//div[contains(.,'查無使用者資料')]"
    success_user_div_xapth = "//div[@class='username' and text()='管理者']"

    # constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # action

    def enter_username(self, username):
        username_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.username_input_xpath)))
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, self.password_input_name)))
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_xpath)))
        login_button.click()

    def get_error_message(self):
        error_message = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.error_message_xpath)))
        return error_message.text

    def get_success_user(self):
        success_user = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.success_user_div_xapth)))
        return success_user.text
