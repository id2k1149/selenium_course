from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

try:
    link = "http://automationpractice.com/index.php"
    browser = webdriver.Chrome()
    browser.get(link)

    product_containers = browser.find_elements_by_class_name('product-container')

    for index, product in enumerate(product_containers):
        hover = ActionChains(browser).move_to_element(product)
        hover.perform()
        browser.find_element_by_xpath('//*[@id="homefeatured"]/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span').click()
        time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    # browser.quit()
