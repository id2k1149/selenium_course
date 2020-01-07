from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("test")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("test")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')

    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)

    # Нажать на кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
