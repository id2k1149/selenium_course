from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    # открываем модальное окно 1
    browser.execute_script("alert('Окно 1');")
    time.sleep(3)

    # переключаемся на окно
    alert = browser.switch_to.alert
    time.sleep(3)

    # клик на ок
    alert.accept()
    time.sleep(3)

    # открываем модальное окно 2
    browser.execute_script("alert('Окно 2');")
    time.sleep(3)

    # получить текст из alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert = browser.switch_to.alert
    alert.accept()

    # открываем модальное окно 3
    browser.execute_script("confirm('Окно 3');")
    time.sleep(3)

    # Другой вариант согласиться
    confirm = browser.switch_to.alert
    confirm.accept()

    # открываем модальное окно 4
    browser.execute_script("confirm('Окно 4');")
    time.sleep(3)

    # вариант отказаться
    confirm = browser.switch_to.alert
    confirm.dismiss()

    # открываем модальное окно 5
    browser.execute_script("prompt('Окно 5');")
    time.sleep(3)

    # ввод текста окно
    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    time.sleep(10)
    prompt.accept()
    time.sleep(10)

finally:
    time.sleep(5)
    browser.quit()
