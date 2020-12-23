import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstagramMessage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/francisco/chrome_web_driver')
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/')

    def enterToAccount(self):
        driver = self.driver
        USER = '' #Insert your user account
        PASSWORD = '' #Insert your password

        user_field = WebDriverWait(driver, 15).until(EC.visibility_of_element_located( (By.NAME, 'username')))
        user_field.clear()
        user_field.send_keys(USER)

        password_field = WebDriverWait(driver, 15).until(EC.visibility_of_element_located( (By.NAME, 'password')))
        password_field.clear()
        password_field.send_keys(PASSWORD)

        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
        login_button.click()

        not_now = WebDriverWait(driver, 5).until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
        not_now.click()

        not_now = WebDriverWait(driver, 5).until(EC.element_to_be_clickable( (By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
        not_now.click()


    def enterToDirect(self):
        driver = self.driver
        instagram_direct = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div')
        instagram_direct.click()

        contact_to_search = input('Select the name of a contact to send a message: ')
        contact = ""

        for i in range(1,11):
            name = driver.find_element_by_xpath(f'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{i}]/a/div/div[2]/div[1]           /div/div/div/div').text
            if(name == contact_to_search):
                contact = driver.find_element_by_xpath(f'/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{i}]/a')
                break

        self.assertNotEqual("", contact)

        contact.click()

    def enterMessage(self):
        driver = self.driver
        text_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located( ( By.TAG_NAME, 'textarea')))
        text_field.clear()
        message = input("Insert a message to sent:  ")
        text_field.send_keys(message)

        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div       [2]/div/div[2]/div/div/div[3]/button')))
        send_button.click()
        time.sleep(10)

    def test_send_message(self):
        self.enterToAccount()
        self.enterToDirect()
        self.enterMessage()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
