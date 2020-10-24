import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):

    def test_link_1(self):
        browser = webdriver.Chrome()
        link_1 = "http://suninjuly.github.io/registration1.html"
        browser.get(link_1)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath('//input[contains(@class, "first") and @required]')
        input1.send_keys("test")
        input2 = browser.find_element_by_xpath('//input[contains(@class, "second") and @required]')
        input2.send_keys("test")
        input3 = browser.find_element_by_xpath('//input[contains(@class, "third") and @required]')
        input3.send_keys("test")

        time.sleep(5)
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
        excepted_text = "Congratulations! You have successfully registered!"

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        # browser.quit()

        self.assertEqual(excepted_text, welcome_text, "Should be welcome text")

    def test_link_2(self):
        browser = webdriver.Chrome()
        link_2 = "http://suninjuly.github.io/registration2.html"
        browser.get(link_2)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath('//input[contains(@class, "first") and @required]')
        input1.send_keys("test")
        input2 = browser.find_element_by_xpath('//input[contains(@class, "second") and @required]')
        input2.send_keys("test")
        input3 = browser.find_element_by_xpath('//input[contains(@class, "third") and @required]')
        input3.send_keys("test")

        time.sleep(10)
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
        excepted_text = "Congratulations! You have successfully registered!"

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        # browser.quit()

        self.assertEqual(excepted_text, welcome_text, "Should be welcome text")


if __name__ == "__main__":
    unittest.main()
