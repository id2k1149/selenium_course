from selenium import webdriver
import time
import math
import re


def calc(xx):
    return str(math.log(abs(12*math.sin(int(xx)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Текущую вкладку можно узнать так
    current_window = browser.current_window_handle
    print(current_window)

    # выбираем вторую вкладку
    new_window = browser.window_handles[1]

    # переключаемся на вторую вкладку
    browser.switch_to.window(new_window)

    # Текущую вкладку можно узнать так
    current_window = browser.current_window_handle
    print(current_window)

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

    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall(
        "(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)",
        alert_text)
    print(text)

finally:
    time.sleep(10)
    browser.quit()
