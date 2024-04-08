'''
Created on 08-Apr-2024

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

'''3. Switch to the frame'''
driver.switch_to.frame("frame-one796456169") # entering the frame

'''4. Enter your name in Name field under Frames'''
name_txt_bx=driver.find_element(By.ID, 'RESULT_TextField-0')
name_txt_bx.send_keys("Vivek")

'''5. Exit from the frame'''
driver.switch_to.parent_frame() # exiting the frame