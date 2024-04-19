'''
Created on 19-Apr-2024

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
driver.get("https://demo.guru99.com/test/simple_context_menu.html")

'''3. Right click on (right click me) button'''
right_click_me=driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
my_actions=ActionChains(driver)
my_actions.context_click(right_click_me).perform()