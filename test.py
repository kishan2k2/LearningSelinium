from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
Path = "chromedriver.exe"
service = Service(path = Path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com/")
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Who is kishan payadi", Keys.ENTER)
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Kishan"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Kishan")
link.click()
time.sleep(10)
driver.quit()