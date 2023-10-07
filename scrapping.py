from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

def acessa_pista(i):
    pistas = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-eventid='cards_meetings_click']")))
    try:
        time.sleep(1)
        wait.until(EC.element_to_be_clickable(pistas[i]))
        pistas[i].click()
    except ElementClickInterceptedException:
        pistas[i].click()
    races = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-eventid='cards_card']")))
    print(driver.find_element(By.ID, "meetingHeaderTitle").text)
    print(len(races))
    driver.back()
    
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
driver.maximize_window()
driver.get("https://greyhoundbet.racingpost.com/#meeting-list/r_date=2023-10-07")

driver.execute_script('''
    var style = document.createElement('style');
    style.innerHTML = '*, *::before, *::after { animation-play-state: paused !important; }';
    document.head.appendChild(style);
''')

for i in range(0,5):
    pyautogui.hotkey('ctrl','-')

pista = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-eventid='cards_meetings_click']")))

for i in range(len(pista)):
    try:
        acessa_pista(i)
    except StaleElementReferenceException:
        acessa_pista(i)

    
