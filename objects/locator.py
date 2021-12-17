'''

This file contains all the object locator.
'''
from selenium.webdriver.common.by import By

# locator class helps to hold element locator.
class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector
        self._original_selector = selector

    def format_selector(self, *args) -> str:
        return self.selector.format(*args)

    def set_original_selector(self, value):
        _original_selector = value

    def get_original_selector(self):
        return self._original_selector

# this class contains all the xpath of elements which we are going to use in Financial review page
class Financial_review:
    visible=Locator(By.XPATH,"//*[@id='content']//div[contains(@data-testid,'SubscriptionPrompt-true')]")
    invisible = Locator(By.XPATH, "//*[@id='content']//div[contains(@data-testid,'SubscriptionPrompt-false')]")
    page=Locator(By.XPATH,"//html")