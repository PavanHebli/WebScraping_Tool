from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument("--headless=new") # for Chrome >= 109
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works


def GetHTML(url, headless=True, className=None, explicit=10):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=ChromeHeadless(headless))
    driver.implicitly_wait(10)
    driver.get(url)

    # wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    if className:
        try:
            # myElem = WebDriverWait(driver, explicit).until(EC.presence_of_element_located((By.CLASS_NAME, className)))
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print ("Page is ready!")
        except TimeoutException:
            print( "Loading took too much time!")
    html = driver.page_source
    driver.quit()
    return html

def ChromeHeadless(headless):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new") # for Chrome >= 109
        # chrome_options.add_argument("--headless")
        # chrome_options.headless = True # also works
    return chrome_options