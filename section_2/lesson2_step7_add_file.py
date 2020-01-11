import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
print("current dir ", current_dir)

# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')

with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file

element = browser.find_element_by_id("file")
element.send_keys(file_path)

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
