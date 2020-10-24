from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Найти element1 + element2
    element1 = browser.find_element_by_id("num1")
    element2 = browser.find_element_by_id("num2")

    # Считать значение для переменной num1 + num2
    x1 = element1.text
    x2 = element2.text

    # Посчитать x1 x2
    y = int(x1) + int(x2)
    y_value = str(y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y_value)

    # Отправляем
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
