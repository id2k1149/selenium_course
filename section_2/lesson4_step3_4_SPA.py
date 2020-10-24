from selenium import webdriver
import time


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)
    time.sleep(1)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(10)
    browser.quit()
