from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTests(object):

    def element_locators(self,locator):
        if  locator is None:
            return By.ID
        if locator == "linkText":
            return By.LINK_TEXT
        elif locator == "ID":
            return By.ID
        elif locator == "name":
            return By.NAME
        elif locator == "xpath":
            return By.XPATH
        else:
            print("No object found")




    def test_successful_login(self):
        baseurl = "http://localhost:10013/"
        driver = webdriver.Firefox(executable_path="/Volumes/Backup/Projects_Base/BBD-Automation-Python/BDDAutomation/utilities/geckodriver")
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(3)

        loginText = driver.find_element(self.element_locators("linkText"),"My account").click()
        emailField = driver.find_element(self.element_locators("ID"),"username").send_keys("admin")
        passwordField = driver.find_element(self.element_locators("ID"),"password").send_keys("admin")
        rememberMe = driver.find_element(self.element_locators("ID"),"rememberme").click()
        loginButton = driver.find_element(self.element_locators("name"),"login").click()
        verifyLogin = driver.find_element(self.element_locators("linkText"),"Log out")
        if verifyLogin is not None:
            print("successful Login")
        else:
            print("login Failed")
        driver.close()

ff = LoginTests()
ff.test_successful_login()




