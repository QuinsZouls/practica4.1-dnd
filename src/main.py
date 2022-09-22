from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import time
import os

TARGET_URL = 'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'

driver = webdriver.Chrome(
    os.getenv('WEBDRIVER_PATH', '/Users/alfredomedrano/Development/tools/chromedriver'))
action = ActionChains(driver)
driver.get(TARGET_URL)


driver.maximize_window()

time.sleep(2)

for i in range(1, 8):
    src = driver.find_element(By.ID, "box%i" % i)
    dest = driver.find_element(By.ID, "box10%i" % i)
    action.drag_and_drop(src, dest).perform()
    time.sleep(1)
driver.quit()