from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    # input1 = browser.find_element_by_xpath('//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    # input3 = browser.find_element_by_xpath('//input[@class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    # button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

    # решение № 2
    # buttons = browser.find_element_by_xpath("//button")
    # for button in buttons:
    #     if button.text == 'Submit':
    #         button.click()

except Exception as e:
    print(e)

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
