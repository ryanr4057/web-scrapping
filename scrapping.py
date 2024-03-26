from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options

import time

def scroll_to(driver, element):
    ActionChains(driver)\
            .scroll_to_element(element)\
            .perform()

def acessa_pista(i):
    pistas = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-eventid='cards_meetings_click']")))
    try:
        time.sleep(1)
        scroll_to(driver, pistas[i])
        wait.until(EC.element_to_be_clickable(pistas[i]))
        pistas[i].click()
    except ElementClickInterceptedException:
        scroll_to(driver, pistas[i])
        pistas[i].click()
    races = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-eventid='cards_card']")))
    print(driver.find_element(By.ID, "meetingHeaderTitle").text)
    print(len(races))
    driver.back()

options = Options()
options.add_argument('--headless')
options.add_argument("--incognito")
options.add_argument("--nogpu")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,1280")
options.add_argument("--no-sandbox")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)
driver.maximize_window()
driver.get("https://greyhoundbet.racingpost.com/#meeting-list/r_date=2024-03-26")


# driver.execute_script('''
#     var style = document.createElement('style');
#     style.innerHTML = '*, *::before, *::after { animation-play-state: paused !important; }';
#     document.head.appendChild(style);
# ''')
# wait.until(EC.invisibility_of_element_located((By.ID, "webAppLanding")))

pista = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-eventid='cards_meetings_click']")))

for i in range(len(pista)):
    try:
        acessa_pista(i)
    except StaleElementReferenceException:
        acessa_pista(i)

    
