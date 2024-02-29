# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# allows us to locate elements in an HTML file
from selenium.webdriver.common.by import By

# for colorful output
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

# instantiate the driver in 'browser'
browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# access the desired webpage using the browser instance
browser.get("https://dotprs.nyc/")

# seek 'START' button
while True:
    try:
        start_button = browser.find_element(By.XPATH, value="//input[@value='START']")
        prGreen("START button found!")
        break
    except:
        prRed("START button not found, refreshing page...")
        browser.refresh()

# start button found
start_button.click()

# seek desired garage and click it
# garages available:
# Borough Hall Municipal Parking Garage
# Staten Island Courthouse
# Court Square Garage
# Bay Ridge Garage
# Jerome and 190th Street
# East 149th Street
# Delancy and Essex Street
garage = browser.find_element(By.XPATH, value="//span[text()='GARAGE NAME HERE']")
garage.click()
prGreen("Successfully selected garage...\n")

# seek 'NEXT' button and click it
next_button = browser.find_element(By.XPATH, value="//input[@value='Next >']")
next_button.click()

# fill out form fields
prGreen("Filling out form fields...\n")
first_name = browser.find_element(By.ID, "edit-field-first-name-und-0-value")
first_name.send_keys("FIRST NAME HERE")

last_name = browser.find_element(By.ID, "edit-title")
last_name.send_keys("LAST NAME HERE")

phone_number = browser.find_element(By.ID, "edit-field-phone-number-und-0-value")
phone_number.send_keys("MOBILE # HERE")

email_address = browser.find_element(By.ID, "edit-field-email-address-und-0-email")
email_address.send_keys("EMAIL HERE")

address = browser.find_element(By.ID, "edit-field-address-und-0-value")
address.send_keys("ADDRESS HERE")

zipcode = browser.find_element(By.ID, "edit-field-zipcode-und-0-value")
zipcode.send_keys("ZIPCODE HERE")

dmv_client_id = browser.find_element(By.ID, "edit-field-dmv-number-und-0-value")
dmv_client_id.send_keys("DMV CLIENT ID HERE")

# once all fields have been filled, click the 'SUBMIT' button
prGreen("Submitting reservation request...\n")
submit_button = browser.find_element(By.XPATH, value="//button[text()='Submit Reservation Request']")
browser.execute_script("arguments[0].click();", submit_button)
# submit_button.click() -> causes ElementClickInterceptedException

# check that we reach the confirmation page
if browser.title == "Reservation Confirm | DOT Parking":
    prGreen("Reservation success!")
else:
    prRed("Reservation failure!")