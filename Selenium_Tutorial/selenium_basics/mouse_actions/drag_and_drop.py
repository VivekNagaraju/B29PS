'''
Created on 11-Apr-2024

@author: admin
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)

'''2. Navigate to practice site'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3.a. Drag and drop by source and target'''
source=driver.find_element(By.ID, 'draggable')
target=driver.find_element(By.ID, 'droppable')
my_actions=ActionChains(driver)
# my_actions.scroll_to_element(target)
my_actions.scroll_by_amount(0, 400).perform()
time.sleep(2)
my_actions.drag_and_drop(source, target).perform()

'''3.b. Drag and drop by offset'''
# my_actions.drag_and_drop_by_offset(source, 100, 50).perform()