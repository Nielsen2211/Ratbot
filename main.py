from selenium import webdriver
from Login.login import login
from Login.register import register
from Village.fields import fields_scan

browser = webdriver.Chrome(executable_path="chromedriver.exe")

# Login Information
username = 'nielsen'
password = 'monster'
mail = 'rasm2211@gmail.com'
tribe = 'roman'
location = '-+'
referrer = ''
register_on = False

# Upgrade Fields
upgradefields = 1
#upgrademode =



if register_on == True:
    register(browser, username, password, mail, tribe, location, referrer)
elif register_on == False:
        login(browser, username, password)


fields_scan(browser, upgradefields)