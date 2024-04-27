'''
Created on 27-Apr-2024

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

'''3. Take the total page count'''
pages=driver.find_elements(By.XPATH, '//*[@id="pagination"]/li')
total_pages=len(pages)

'''4. Take the total table row count'''
table_rows=driver.find_elements(By.XPATH, '//*[@id="productTable"]/tbody/tr')
total_rows=len(table_rows)

'''5. Take the product name input from the user'''
expected_product_name=input("Please enter a product name:")
a=False

'''6. Look for the product and return the price'''
for x in range(1, total_pages+1):
    page=driver.find_element(By.XPATH, f'//*[@id="pagination"]/li[{x}]/a')
    page.click()
                                
    for i in range(1, total_rows+1):
        product_name=driver.find_element(By.XPATH, f'//*[@id="productTable"]/tbody/tr[{i}]/td[2]')
        actual_product_name=product_name.text  
        if expected_product_name == actual_product_name:
            product_price=driver.find_element(By.XPATH, f'//*[@id="productTable"]/tbody/tr[{i}]/td[3]')
            print(product_price.text)
            a=True
            break
    if a==True:
        break     
         
          
                               