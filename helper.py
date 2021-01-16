from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse
import time

from selenium import webdriver
from data import *


def chrome_driver(url):
    """chrome driver initialization"""
    chrome_options = webdriver.ChromeOptions()
    # without ui
    chrome_options.add_argument('headless')
    # without logs in console
    chrome_options.add_argument('--log-level=3')
    driver = webdriver.Chrome(executable_path=driver_chrome, options=chrome_options)
    # arbitrary screen size
    driver.set_window_size(1920, 1080)
    driver.get(url)
    return driver


def waiting(driver, element, count=2):
    """wait for the element to appear"""
    while count:
        count -= 1
        mytime = False
        try:
            time.sleep(1)
            mytime = WebDriverWait(driver, timeout_page_sec).until(
                EC.presence_of_element_located((By.XPATH, element)))
        except TimeoutException as e:
            print('Something went wrong... Error: ' + str(e))
        if mytime == False:
            if count == 0:
                assert False
            else:
                # reload the page and try to load it again
                time.sleep(1)
                urlparse(driver.refresh())
            continue
        else:
            assert True
            break


def js_request(driver, text):
    js = 'window.editor.getDoc().setValue(' + text + ');'
    driver.execute_script(js)
