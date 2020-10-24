from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(2)").click()

    # другой способ
    browser.find_element_by_css_selector("[value='1']").click()

    # Есть более удобный способ
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("1")  # ищем элемент с value("1")

    # Можно использовать еще два метода:
    # Первый способ ищет элемент по видимому тексту например "Python"
    select.select_by_visible_text("text")
    # Второй способ ищет элемент по его индексу или порядковому номеру.
    # Индексация начинается с нуля.
    select.select_by_index(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
