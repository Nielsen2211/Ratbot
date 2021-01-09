from selenium import webdriver
from Login.login import login
from Login.register import register

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get('https://www.zravian.com/')


# Create account: 1:Username 2:Password 3:Mail 4:Tribe 5:location 6:Referrer(not needed) !Remember('')!
register(browser, 'nielsen', 'monster', 'rasm2211@gmail.com', 'roman', '-+')

# login: 1:Username 2:password
login(browser, 'nielsen', 'monster')
