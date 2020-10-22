from selenium import webdriver
import time

try:
    link = "https://google.com"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # test_input = browser.find_element_by_name('q')
    element = browser.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[1]/a')
    element.click()

    browser.back()
    search_element = browser.find_element_by_name('q')
    search_element.send_keys('spectrum')
    go_button = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    go_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
