from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# By.ID – поиск по уникальному атрибуту id элемента;
# By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
# By.XPATH – поиск элементов с помощью языка запросов XPath;
# By.NAME – поиск по атрибуту name элемента;
# By.TAG_NAME – поиск по названию тега;
# By.CLASS_NAME – поиск по атрибуту class элемента;
# By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
# By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")

print("button=", button)
time.sleep(5)

browser.quit()

