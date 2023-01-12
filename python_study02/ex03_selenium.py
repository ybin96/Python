from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/chromedriver_win32_109/chromedriver.exe")
driver.get("https://www.python.org/")
print(driver.title)

while True:
    pass

