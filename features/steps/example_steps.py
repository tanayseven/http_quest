from behave import given, when, then
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebDriver:
    DOWNLOAD_DIR = '/tmp'

    def __init__(self):
        headless=bool(os.environ.get('HEADLESS'))
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-extensions')
        if headless:
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--no-sandbox')
        self.options.add_experimental_option(
            'prefs', {
                'download.default_directory': self.DOWNLOAD_DIR,
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': True
            }
        )
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def login(self):
        self.driver.get('http://localhost')



@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):
    assert number > 1 or number == 0
    context.tests_count = number

@when('we start selenium webbrowser')
def step_impl(context):
    context.webbrowser = WebDriver()
    context.webbrowser.login()
    context.webbrowser.close()

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
