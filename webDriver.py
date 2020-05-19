from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def initializeChromWebDriver():
    # Using Chrome to access web - Driver URL depending on your saved file
    driver = webdriver.Chrome('D:\\ETORO\\Prerequesites\\chromedriver')
    return driver


def logIn(driver):
    # Open the website
    driver.get('https://www.etoro.com/login')

    # Selects the id box - USERNAME
    id_box = driver.find_element_by_name('username')

    # Sends id information
    id_box.send_keys('$$$$$')

    time.sleep(5)

    # Finds password box
    pass_box = driver.find_element_by_name('password')
    # Sends password
    pass_box.send_keys('$$$$')

    time.sleep(5)
    # Finds login button
    login_button = driver.find_element_by_tag_name('button')
    # Click login
    login_button.click()
    time.sleep(5)


def goToStats(driver):
    # Goes to Interested Stock Stats
    driver.get('https://www.etoro.com/markets/tsla/stats')


def returnValue(driver):

    tslCurrentValue = driver.find_element_by_css_selector(
        'span.head-info-stats-value')

    print("Tesla Current Value: " + str(tslCurrentValue.text))


def returnPercentage(driver):
    # Gets todays percentage and value difference from openning
    tslTodayPercentage = driver.find_element_by_css_selector(
        'span.head-info-stats-change')

    # Separates WebElement by Quantity & Percentage
    tdyPtgChunks = tslTodayPercentage.text.split(' ')

    # Prints separated values ready to use for further learning functions
    print("Tesla's Today Price Difference: " + str(tdyPtgChunks[0]))
    print("Tesla's Today Percentage Difference: " + str(tdyPtgChunks[1]))


driver = initializeChromWebDriver()
goToStats(driver)
returnValue(driver)
returnPercentage(driver)
