from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд,
    # пока цена станет 100
    our_price = WebDriverWait(browser, 12).\
        until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))

    button = browser.find_element_by_id("book")
    button.click()

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Нажать на кнопку Submit
    button = browser.find_element_by_id("solve")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
