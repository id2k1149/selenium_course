from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
time.sleep(5)

browser.execute_script("document.title='Script executing';")

browser.execute_script('document.title="Script executing";')

browser.execute_script("document.title='Script executing';alert('Robots at work');")

# Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
# element = browser.execute_script('document.getElementsByName("name")')
#
# Так же есть конструкции:
# getElementById
# getElementsByTagName
# getElementsByClassName
# querySelector - для CSS
# querySelectorAll - для CSS (находит все совпадения)
#
# evaluate - для XPATH.
