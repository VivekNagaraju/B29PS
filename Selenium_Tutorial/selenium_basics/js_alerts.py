'''
Created on 08-Apr-2024

@author: admin
'''
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

'''3. Click on Alert button'''
alert_btn=driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button[1]')
alert_btn.click()

# time.sleep(2) # hard wait

'''4. Accept the alert'''
al=driver.switch_to.alert #Alert class object
al.accept()

'''5. Click on Confirm Box and accept it'''
confirm_box_btn=driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button[2]')
confirm_box_btn.click()

confirm_bx_alert=driver.switch_to.alert
confirm_bx_alert.accept()

'''6. Click on Confirm Box and dismiss it'''
confirm_box_btn.click()
confirm_bx_alert.accept()

'''7. Click on Prompt, enter your name and accept it'''
prompt_btn=driver.find_element(By.CSS_SELECTOR, '#HTML9 > div.widget-content > button:nth-child(3)')
prompt_btn.click()

prompt_alert=driver.switch_to.alert
prompt_alert.send_keys("Vivek")
prompt_alert.accept()

'''8. Click on Prompt and dismiss it'''
prompt_btn.click()
prompt_alert.dismiss()

