def login(browser, usernameinput, passwordinput):
    browser.get('https://s5.zravian.com/')
    username = browser.find_element_by_id('name')
    username.send_keys(usernameinput)
    password = browser.find_element_by_id('pass')
    password.send_keys(passwordinput)
    login_botton = browser.find_element_by_css_selector('.grp input[type="submit"]')
    login_botton.click()