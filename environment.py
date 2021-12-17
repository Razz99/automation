'''
This file contains logic related to framework configuration.
'''
import reusable.driver as driver

def before_all(context):
    driver.initialize()

def after_all(context):
    driver.stop_instance()