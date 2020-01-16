from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = "google.com"
    browser.get(link)

    assert abs(-42) == -42, "Should be absolute value of a number"

    # Функция is_element_present() вспомогательная.
    assert self.is_element_present('create_class_button', timeout=30), "No create class button"

    # указать, где именно произошла ошибка
    assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"

    # Форматирование строк с помощью конкатенации
    actual_result = "abrakadabra"
    print("Wrong text, got " + actual_result + ", something wrong")

    # Форматирование строк с помощью str.format
    print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

    # Форматирование строк с помощью f-strings
    str1 = "one"
    str2 = "two"
    str3 = "three"
    print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

    # Пример 2:
    actual_result = "abrakadabra"
    f"Wrong text, got {actual_result}, something wrong"

    # неправильно:
    assert self.catalog_link.text == "Каталог", \
        f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'"

    # правильно:
    catalog_text = self.catalog_link.text  # считываем текст и записываем его в переменную
    assert catalog_text == "Каталог", \
        f"Wrong language, got {catalog_text} instead of 'Каталог'"

finally:
    time.sleep(5)
    browser.quit()
