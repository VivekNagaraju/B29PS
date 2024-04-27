from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launch Chrome Browser'''
my_options=webdriver.ChromeOptions()
my_options.add_experimental_option("detach", True)
my_options.add_argument("start-maximized")
driver=webdriver.Chrome(options=my_options)
driver.implicitly_wait(5)

'''2. Navigate to practice site'''
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

'''3. Enter UserName'''
user_name=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
user_name.send_keys("Admin")

'''4. Enter Password'''
password=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
password.send_keys("admin123")

'''5. Click on login button'''
login=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
login.click()

'''6. Validate the login functionality'''
actual_url=driver.current_url
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
# print(actual_url)

if expected_url in actual_url:
    print("Login successfull")
    
else:
    print("Login failed")

    
