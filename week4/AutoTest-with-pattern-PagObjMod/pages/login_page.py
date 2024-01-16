from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "https://selenium1py.pythonanywhere.com/en-gb/" != current_url, "It's wrong link" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not provided"
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISER_FORM), "Registration form not provided"
        
    def register_new_user(self, email, passwd):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)
        passwd_field = self.browser.find_element(*LoginPageLocators.PASSWD)
        passwd_field.send_keys(passwd)
        confirm_field = self.browser.find_element(*LoginPageLocators.CONFR_PASSWD)
        confirm_field.send_keys(passwd)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
