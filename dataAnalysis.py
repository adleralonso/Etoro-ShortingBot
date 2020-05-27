import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import datetime
import winsound


def fileName():
    currentDT = datetime.datetime.now()
    return(str(currentDT.month) + "-"+str(currentDT.day) + "-" +
           str(currentDT.year)+"-"+str(currentDT.hour)+"_"+str(currentDT.minute)+"-min-max.csv")


def dataAnalisis(fileName, categoria):
    df = pd.read_csv(fileName)

    media = df[str(categoria)].mean()
    mediana = df[str(categoria)].median()
    moda = df[str(categoria)].mode()
    print(categoria)
    print("""
        Media: %d
        Mediana: %d
        Moda: %d
        ---------------------------
    """ % (media, mediana, moda))


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
    companyStatsURL = 'https://www.etoro.com/markets/' + \
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


def sellSound():
    frequency = 1500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def buySound():
    frequency = 500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    time.sleep(.5)
    winsound.Beep(frequency, duration)


def advice(currentMin, currentMax, currentValue, minDifference):
    # Corrects minDifference Rule on 80/20 based on the difference between currentMax and currentMin
    if minDifference < currentMax - currentMin:
        minDifference = currentMax - currentMin
    print("Min Difference: " + str(minDifference))

    # Sell Buy - Recomendation Based on MinMax difference of 20 or more
    if float(currentMax) - 4 > float(currentMin) and float(minDifference*.2) + float(currentMin) >= float(currentValue):
        advice = "You Should Buy"
        buySound()
    elif float(currentMax) - 4 > float(currentMin) and float(minDifference*.8) + (currentMin) <= float(currentValue):
        advice = "You should Sell"
        sellSound()
    else:
        advice = "Wait champion"

    print(advice)
    return minDifference, advice


def basicRoutine(driver, companyName, repetitions, currentDifference):
    # Initialize Driver and Company Name for current Routine
    driver = driver
    companyName = companyName
    currentMin = -34
    currentMax = 2.5
    currentDifference = currentDifference
    currentAdvice = ""

    goToStats(driver, companyName)

    with open(str(companyName+"-"+fileName()), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Value", "Range", "Percentage", "Min", "Max", "Advice"])

        # Repeats the getting stats values operations
        for x in range(repetitions):
            time.sleep(5)
            print("Iteration: " + str(x))
            tempRow = []
            tempRow.append(returnValue(driver, companyName))
            parcialRow = returnPercentage(driver, companyName)
            tempRow.append(parcialRow[0])

            if currentMin > float(parcialRow[0]):
                currentMin = float(parcialRow[0])
            if currentMax < float(parcialRow[0]):
                currentMax = float(parcialRow[0])
            tempRow.append(parcialRow[1])

            print("Current Min: " + str(currentMin))
            print("Current Max: " + str(currentMax))

            tempRow.append(currentMin)
            tempRow.append(currentMax)

            # tempRow.append(returnGeneralView(driver, companyName))
            currentDifference, currentAdvice = advice(
                currentMin, currentMax, parcialRow[0], currentDifference)

            tempRow.append(currentAdvice)
            writer.writerow(tempRow)
            print("-----------------------------")


driver = initializeChromWebDriver()
# driver.get('https://www.etoro.com/login')
# driver.get('https://www.etoro.com/markets/tsla/stats')
# time.sleep(10)
# invest(driver)
# basicRoutine(driver, "tsla", 10000)

basicRoutine(driver, "tsla", 10000, 3)
