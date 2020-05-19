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


def goToStats(driver, companyName):
    # Goes to Interested Stock Stats
    companyStatsURL = 'https://www.etoro.com/markets/' + \
        str(companyName) + '/stats'
    driver.get(companyStatsURL)


def returnValue(driver, companyName):

    companyCurrentValue = driver.find_element_by_css_selector(
        'span.head-info-stats-value')

    print(companyName + "'s Current Value: " + str(companyCurrentValue.text))


def returnPercentage(driver, companyName):
    # Gets todays percentage and value difference from openning
    companyTodayPercentage = driver.find_element_by_css_selector(
        'span.head-info-stats-change')

    # Separates WebElement by Quantity & Percentage
    tdyPtgChunks = companyTodayPercentage.text.split(' ')

    # Prints separated values ready to use for further learning functions
    print(companyName + "'s Today Price Difference: " + str(tdyPtgChunks[0]))
    print(companyName + "'s Today Percentage Difference: " +
          str(tdyPtgChunks[1]))


def returnGeneralView(driver, companyName):
    companyGeneralView = driver.find_element_by_css_selector('div.col')

    print(companyName + "'s General View: \n" + str(companyGeneralView.text))


def basicRoutine(driver, companyName, repetitions):
    # Initialize Driver and Company Name for current Routine
    driver = driver
    companyName = companyName

    goToStats(driver, companyName)

    # Repeats the getting stats values operations
    for x in range(repetitions):
        time.sleep(3)
        print("Iteration: " + str(x))
        returnValue(driver, companyName)
        returnPercentage(driver, companyName)
        returnGeneralView(driver, companyName)
        print("-----------------------------")
        time.sleep(2)


driver = initializeChromWebDriver()

basicRoutine(driver, "tsla", 1)

basicRoutine(driver, "btc", 10)
