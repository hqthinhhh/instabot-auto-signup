import requests
from bs4 import BeautifulSoup
import time


def getFakeMail(driver):
    INST_CODE = 'https://www.disposablemail.com/'
    
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(INST_CODE)
    time.sleep(15)
    # req = requests.get(url)
    # soup = BeautifulSoup(req.content, "html.parser")
    # mail = soup.find_all("span", {"id": "email"})
    # mail = soup.find_all_previous("span",{"id":"email"})
    # mail = soup.get_text()
    # return mail[0].contents
    mail = driver.find_element_by_xpath("//span[@id='email']").text
    return mail

