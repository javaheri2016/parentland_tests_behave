from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
import os


class ParentHomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://parent.land')

    locator_dictionary = {
        "main_logo": (By.ID, 'logo_img'),
        "log_in_menu": (By.XPATH, '//A[@title="Zaloguj się"]'),
        "signup_menu": (By.XPATH, '//A[@title="Zarejestruj się"]'),
        "login_username_input": (By.XPATH, '//INPUT[@class="form-control sq-username"]'),
        "login_pass_input": (By.XPATH, '//INPUT[@class="sq-password form-control"]'),
        "login_btn": (By.XPATH, '//BUTTON[@class="btn btn-lg btn-default btn-block"][text()="Zaloguj "]'),
        "log_out": (By.XPATH, '//A[@title="Wyloguj"]'),
        "accept_cookies": (By.XPATH, '//A[@class="tplis-cl-button tplis-cl-button-accept"]')
    }

    class SignUpPage(BasePage):
        def __init__(self, context):
            BasePage.__init__(
                self,
                context.browser,
                base_url='https://parent.land')
        locator_dictionary = {
            "username_input": (By.XPATH, "//INPUT[@id='user_login']"),
            "name_input": (By.XPATH, "//INPUT[@id='user_first']"),
            "email_input": (By.XPATH, "//INPUT[@id='user_email']"),
            "town_input": (By.XPATH, "//INPUT[@id='miasto']"),
            "password_input": (By.XPATH, "//INPUT[@id='user_pass']"),
            "password2_input": (By.XPATH, "//INPUT[@id='user_pass2']"),
            "checkbox_reg": (By.XPATH, "//INPUT[@id='akceptacjaregulaminuparentland-0']"),
            "signup_btn": (By.XPATH, "//BUTTON[@id='regist1']"),
            "success_msg": (By.XPATH, "//DIV[@class='bf-alert success']")
        }
