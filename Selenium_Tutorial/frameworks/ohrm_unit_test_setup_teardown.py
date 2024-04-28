import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestOHRMLogin(unittest.TestCase):


    def setUp(self):
        '''1. Launch Chrome Browser'''
        my_options=webdriver.ChromeOptions()
        my_options.add_experimental_option("detach", True)
        my_options.add_argument("start-maximized")
        self.driver=webdriver.Chrome(options=my_options)
        self.driver.implicitly_wait(5)
        
        '''2. Navigate to practice site'''
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    def tearDown(self):
        pass


    def test_navigation(self):        
        '''3. Validation'''
        login_title=self.driver.find_element(By.TAG_NAME, 'h5')
        login_text=login_title.text
        self.assertEqual(login_text, "Login", "Navigation test failed")

    def test_login(self):
        
        '''3. Enter UserName'''
        user_name=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        user_name.send_keys("Admin")
        
        '''4. Enter Password'''
        password=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password.send_keys("admin123")
        
        '''5. Click on login button'''
        login=self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login.click()
        
        '''6. Validate the login functionality'''
        actual_url=self.driver.current_url
        expected_url="dashboard/index"
        self.assertIn(expected_url, actual_url, "Login failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()