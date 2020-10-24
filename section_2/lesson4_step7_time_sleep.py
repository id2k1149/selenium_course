import time
from selenium.webdriver.common.by import By
# Задание явных ожиданий реализуется
# с помощью инструментов WebDriverWait и expected_conditions.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/wait2.html"
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд,
    # пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).\
        until(EC.element_to_be_clickable((By.ID, "verify")))

    # Если мы захотим проверять, что кнопка становится неактивной после отправки данных,
    # то можно задать негативное правило с помощью метода until_not:

    # button = WebDriverWait(browser, 5).until_not(
    #     EC.element_to_be_clickable((By.ID, "verify"))
    # )

    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(10)
    browser.quit()
