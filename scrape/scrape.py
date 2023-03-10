import json
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


columns = ["World Rank", "University name", "Overall Score", "International Research Network",
           "H-Index citations", "Citations per paper", "Academic reputation", "Employer Reputation"]


# Create an instance of Chrome
driver = webdriver.Chrome()
# wait for 10 seconds for the page to load
driver.implicitly_wait(50)

# Navigate to a website
driver.get('https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/natural-sciences')


# Find and interact with an element on the page
XPATH = '//div[@class="ranking_tabs quik-tabs"]//ul//li[2]'

# Wait for the element to appear
wait = WebDriverWait(driver, 50)
element: WebElement = wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))
# print(element.get_attribute('outerHTML'))
# print(element.is_displayed(), element.is_enabled())

driver.execute_script("arguments[0].click();", element)  # Working



element: WebElement = wait.until(EC.presence_of_element_located((By.ID, 'ranking-data-load_ind')))



def change_perpagedata():
    # perpagedata dropdown
    element_: WebElement = wait.until(EC.presence_of_element_located((By.ID, 'perpagedata')))
    element: WebElement = element_.find_element(By.XPATH, "..")
    # print(element.get_attribute("outerHTML"))
    driver.execute_script("arguments[0].click();", element)  # Working

    # select 100
    element: WebElement = element_.find_element(By.XPATH, '..//div[4]')
    # print(element.get_attribute("outerHTML"))
    element.click()  # Working
    # driver.execute_script("arguments[0].click();", element)  # Working


def change_page():
    # next page button
    XPATH = '//ul[@id="alt-style-pagination"]//li//a[@class="page-link next"]'
    element: WebElement = wait.until(EC.presence_of_element_located((By.XPATH, XPATH)))
    # print(element_.get_attribute("outerHTML"))
    # element.click()  # Not working
    driver.execute_script("arguments[0].click();", element)  # Working


def get_data():
    # data
    CSS_SELECTOR_RANK = 'div#ranking-data-load_ind div._univ-rank'
    ranks: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_RANK)))

    CSS_SELECTOR_UNI = 'div#ranking-data-load_ind a.uni-link'
    universities: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_UNI)))

    CSS_SELECTOR_COUNTRY = 'div#ranking-data-load_ind div.location'
    location: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_COUNTRY)))

    CSS_SELECTOR_OS = 'div#ranking-data-load_ind div.overall-score-span-ind.overall div.td-wrap-in'
    os: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_OS)))

    CSS_SELECTOR_IRN = 'div#ranking-data-load_ind div.overall-score-span-ind.ind_15 div.td-wrap-in'
    irn: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_IRN)))

    CSS_SELECTOR_HC = 'div#ranking-data-load_ind div.overall-score-span-ind.ind_69 div.td-wrap-in'
    hc: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_HC)))

    CSS_SELECTOR_CPP = 'div#ranking-data-load_ind div.overall-score-span-ind.ind_70 div.td-wrap-in'
    cpp: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_CPP)))

    CSS_SELECTOR_AR = 'div#ranking-data-load_ind div.overall-score-span-ind.ind_76 div.td-wrap-in'
    ar: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_AR)))

    CSS_SELECTOR_ER = 'div#ranking-data-load_ind div.overall-score-span-ind.ind_77 div.td-wrap-in'
    er: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_ER)))

    return zip(
        map(lambda x: x.text, ranks),
        map(lambda x: x.text, universities),
        map(lambda x: x.text, location),
        map(lambda x: x.text, os),
        map(lambda x: x.text, irn),
        map(lambda x: x.text, hc),
        map(lambda x: x.text, cpp),
        map(lambda x: x.text, ar),
        map(lambda x: x.text, er),
    )


all_elements = []
page_no = 51

for indx in range(page_no):
    while(True):
        try:
            all_elements.extend(get_data())
            
        except Exception as e:
            print(e)
            continue
        
        else:
            print(len(all_elements))
            if indx != page_no - 1:
                change_page()
                sleep(1) 
            break

def format_scrappy_data(data: list[tuple]):
    return [
        {
            "World Rank": a,
            "University name": b,
            "Location": c,
            "Overall Score": d,
            "International Research Network": e,
            "H-Index citations": f,
            "Citations per paper": g,
            "Academic reputation": h,
            "Employer Reputation": i,
        } for a, b, c, d, e, f, g, h, i in data
    ]


# print formatted data using json to a file

with open('data.json', 'w') as f:
    json.dump(format_scrappy_data(all_elements), f, indent=2)


# pause for 10 seconds
sleep(10)

# # Close the browser
# driver.quit()
