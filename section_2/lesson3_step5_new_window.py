from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    link = "https://google.com"
    browser.get(link)

    current_window = browser.current_window_handle

    browser.switch_to.window(window_name)

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(first_window)


finally:
    time.sleep(5)
    browser.quit()
