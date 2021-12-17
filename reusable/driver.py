'''
This class contains driver instance related codes
'''
import os
from selenium import webdriver
browser="chrome"

class SeleniumDriverNotFound(Exception):
    pass

instance = None

# this function initializes the driver instance
def initialize():
    global instance
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        instance = webdriver.Chrome(executable_path=os.getcwd()+"/driver/chromedriver.exe", chrome_options=chrome_options)
        instance.maximize_window()
    else:
        raise SeleniumDriverNotFound(f'{browser} is not currently supported')

# this function is used to open URL
def navigate(url):
    instance.get(url)

#  this function closes the browser instance
def stop_instance():
    instance.quit()