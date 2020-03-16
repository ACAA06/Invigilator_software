#
# Copyright © 2019 Maestro Creativescape
#
# SPDX-License-Identifier: GPL-3.0
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
import re
from os import remove
from os import environ
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk import capture_exception


load_dotenv("config.env")
chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)

# Grab the current window
main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle

driver.get("http://127.0.0.1:8000")
username=driver.find_element_by_id('exampleInputEmail1')
pwd=driver.find_element_by_id('exampleInputPassword1')
btn=driver.find_element_by_name('submit')
username.send_keys('clemadr')
pwd.send_keys('12345')
btn.click()

driver.get("http://127.0.0.1:8000/addfaculty")

driver.get("http://127.0.0.1:8000/addtimetable")
driver.get("http://127.0.0.1:8000/addexam")
driver.get("http://127.0.0.1:8000/allotfaculty")
btn = driver.find_element_by_name('submit')
btn.click()
sleep(10)
driver.quit()
