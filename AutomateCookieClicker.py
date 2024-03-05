#This is my tutorial
# First we make some of the observations.
# Click the button with class big cookie and span with class price.



# My code for automating the cookieClicker is done and iam very much satisfied with the results.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
path = "chromedriver.exe"
service = Service(path = path)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")
print("Waiting for clicking")
WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "cc_btn"))
)
print("Available for printing")
first_click = driver.find_element(By.CLASS_NAME, "cc_btn")
first_click.click()
print("Waiting for langSelect-EN")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
print("Available for clicking")
second_click = driver.find_element(By.ID, "langSelect-EN")
second_click.click()
while True:
    print("Finding the presence of the main clickable cookie")
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.ID, "bigCookie"))
    )
    print("BigCookie found and unlocked finding")
    WebDriverWait(driver, 40).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))
    )
    print("Available for printing")
    click = driver.find_element(By.ID, "bigCookie")
    click.click()
    click2 = driver.find_element(By.ID, "product0")
    click3 = driver.find_element(By.ID, "product1")
    comp1 = driver.find_element(By.ID, "productOwned0")
    comp2 = driver.find_element(By.ID, "productOwned1")
    # comp = driver.find_element(By.ID, "productOwned1")
    if comp1.text!="5":
        click2.click()
    elif comp2.text!="5":
        click3.click()
    print(comp1.text)
    # click2.click()
time.sleep(10)
driver.quit()