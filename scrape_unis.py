import json
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

columns = ["University name", "Overall Score", "International Research Network",
           "H-Index citations", "Citations per paper", "Academic reputation", "Employer Reputation"]


# Create an instance of Chrome
driver = webdriver.Chrome()
# wait for 10 seconds for the page to load
driver.implicitly_wait(50)

XPATH = '//div[@class="ranking_tabs quik-tabs"]//ul//li'

driver.get('https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/natural-sciences')

# Find all the university elements on the page
# university_elements = driver.find_elements_by_css_selector('.university')

def change_page():
    #next page link
    CSS_SELECTOR_UNI = 'div#ranking-data-load_ind a.uni-link'
    universities: list[WebElement] = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SELECTOR_UNI)))


    # Iterate over the university elements
    for university_element in university_elements:
    # Find the link element and extract the link URL
    link_element = university_element.find_element_by_css_selector('.university-link')
    link_url = link_element.get_attribute('href')

    # Navigate to the university's website
    driver.get(link_url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Find the GRE score element and extract the score
    gre_score_element = driver.find_element_by_css_selector('.gre-score')
    gre_score = gre_score_element.text

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
