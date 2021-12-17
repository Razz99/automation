'''
This file contains all the functions related to financial review page.
'''
import time
import reusable.reusable as reusable
from objects.locator import Financial_review

def validate_popup_visible():
    reusable.verify_element_present(Financial_review.visible)
    reusable.verify_css_properties(Financial_review.visible,'fixed', '0px')

def validate_popup_invisible():
    reusable.verify_element_present(Financial_review.invisible)

def scroll_page_down():
    reusable.scroll_down(Financial_review.page,scroll_time=20)

def page_wait():
    time.sleep(10)