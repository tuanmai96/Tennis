from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import timedelta, datetime
today = datetime.now()
reservation_date = 22

while True:
    #login
    with webdriver.Chrome(ChromeDriverManager().install()) as driver:
        tennis_name = "159363"
        tennis_pass = "vietnam9"
        try:
            driver.get('https://www.cogesport.com/club/0020/0020.fwx?opt=1&lang=EN')


            driver.find_element(By.NAME,"Cusager").send_keys(tennis_name)
            driver.find_element(By.NAME,"Mdp").send_keys(tennis_pass)

        #navigating to reservation table
            driver.find_element(By.XPATH,'/html/body/center/form[1]/table/tbody/tr[4]/td/center/input').click()
            driver.find_element(By.NAME,'msrvh.fwx').click()
            driver.find_element(By.XPATH,'/html/body/form[3]/table[3]/tbody/tr/td/input').click()


        #Checking in the reservation table if its reservation day
            website_date = driver.find_element(By.XPATH,'html/body/form[3]/form/table[2]/tbody/tr[20]/td[9]/center').text
            print(website_date)


            # expected_reservation_date = today + timedelta(days=8)
            day_to_reserve = str(reservation_date)
        #if = continue with the code, else = stop code and rerun after certain amount of time
            if day_to_reserve in website_date:
                select = Select(driver.find_element(By.NAME,'Minutes'))
                select.select_by_value('120')
                #check if timeslot for court is available
                if len(driver.find_elements(By.XPATH,'/html/body/form[3]/form/table[2]/tbody/tr[34]/td[9]/center/input')) == 0:
                    continue

                # below xpath is the correct one
                driver.find_element(By.XPATH, '/html/body/form[3]/form/table[2]/tbody/tr[34]/td[9]/center/input').click()
                # below is test xpath
                # driver.find_element(By.XPATH, '/html/body/form[3]/form/table[2]/tbody/tr[24]/td[6]/center/input').click()

                found_court = False
                courts = ['PREF-4','PREF-5','PREF-11','PREF-12','PREF-13','PREF-14','PREF-15']
                for x in courts:
                    #1. check in list which court is available
                    #2. click on available court
                    #3. continue with reservation code
                    if len(driver.find_elements(By.NAME, x)) != 0:
                        driver.find_element(By.NAME, x).click()
                        found_court = True
                        break

                if not found_court:
                    time.sleep(2)
                    continue

                select = Select(driver.find_element(By.NAME, 'Part1'))
                select.select_by_visible_text('LY, DANNY')
                driver.find_element(By.XPATH, '/html/body/form[4]/table[4]/tbody/tr/td/input').click()
                driver.find_element(By.XPATH, '/html/body/form[4]/table/tbody/tr[2]/td/input').click()
                print('You got a court!')
                break

            else:
                #interval between runs
                time.sleep(5)

        except:
            continue



