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

# look for the 'START' button
while True:
    try:
        start_button = browser.find_element(By.XPATH, value="//input[@value='START']")
        break
    except:
        browser.refresh()

# start button found
start_button.click()

# look for the desired garage and click it
garage = browser.find_element(By.XPATH, value="//span[text()='Borough Hall Municipal Parking Garage']")
prGreen("Found garage!\n")
garage.click()
prGreen("Successfully selected garage...\n")


# look for the 'NEXT' button and click it
next_button = browser.find_element(By.XPATH, value="//input[@value='Next >']")
next_button.click()
prGreen("Succesfully clicked NEXT >...\n")

# fill out form fields
prGreen("Filling out form fields...\n")
first_name = browser.find_element(By.ID, "edit-field-first-name-und-0-value")
first_name.send_keys("Luis")

last_name = browser.find_element(By.ID, "edit-title")
last_name.send_keys("Morales")

phone_number = browser.find_element(By.ID, "edit-field-phone-number-und-0-value")
phone_number.send_keys("3479304167")

email_address = browser.find_element(By.ID, "edit-field-email-address-und-0-email")
email_address.send_keys("0317guadalupe@gmail.com")

address = browser.find_element(By.ID, "edit-field-address-und-0-value")
address.send_keys("6 W 190TH ST APT C")

zipcode = browser.find_element(By.ID, "edit-field-zipcode-und-0-value")
zipcode.send_keys("10468")

dmv_client_id = browser.find_element(By.ID, "edit-field-dmv-number-und-0-value")
dmv_client_id.send_keys("000000000")

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
