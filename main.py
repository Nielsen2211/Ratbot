from selenium import webdriver
from Login.login import login

browser = webdriver.Chrome(executable_path="Main/chromedriver.exe")

browser.get('https://www.zravian.com/')

#register(browser, 'nielsen', 'monster', 'rasm2211@gmail.com', 'roman', '-+')

login(browser, 'nielsen', 'monster')