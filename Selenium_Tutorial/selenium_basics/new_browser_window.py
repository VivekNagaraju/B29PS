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

print(driver.current_window_handle)

'''3. Click on New Browser Window button'''
new_browser_window_btn=driver.find_element(By.CSS_SELECTOR, "#HTML4 > div.widget-content > button")
new_browser_window_btn.click()

'''4. Switch to new window'''
win_handles=driver.window_handles
driver.switch_to.window(win_handles[1])
print(driver.current_window_handle)

'''5. Click on desktops in Nav bar'''
menu_desktops=driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a')
menu_desktops.click()