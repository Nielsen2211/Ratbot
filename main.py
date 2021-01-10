from selenium import webdriver
from Login.login import login
from Login.register import register

browser = webdriver.Chrome(executable_path="chromedriver.exe")

username = 'nielsen'
password = 'monster'
mail = 'rasm2211@gmail.com'
tribe = 'roman'
location = '-+'
referrer = ''


# Create account: 1:Username 2:Password 3:Mail 4:Tribe 5:location 6:Referrer(not needed) !Remember('')!
register(browser, username, password, mail, tribe, location, referrer)

# login: 1:Username 2:password
login(browser, username, password)
