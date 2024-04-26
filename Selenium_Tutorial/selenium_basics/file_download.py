'''
Created on 26-Apr-2024

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
driver.get("https://demo.automationtesting.in/FileDownload.html")

'''3. Click on download button'''
download_btn=driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div[1]/a')
download_btn.click()

