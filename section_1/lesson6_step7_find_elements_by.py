from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    # elements = browser.find_elements_by_tag_name("input")
    elements = browser.find_elements(By.TAG_NAME, "input")

    for element in elements:
        element.send_keys("Мой ответ")

    # button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
