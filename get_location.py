USERNAME = ""
PASSWORD = ""
from selenium.webdriver.common.by import By
import time
import datetime
import undetected_chromedriver as uc

file = open('current_location_.tsv', 'w')
file.close()
file = open('location_history.tsv', 'w')
driver = uc.Chrome()

while datetime.datetime.now() < datetime.datetime(2024, 7, 28):
    current_time = datetime.datetime.now().time()
    while True:
        try:
            url = 'https://www.google.com/android/find/?device=1&rs=1'
            driver.get(url)
            time.sleep(2)
            
            inputElement = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
            inputElement.send_keys(USERNAME)
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/c-wiz/div/div[3]/div/div/div/div/button").click()
            time.sleep(5)
            
            inputElement = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
            inputElement.send_keys(PASSWORD)
            time.sleep(5)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button').click()
            time.sleep(5)
            
            driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div[2]/button').click()
            time.sleep(2)
            
            TIME = datetime.datetime.now()
            TIME = TIME.strftime('%Y/%m/%d %H:%M:%S')
            page = driver.page_source
            HEADER = 'https://www.google.com/maps/@'
            map = page.split(HEADER)[1].split('"')[0]
            LAT, LONG, ZOOM = map.split(',')
            location = 'https://www.google.com/maps/place/' + ','.join([LAT, LONG])
            
            print(TIME, location)
            file = open('current_location.tsv', 'w')
            file.write('\t'.join([TIME, location]) + '\n')
            file.close()
            
            file = open('location_history.tsv', 'a')
            file.write('\t'.join([TIME, location]) + '\n')
            file.close()
            
            break
        except:
            time.sleep(1)
    
    time.sleep(850)
