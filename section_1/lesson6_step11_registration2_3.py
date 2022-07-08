from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    # Тест успешно проходит на странице
    link1 = "http://suninjuly.github.io/registration1.html"

    # Тест падает с ошибкой NoSuchElementException
    link2 = "http://suninjuly.github.io/registration2.html"

    browser.get(link1)
    # browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath("//label[text()='First name*']/..//input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_xpath("//label[text()='Last name*']/..//input")
    last_name.send_keys("Fedorov")
    email = browser.find_element_by_xpath("//label[text()='Email*']/..//input")
    email.send_keys("ivan777@ya.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
