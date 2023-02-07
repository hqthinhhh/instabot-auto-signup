from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import time
import argparse

# parser = argparse.ArgumentParser()

# args = parser.parse_args()
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)

#replace 'your path here' with your chrome binary absolute path
driver = webdriver.Chrome('/Users/admin/Desktop/python/Driver selenium/chromedriver')
# driver = webdriver.Firefox(executable_path="/Users/admin/Desktop/python/Driver selenium/geckodriver")
# driver = webdriver.Safari()


#saves the login & pass into accounts.txt file.
acc = open("accounts.txt", "a")

driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(5)
try:
    cookie = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Only allow essential cookies')]"))).click()
except:
    pass
name = account.username()
#Fill the email value
email_field = driver.find_element_by_name('emailOrPhone')
fake_email = email.getFakeMail(driver)
driver.switch_to.window(driver.window_handles[0])
print(fake_email)
email_field.send_keys(fake_email)
print(fake_email)

# Fill the fullname value
fullname_field = driver.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())

# Fill username value
username_field = driver.find_element_by_name('username')
username_field.send_keys(name)
print(name)

# Fill password value
password_field = driver.find_element_by_name('password')
acc_password = account.generatePassword()
password_field.send_keys(acc_password) # You can determine another password here.
print(acc_password)

print(name+":"+acc_password, file=acc)

acc.close()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Sign up']"))).click()

time.sleep(8)

#Birthday verificationdriver.find_element_by_xpath("//select[@title='Month:']").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@title='March']"))).click()

driver.find_element_by_xpath("//select[@title='Day:']").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@title='3']"))).click()

driver.find_element_by_xpath("//select[@title='Year:']").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[@title='1969']"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Next']"))).click()
time.sleep(3)
#
# fMail = fake_email[0].split("@")
# mailName = fMail[0]
# domain = fMail[1]
instCode = verifiCode.getInstVeriCode(driver)
print(instCode)
driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(10)

#accepting the notifications.
# driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
# time.sleep(2)

#logout
# driver.find_element_by_xpath(
# "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
# driver.find_element_by_xpath(
# "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div").click()

# try:
# not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
# if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
# time.sleep(10)
# instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
# confInput = driver.find_element_by_name('email_confirmation_code')
# confInput.send_keys(Keys.CONTROL + "a")
# confInput.send_keys(Keys.DELETE)
# confInput.send_keys(instCodeNew, Keys.ENTER)
# except:
# pass


time.sleep(6)
driver.quit()