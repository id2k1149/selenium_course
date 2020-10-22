from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    link = "http://google.com"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # test_input = browser.find_element_by_name('q')
    test_input = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    test_input.send_keys("test")

    # Отправляем заполненную форму
    test_input.send_keys(Keys.RETURN)

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    first_h1 = browser.find_element_by_tag_name("h1")
    # записываем в переменную  из элемента welcome_text_elt
    h1_text = first_h1.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Accessibility Links" == h1_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
