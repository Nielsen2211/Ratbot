from selenium.common.exceptions import NoSuchElementException
import time

def upgradefield(browser, link):
    try:
        browser.get(link)
        browser.find_element_by_css_selector('#build #contract a.build').click()
        return True
    except NoSuchElementException:
        return False

def fields_upg_all(browser, upgradefields):
    fields_container = browser.find_elements_by_css_selector('#content map#rx area')
    href = []

    for _ in range(0,upgradefields):
        for x in fields_container:
            if 'build.php' in x.get_attribute('href'):
                href.append(x.get_attribute('href'))

    for link in href:
        could_upgrade = upgradefield(browser, link)
        while could_upgrade == False:
            time.sleep(5)
            could_upgrade = upgradefield(browser, link)

def fields_scan(browser, upgradefields):
    browser.get('https://s5.zravian.com/village1.php')
    fields_upg_all(browser, upgradefields)