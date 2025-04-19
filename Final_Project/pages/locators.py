from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button[type='submit']")
