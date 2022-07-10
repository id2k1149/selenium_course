from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://icp.administracionelectronica.gob.es/icpplus/index"

try:
    browser.get(link)
    selection_list = browser.find_element(By.ID, "form")
    selection_list.click()

except Exception as e:
    print(e)

finally:
    # time.sleep(10)
    browser.quit()
