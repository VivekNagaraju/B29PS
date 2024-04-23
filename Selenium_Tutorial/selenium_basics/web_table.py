'''
Created on 23-Apr-2024

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

'''3. Fetch the text in row 2 and column 1'''
for i in range(2, 8):
    cell=driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{i}]/td[1]')
    print(cell.text)


