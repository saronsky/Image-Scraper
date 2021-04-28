"""Requires Selenium"""
from selenium import webdriver

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument("--incognito")
#CHROME_OPTIONS.add_argument("--headless")
COUNT = 0
MAX_VOTES = 2


# Change value in ADD_LINK_HERE (whatever your survey link is)
# Change value in TEXT_YOU_WANT_TO_TARGET for forms with radio button inputs.

while COUNT < MAX_VOTES:
    driver = webdriver.Chrome(chrome_options=CHROME_OPTIONS)
    driver.get('https://www.surveymonkey.com/r/VLG755T')
    driver.find_element_by_xpath('//*[@id="646663622_4248634139"]').click()
    driver.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button').click()
    COUNT+=1
    print(COUNT,"submissions")
    driver.close()
