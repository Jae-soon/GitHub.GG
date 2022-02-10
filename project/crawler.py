from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class crawler:
    def driver(self, input_id):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        # ChromeDriver
        s = Service('C:/selenium/chromedriver.exe')
        driver = webdriver.Chrome(service=s, chrome_options=options)
        url = "http://www.github.com/{}".format(input_id)
        driver.get(url)
        return driver

    def name(self, driver):
        try:
            input_name = driver.find_element(By.CSS_SELECTOR, 'span.p-name').text
        except:
            try:
                input_name = driver.find_element(By.CSS_SELECTOR, 'h1.h2.lh-condensed').text
            except:
                input_name = None
        return input_name

    def bio(self, driver):
        try:
            input_bio = driver.find_element(By.CSS_SELECTOR, 'div.p-note > div').text
        except:
            try:
                input_bio = driver.find_element(By.CSS_SELECTOR, 'div.color-fg-muted > div').text
            except:
                input_bio = None
        return input_bio

    def email(self, driver):
        try:
            input_email = driver.find_element(By.CSS_SELECTOR, 'li.vcard-detail > a.Link--primary').text
        except:
            input_email = None
        return input_email

    def fwer(self, driver):
        try:
            input_fwer = int(driver.find_element(By.CSS_SELECTOR, 'span.color-fg-default').text)
        except:
            input_fwer = 0
        return input_fwer

    def fwing(self, driver):
        try:
            input_fwing = int(driver.find_element(By.CSS_SELECTOR, 'span.color-fg-default:nth-child(1)').text)
        except:
            input_fwing = 0
        return input_fwing

    def rep(self, driver):
        try:
            input_rep = int(driver.find_element(By.CSS_SELECTOR, 'span.Counter').text)
        except:
            try:
                input_rep = int(driver.find_element(By.CSS_sELECTOR, 'span.Counter.js-profile-repository-count').text)
            except:
                input_rep = 0
        return input_rep

    def date(self):
        present_date = datetime.now()
        input_present_date = present_date.strftime("%Y/%m/%d %H:%M")
        return input_present_date