def choose_Fields(browser, usernameinput, passwordinput, emailinput):
    username = browser.find_element_by_id('name')
    username.send_keys(usernameinput)
    password = browser.find_element_by_id('pw1')
    password.send_keys(passwordinput)
    passagian = browser.find_element_by_id('pw2')
    passagian.send_keys(passwordinput)
    email = browser.find_element_by_id('mail')
    email.send_keys(emailinput)
    emailagain = browser.find_element_by_id('mail2')
    emailagain.send_keys(emailinput)

def choose_Tribe(browser, tribeinput):
    tribe = browser.find_elements_by_class_name('tribe')

    if tribeinput.upper() == 'Roman'.upper():
        for x in tribe:
           if x.text.upper() == 'Roman'.upper():
               x.click()

    if tribeinput.upper() == 'Teuton'.upper():
        for x in tribe:
           if x.text.upper() == 'Teuton'.upper():
               x.click()

    if tribeinput.upper() == 'Gaul'.upper():
        for x in tribe:
           if x.text.upper() == 'Gaul'.upper():
               x.click()

def choose_Location(browser, locationinput):
    location = browser.find_elements_by_class_name('loc')

    if locationinput.upper() == '-+'.upper():
        for x in location:
           if x.text.upper() == '-|+'.upper():
               x.click()

    if locationinput.upper() == '++'.upper():
        for x in location:
           if x.text.upper() == '+|+'.upper():
               x.click()

    if locationinput.upper() == '--'.upper():
        for x in location:
           if x.text.upper() == '-|-'.upper():
               x.click()

    if locationinput.upper() == '+-'.upper():
        for x in location:
           if x.text.upper() == '+|-'.upper():
               x.click()

def choose_Referrer(browser,refferinput):
    refferer = browser.find_element_by_id('ref')
    refferer.send_keys(refferinput)

def submit(browser):
    check = browser.find_element_by_id('chk')
    check.click()

    continue_botton = browser.find_element_by_css_selector('.grp input[type="submit"]')
    continue_botton.click()

def register(browser, usernameinput, passwordinput, emailinput, tribeinput, locationinput, refferinput=''):
    browser.get('https://s5.zravian.com/register.php')
    choose_Fields(browser, usernameinput, passwordinput, emailinput)
    choose_Location(browser, locationinput)
    choose_Tribe(browser, tribeinput)
    choose_Referrer(browser, refferinput)
    submit(browser)
