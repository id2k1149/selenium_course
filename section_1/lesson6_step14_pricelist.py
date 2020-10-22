from selenium import webdriver
import time

try:
    link = "https://www.phptravels.net/offers"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    span_tags = browser.find_elements_by_tag_name('span')

    price_list = []
    for each in span_tags:
        price_list.append(each.text)

    print(price_list)

    clean_price_list = []

    for each in price_list:
        if each.startswith('$'):
            price_number = each[1:]
            int_price = int(price_number.replace(',', ''))
            clean_price_list.append(int_price)

    print(sorted(clean_price_list))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
