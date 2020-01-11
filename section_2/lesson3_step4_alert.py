from selenium import webdriver
import time
import math


def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # переключаемся на окно
    alert = browser.switch_to.alert

    # клик на ок
    alert.accept()

    # Считать значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
