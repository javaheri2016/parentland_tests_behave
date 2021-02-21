from behave import given, then
from test_data import *
from features.pages.home_page import ParentHomePage
import os
import time


def read_creds(file_dir: str, line_num: int) -> str:
    f = open(os.getcwd() + file_dir, "r")
    read = f.readlines()
    return read[line_num]


@given('User opens ParentLand')
def step_impl(context):
    context.browser.get('https://parent.land')


@given('User is logged in')
def step_impl(context):
    page = ParentHomePage(context)
    page.log_in_menu.click()
    page.login_username_input.send_keys(read_creds(username, 0))
    page.login_pass_input.send_keys(read_creds(password, 1))
    page.login_btn.click()


@then('It should have main logo visible')
def step_impl(context):
    page = ParentHomePage(context)
    assert page.main_logo.is_displayed() is True


@then("User logs out")
def step_imp(context):
    page = ParentHomePage(context)
    page.log_out.click()


@then("User opens sign up page")
def step_imp(context):
    page = ParentHomePage(context)
    page.signup_menu.click()


@then("User sign up")
def step_imp(context):
    page = ParentHomePage(context).SignUpPage(context)
    page.username_input.send_keys(new_username)
    page.name_input.send_keys(new_name)
    page.email_input.send_keys(read_creds(new_email, 2))
    page.town_input.send_keys(new_town)
    page.password_input.send_keys(new_pass)
    page.password2_input.send_keys(new_pass)
    page.checkbox_reg.click()
    time.sleep(5)
    page.signup_btn.click()
    time.sleep(5)


@then('User accepts cookies')
def step_imp(context):
    page = ParentHomePage(context)
    time.sleep(5)
    page.accept_cookies.click()


@then('User can see SignOut option')
def step_imp(context):
    page = ParentHomePage(context)
    assert page.log_out.is_displayed() is True


@then('User can see success message')
def step_imp(context):
    page = ParentHomePage(context).SignUpPage(context)
    assert page.success_msg.is_displayed() is True

