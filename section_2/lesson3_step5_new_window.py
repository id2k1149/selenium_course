from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    link_1 = "https://google.com"
    browser.get(link_1)

    link_2 = "https://yandex.ru"
    browser.get(link_2)

    current_window = browser.current_window_handle
    print("current_window = ", current_window)

    # Для переключения на новую вкладку надо явно указать,
    # на какую вкладку мы хотим перейти.
    window_name = "https://yandex.ru"
    browser.switch_to.window(window_name)

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(first_window)


finally:
    time.sleep(5)
    browser.quit()
