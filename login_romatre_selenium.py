from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os
import json
import logging
import PySimpleGUI as sg

# current_file_path = os.getcwd()
current_file_path = os.path.realpath(__file__)
current_file_path = current_file_path[:current_file_path.rfind(os.path.sep)]

# log
log_file_name = "login_romatre_log.log"
log_file_path = current_file_path + os.path.sep + log_file_name

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO,
                    filename=log_file_path, filemode="w")

# Dict
# key = browser name, same used in web driver's function
# value = absolute path of the driver
driver = {}

web_browser_driver_json_file_name = "web_browser_driver.json"
web_browser_driver_json_path = current_file_path + os.path.sep + web_browser_driver_json_file_name
logging.info("Web browser driver JSON file in \"" + web_browser_driver_json_path + "\"")

login_page_data_file_name = "login_page_data.json"
login_page_data_path = current_file_path + os.path.sep + login_page_data_file_name
login_page_data_number_expected_items = 7
logging.info("Login page JSON file in \"" + login_page_data_path + "\"")

# Dict with the login information. It should have information about username, password and submit button
# key = html input name
# value = value you want to enter in this input, or "submit" if this is a submit button
auth = {}

# Link of the web page, i hope
web_page_link = ""

# Title of the desired web page, just to check if you are entering the auth data into the correct page
web_page_title = ""

# Copy the file into "driver" var
with open(web_browser_driver_json_path) as json_file:
    try:
        data = json.load(json_file)
        for row in data:
            driver[row] = data[row]
        logging.info("File \"" + web_browser_driver_json_file_name + "\" read correctly")
    except Exception as e:
        logging.error("Bad JSON syntax in \"" + web_browser_driver_json_file_name + "\"")
        logging.error(e)
        exit(1)

# Copy file information into variables
with open(login_page_data_path) as json_file:
    try:
        data = json.load(json_file)
        if len(data) != login_page_data_number_expected_items:
            logging.error("Check JSON file \"" + login_page_data_file_name + "\", it should have " +
                          str(login_page_data_number_expected_items) + " items")
            exit(1)
        for row in data:
            if row == "website_link":
                if data[row] == "":
                    logging.error("No Web Site link in \"" + login_page_data_file_name + "\"")
                    exit(1)
                web_page_link = data[row]
            elif row == "website_title":
                if data[row] == "":
                    logging.error("No Web Site title in \"" + login_page_data_file_name + "\"")
                    exit(1)
                web_page_title = data[row]
            else:
                if row != "password_value" and data[row] == "":
                    logging.error("No \"" + row + "\" value in \"" + login_page_data_file_name + "\"")
                    exit(1)
                auth[row] = data[row]
        logging.info("File \"" + login_page_data_file_name + "\" read correctly")
    except Exception as e:
        logging.error("Bad JSON syntax in \"" + login_page_data_file_name + "\"")
        logging.error(e)
        exit(1)


# Check if the driver path is a valid file, even in case of multiple browser
def get_correct_browser():
    for browser in driver:
        if os.path.isfile(driver[browser]):
            logging.info("You choose \"" + browser + "\" browser")
            return browser
    logging.error("\"" + web_browser_driver_json_file_name + "\" doesn't contain a correct absolute path")
    exit(1)


browser = get_correct_browser()

# Insert in the path environment the selected driver
try:
    os.environ["PATH"] += os.pathsep + driver[browser]
    logging.info("Added path env correctly: \"" + driver[browser] + "\"")
except Exception as e:
    logging.error("Driver path can't be added in the env path")
    logging.error(e)
    exit(1)


def is_native_headless(current_browser):
    native_headless_browser = ["PhantomJS"]
    return current_browser in native_headless_browser


# Open the browser and try to go to the selected web page
try:
    current_browser_name = getattr(webdriver, browser)
    if is_native_headless(browser):
        current_browser = current_browser_name(executable_path=driver[browser])
    else:
        current_browser_options = globals()[browser + "Options"]()
        current_browser_options.headless = True
        logging.info("Browser " + browser + " set to headless")
        current_browser = current_browser_name(executable_path=driver[browser], options=current_browser_options)
    logging.info(browser + " opened correctly")
    current_browser.get(web_page_link)
    logging.info(browser + " is trying to open " + web_page_link)
except Exception as e:
    logging.error("Problems with the browser " + browser)
    logging.error(e)
    exit(1)

print(current_browser.title)


def password_with_gui():
    layout = [[sg.Text('Enter the password')],
              [sg.InputText(key='_Password_', password_char="*")],
              [sg.Submit(button_text="Submit")]]

    window = sg.Window("Loginner for RomaTre's network", layout)

    event, values = window.Read()
    window.Close()

    text_input = values['_Password_']
    return text_input


if current_browser.title == web_page_title:
    logging.info("You're in the login page")
    # Fill input fields (or at least he try to...) and close the browser
    try:
        username_input = current_browser.find_element_by_name(auth["username_tag_name"])
        username_input.send_keys(auth["username_value"])
        logging.info("Username entered correctly")

        if auth["password_value"] == "":
            logging.info("Getting password from GUI")
            current_password_value = password_with_gui()
        else:
            logging.info("Getting password from " + login_page_data_file_name)
            current_password_value = auth["password_value"]
        password_input = current_browser.find_element_by_name(auth["password_tag_name"])
        password_input.send_keys(current_password_value)
        logging.info("Password entered correctly")

        submit_button_input = current_browser.find_element_by_name(auth["submit_tag_name"])
        submit_button_input.click()
        logging.info("Submit button clicked correctly")

        if current_browser.title != web_page_title:
            current_browser.quit()
            logging.info("Now you're logged!")
            logging.info("Quitted browser")
        else:
            logging.error("Wrong username or password. Please check them")
            current_browser.quit()
            exit(2)
    except Exception as e:
        logging.error("Problems during inputs filling")
        logging.error(e)
        current_browser.quit()
        logging.info("Quitted browser")
else:
    logging.info("Nice, you don't need to log in!")
    current_browser.quit()
    logging.info("Quitted browser")
