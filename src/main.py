

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

answers = {
    '//*[@id="box1"]': '//*[@id="box101"]',
    '//*[@id="box2"]': '//*[@id="box102"]',
    '//*[@id="box3"]': '//*[@id="box103"]',
    '//*[@id="box4"]': '//*[@id="box104"]',
    '//*[@id="box5"]': '//*[@id="box105"]',
    '//*[@id="box6"]': '//*[@id="box106"]',
    '//*[@id="box7"]': '//*[@id="box107"]',
}

for x, y in answers.items():
    src = driver.find_element(By.XPATH, x)
    dest = driver.find_element(By.XPATH, y)
    action.drag_and_drop(src, dest).perform()
    time.sleep(1)

driver.quit()