from selenium import webdriver
import time
import unittest


def reg_link(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath('//input[@class="form-control first"][@required]').send_keys("Иван")
    browser.find_element_by_xpath('//input[@class="form-control second"][@required]').send_keys("Иванов")
    browser.find_element_by_xpath('//input[@class="form-control third"][@required]').send_keys("ivan@yandex.ru")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    h1_text = browser.find_element_by_tag_name("h1").text

    # закрываем браузер после всех манипуляций
    browser.quit()
    return h1_text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(reg_link("http://suninjuly.github.io/registration1.html"),
                         expected_text,
                         "registration test")

    def test_reg2(self):
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(reg_link("http://suninjuly.github.io/registration2.html"),
                         expected_text,
                         "registration test")


if __name__ == "__main__":
    unittest.main()

# pytest -v lesson2_step13_2.py
