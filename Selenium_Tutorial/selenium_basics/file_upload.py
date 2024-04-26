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
driver.get("https://demo.automationtesting.in/FileUpload.html")

'''3. Upload a file'''
browse_btn=driver.find_element(By.ID, "input-4")
browse_btn.send_keys(r"C:\Users\admin\Downloads\samplefile (2).pdf")


driver.get_screenshot_as_file(r"C:\Users\admin\Downloads\ss264.png")