import random
import string
import os
import requests

import pymailtm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options, executable_path=(os.path.join(os.path.dirname(os.path.realpath(__file__)), "chromedriver") ))

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

tm = pymailtm.MailTm()
account = tm.get_account()

# Loop
driver.get("https://socalexplorer.metrolinktrains.com/join/Qx6w7WaHWyDue3b")
token = driver.find_element_by_name('_token').text

first_name = driver.find_element_by_name('first_name')
first_name.send_keys("".join(random.sample(string.ascii_lowercase, random.randint(3,8))))

last_name = driver.find_element_by_name('last_name')
last_name.send_keys("".join(random.sample(string.ascii_lowercase, random.randint(3,8))))

email_to_use = account.address

email = driver.find_element_by_name('email')
email.send_keys(email_to_use)

element = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CLASS_NAME, "next-btn")))
element.click()

pass_to_use = "".join(random.sample(string.ascii_lowercase, random.randint(5,7))) + "".join(random.sample(string.ascii_uppercase, random.randint(1,4))) + "".join(random.sample(string.digits, random.randint(1,4))) + "".join(random.sample(string.punctuation, random.randint(1,4)))
password = driver.find_element_by_name('password')
password.send_keys(pass_to_use)

password_confirmation = driver.find_element_by_name('password_confirmation')
password_confirmation.send_keys(pass_to_use)

tc = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.NAME, 'terms_and_condition')))
tc.click()

submit = driver.find_element_by_xpath("//button[@type='submit']").click()


print(account.get_messages()) 
