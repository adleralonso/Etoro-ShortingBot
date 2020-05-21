from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


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
    pass_box.send_keys('$$$$$')

    time.sleep(5)
    # Finds login button
    login_button = driver.find_element_by_tag_name('button')
    # Click login
    login_button.click()
    time.sleep(5)


def goToStats(driver, companyName):
    # Goes to Interested Stock Stats
    companyStatsURL = 'https://www.etoro.com/v' + \
        str(companyName) + '/stats'
    driver.get(companyStatsURL)


def invest(driver):
    time.sleep(5)
    # Finds login button
    login_button = driver.find_element_by_css_selector(
        'span.ng-binding')
    time.sleep(5)
    # Click login
    login_button.click()
    print("Invest Button Clicked")


def returnValue(driver, companyName):

    companyCurrentValue = driver.find_element_by_css_selector(
        'span.head-info-stats-value')

    print(companyName + "'s Current Value: " + str(companyCurrentValue.text))
    return str(companyCurrentValue.text)


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

    return tdyPtgChunks


def returnGeneralView(driver, companyName):
    companyGeneralView = driver.find_element_by_css_selector(
        'et-card-content.market-stats-wrapper')

    print(companyName + "'s General View: \n" + str(companyGeneralView.text))
    return str(companyGeneralView.text)


def basicRoutine(driver, companyName, repetitions):
    # Initialize Driver and Company Name for current Routine
    driver = driver
    companyName = companyName

    goToStats(driver, companyName)

    with open('firsthourtsl.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Value", "Range", "Percentage", "Stats"])

        # Repeats the getting stats values operations
        for x in range(repetitions):
            time.sleep(5)
            print("Iteration: " + str(x))
            tempRow = []
            tempRow.append(returnValue(driver, companyName))

            parcialRow = returnPercentage(driver, companyName)
            tempRow.append(parcialRow[0])
            tempRow.append(parcialRow[1])
            tempRow.append(returnGeneralView(driver, companyName))
            writer.writerow(tempRow)

            print("-----------------------------")


driver = initializeChromWebDriver()
driver.get('https://www.etoro.com/login')
time.sleep(60)
driver.get('https://www.etoro.com/markets/tsla/stats')
time.sleep(10)
invest(driver)
#basicRoutine(driver, "tsla", 10000)

# basicRoutine(driver, "btc", 10000)
