'''
This is the step implementation file for all the features related to financial review page.
'''
from behave import step
import reusable.driver as driver
import page.financial_review as fr


@step('user launches "{url}"')
def step_impl(context, url):
    driver.navigate(url)


@step('Verify that the subscription prompt poupped up')
def step_impl(context):
    fr.validate_popup_visible()


@step('User scrolls downs to the end of the page')
def step_impl(context):
    fr.scroll_page_down()


@step('User waits for 10 seconds')
def step_impl(context):
    fr.page_wait()


@step('Verify that pop up disappears')
def step_impl(context):
    fr.validate_popup_invisible()

