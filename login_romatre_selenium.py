from selenium import webdriver
import os
import json

# Dict
# key = browser name and web driver's function
# value = path of the driver
driver = {}

# Copy the file into "driver" var
with open('web_browser_driver.json') as json_file:
    try:
        data = json.load(json_file)
        for row in data:
            driver[row] = data[row]
    except Exception as e:
        print("ERROR - Bad JSON syntax")
        print(e)

# Dict with the login informations. It should have, in order, username, password and submit button
# key = html input name
# value = value you want to enter in this input, or "submit" if this is a submit button
auth = {}

# Link of the web page, i hope
web_page_link = ""

# Title of the desired web page, just to check if you are entering the auth data into the correct page
web_page_title = ""

# Copy file information into variables
with open('login_page_data.json') as json_file:
    data = json.load(json_file)
    for row in data:
        if row == "website_link":
            web_page_link = data[row]
        elif row == "website_title":
            web_page_title = data[row]
        else:
            auth[row] = data[row]


# Check if the driver path is a valid file, even in case of multiple browser
def check_browser():
    for browser in driver:
        if os.path.isfile(driver[browser]):
            return browser
    print("ERROR - Check \"web_browser_driver.json\" file and select a correct absolute path")
    exit(1)


browser = check_browser()

# Insert in the path environment the selected driver
try:
    os.environ["PATH"] += os.pathsep + driver[browser]
except Exception as e:
    print("ERROR - Error with the driver path")
    print(e)
    exit(1)

# Open the browser and try to go to the selected web page
try:
    current_browser_name = getattr(webdriver, browser)
    current_browser = current_browser_name(driver[browser])
    current_browser.get(web_page_link)
except Exception as e:
    print("ERROR - Error with the browser")
    print(e)
    exit(1)

print(current_browser.title)
if current_browser.title == web_page_title:
    # Fill input fields (or at least he try to...) and close the browser
    try:
        for auth_row in auth:
            if auth[auth_row] == "submit":
                current_input = current_browser.find_element_by_name(auth_row)
                current_input.click()
                continue
            current_input = current_browser.find_element_by_name(auth_row)
            current_input.send_keys(auth[auth_row])
        current_browser.quit()
    except Exception as e:
        print("ERROR - Error with the inputs filling")
        print(e)
else:
    current_browser.quit()
