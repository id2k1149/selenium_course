from selenium import webdriver
import time

# попробуем вызвать alert в браузере с помощью WebDriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
time.sleep(5)

# Если внутри скрипта вам также понадобится использовать кавычки,
# а для выделения скрипта вы уже используете двойные кавычки,
# то в скрипте следует поставить одинарные:
browser.execute_script("document.title='Script executing';")

# Такой формат записи тоже будет работать:
browser.execute_script('document.title="Script executing";')

# можно все внутренние кавычки экранировать обратным слэшем вот так:
browser.execute_script("alert(\"Robots at work\");")

# Можно с помощью этого метода выполнить сразу несколько инструкций,
# перечислив их через точку с запятой.
# Изменим сначала заголовок страницы, а затем вызовем alert:
browser.execute_script("document.title='Script executing'; alert('Robots at work');")

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
