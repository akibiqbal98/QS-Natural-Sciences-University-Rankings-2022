# 2022 QS World University Rankings by Subject Natural Sciences


## Problem Statement
The goal of this project is to gather information of top 500 universities rank, name, academic reputation, h-index citation, citation per paper by the subject: Natural Science [this website](https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/natural-sciences#university-rankings-indicators). <br/> 
Later we utilized the scraped data to understand the following demographics and correlations using Tableau Dashboard: 

1. Scatter plot of Employer and Academic reputation. 
2. H-Index  for each university, sorted by country.
3. Total Students of each Universities. 
4. Average GMAT, GRE, GPA of each Country. 

You can visit the public dashboard [here](https://public.tableau.com/app/profile/md.akib.iqbal.majumder/viz/WorldUniversitydemographyofNaturalSciencesSubject/Dashboard1). 

## Findings and Observations from the [Dashboard](https://public.tableau.com/app/profile/md.akib.iqbal.majumder/viz/WorldUniversitydemographyofNaturalSciencesSubject/Dashboard1)
1. All the top 5 rank universities has the most Academic and Employer reputation.
2. University of sydney and University of Toronto has more than 30000 international student.
3. USA and New Zeland has the most average GMAT, GPA, GRE.
4. The ranking of the universities was done most probably using Overall score.


## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
git clone https://github.com/akibiqbal98/QS-World-University-Rankings-by-Subject-2022-Natural-Sciences
```
2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads 
5. Run the scraper
```bash
python uni_info_scrape.py --chromedriver_path <path_to_chromedriver>
```


