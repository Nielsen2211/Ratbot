from selenium import webdriver
from Login.login import login
from Login.register import register

browser = webdriver.Chrome(executable_path="chromedriver.exe")

# login information
username = 'nielsen'
password = 'monster'
mail = 'rasm2211@gmail.com'
tribe = 'roman'
location = '-+'
referrer = ''


register(browser, username, password, mail, tribe, location, referrer)

login(browser, username, password)
