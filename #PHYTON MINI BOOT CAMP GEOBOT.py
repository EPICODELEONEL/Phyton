#PHYTON MINI BOOT CAMP GEOBOT
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickabale
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import panda as pd


def wait_and_get(by, el):
    return wait.until(element_to_be_clickable(
        (by, el)))


options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_driver = ChromeDriverManager().install()
driver = Chrome(service=Service(chrome_driver), options=options)
wait = WebBDriverWait(driver, 10)





driver.maximize_windows()
driver.get('https://www.google.it/maps/place/Westminster')
# non accetare il cookies e trovare elemento html tasto dx espeziona
#  aria label
wait_and_get(By.CSS_SELECTOR, '[aria-label="Reject all"]').click()
# click direction tasto destro ispeziona data value direction
wait_and_get(By.CSS_SELECTOR, '[data-value="Direction"]').click()
# prendere aria label
wait_and_get(By.CSS_SELECTOR, '[aria-label="Driving"]').click()
#la tab driving  e stata attivata dal nostro bot
# dataframe csv con cui ce la citta e duration

#importiamo il file csv
# e leggere

df = pd.read_csv('cities.csv',index_col=0)
#print(df.index)
for city in df.index:
    print(city)
    searchbox_div = wait_and_get(
        By.CSS_SELECTOR, '[id="directions-searchbox-0"]')
    searchbox_input=searchbox_div.find_element(By.TAG_NAME, 'input')
    searchbox_input.clear()
    searchbox_input.send_keys(f'{city}, London, UK' + Keys.ENTER)
    sleep(1)

    duration_span = wait_and_get(
        By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')
    
    duration = duration_span.text
    print(city, duration)

    minutes = pd.Timedelta(duration).total_seconds() / 60

    df.loc[city, 'DURATION'] =  minutes
    
    df.to_csv('duration.csv')