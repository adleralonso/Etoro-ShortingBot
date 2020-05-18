from selenium import webdriver
# Using Chrome to access web
driver = webdriver.Chrome('D:\ETORO\Prerequesites\chromedriver')
# Open the website
driver.get('https://www.etoro.com/login')


# Select the id box - USERNAME
id_box = driver.find_element_by_name('username')
# Send id information
id_box.send_keys('$$$$$')


# Find password box
pass_box = driver.find_element_by_name('password')
# Send password
pass_box.send_keys('$$$$')

# Find login button
login_button = driver.find_element_by_tag_name('button')
# Click login
login_button.click()
