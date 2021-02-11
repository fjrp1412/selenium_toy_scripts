from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import unittest


class Twitter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='')
        self.driver.maximize_window()
        self.driver.get('https://twitter.com')

    def readCsv(self):
        PASSWORD = "no password"
        ACCOUNT = "no account"
        with open('../../src/accounts.csv') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                if(line[0] == 'twitter'):
                    ACCOUNT = line[1]
                    PASSWORD = line[2]
                    return ACCOUNT, PASSWORD

        return PASSWORD, ACCOUNT

    def enterToAccount(self):
        driver = self.driver
        log_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[2]/div[3]/a[2]/div') ))
        log_in_button.click()
        ACCOUNT, PASSWORD = self.readCsv()
        account_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.NAME, 'session[username_or_email]')))
        account_input.send_keys(ACCOUNT)
        password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(( (By.NAME, 'session[password]'))))
        password_input.send_keys(PASSWORD)
        log_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div') ))
        log_in_button.click()

    def sendTweet(self):
        self.enterToAccount()
        driver = self.driver
        tweet_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')))
        tweet_input.send_keys('enter your message')

        send_tweet_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')))
        send_tweet_button.click()

    def tearDown(self):
        self.driver.quit()

    def test_write_tweet(self):
        self.sendTweet()

if __name__ == '__main__':
    unittest.main(verbosity=2)



