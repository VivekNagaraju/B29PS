'''
Created on 07-Apr-2024

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)

'''2. Navigate to practice site'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3. Interact with the web elements'''
wiki_search_txtbx=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki_search_txtbx.send_keys("wikipedia")


wiki_search_btn=driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
wiki_search_btn.click()