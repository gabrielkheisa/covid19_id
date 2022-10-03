import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import base64

from selenium.webdriver.chrome.options import Options

while(1):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('CHROMEDRIVER_PATH', chrome_options=options) 

    browser.delete_all_cookies()
    browser.get("https://kawalcovid19.id/")

    time.sleep(5)


    terkonfirmasi = browser.find_element_by_class_name("kcov-zqe2y4-Text").get_attribute('textContent')
    perawatan = browser.find_element_by_class_name("kcov-6173qq-Text").get_attribute('textContent')
    sembuh = browser.find_element_by_class_name("kcov-kmc3ux-Text").get_attribute('textContent')
    meninggal = browser.find_element_by_class_name("kcov-1alrthh-Text").get_attribute('textContent')
    last_update = browser.find_element_by_class_name("kcov-s88wow-Text").get_attribute('textContent')

    payload = terkonfirmasi + "," + perawatan + "," + sembuh + "," + meninggal + "," + last_update + "," + dt_string + " GMT+7"

    print(payload)

    payload_encoded = base64.b64encode(bytes(payload, 'ascii'))

    print(payload_encoded.decode('ascii'))

    response = requests.get('YOUR_URL'+str(payload_encoded.decode('ascii')))

    browser.quit()
    print("Sleep for 300 seconds")
    time.sleep(5*60)
