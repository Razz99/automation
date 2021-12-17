'''
This file contains all the functions which can be reused in any project.

'''
import reusable.driver as driver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

#waits until the condition is satisfied
def _execute_with_wait(condition):
    return WebDriverWait(driver.instance,3).until(condition)

#checks whetehr the element is esists or not
def element_exists(locator):
    try:
        time.sleep(1)
        _execute_with_wait(
            ec.presence_of_element_located(
                (locator.l_type, locator.selector))
        )
        return True
    except TimeoutException:
        return False

#returns element
def get_elements(locator):
    return driver.instance.find_elements(locator.l_type, locator.selector)

# counts the element having same locator
def count_all_elements(locator):
    return len(driver.instance.find_elements(locator.l_type, locator.selector))

# scrolls the page simulating key down press for given times
def scroll_down(locator,scroll_time):
    page=driver.instance.find_element(locator.l_type,locator.selector)
    for num in range(0,scroll_time):
        page.send_keys(Keys.PAGE_DOWN)

#veries the css properties for an element
def verify_css_properties(locator,*args):
    css_prop=[]
    expect_css_prop=list(args)
    element=driver.instance.find_element(locator.l_type,locator.selector)
    css_prop.append(element.value_of_css_property("position"))
    css_prop.append(element.value_of_css_property("bottom"))
    css_prop.sort()
    expect_css_prop.sort()
    if css_prop == expect_css_prop:
        assert True
    else:
        assert False, "Popups is not coming from the bottom of the screen"




#verifies if element esists in the page.
def verify_element_present(locator):

    if element_exists(locator):
        assert True

    else:
        assert False, " Element is not available on the page"

