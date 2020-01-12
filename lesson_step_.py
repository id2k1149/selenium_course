from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    link = ""
    browser.get(link)

finally:
    time.sleep(5)
    browser.quit()
