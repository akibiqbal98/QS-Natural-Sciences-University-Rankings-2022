# 2022 QS World University Rankings by Subject Natural Sciences


## Problem Statement
The goal of this project is to gather information of top 500 universities rank, name, academic reputation, h-index citation, citation per paper by the subject: Natural Science [this website](https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/natural-sciences#university-rankings-indicators). <br/> 
Later we utilized the scraped data to understand the following demographics and correlations using Tableau Dashboard: 

1. A barchart International Research Network higher than 80 
2. Scatter plot of Employer and Academic reputation. 
3. Barchart of H-Index citations for each university, sorted by country
4. Map of H-Index citations of European countries.

You can visit the public dashboard [here](https://public.tableau.com/app/profile/md.akib.iqbal.majumder/viz/WorldUniversitydemographyofNaturalSciencesSubject/Dashboard1). 

## Findings and Observations from the [Dashboard](https://public.tableau.com/app/profile/md.akib.iqbal.majumder/viz/WorldUniversitydemographyofNaturalSciencesSubject/Dashboard1)
1. Université Paris Cité has perfect score in International Research Network. 
2. Princtone university and Stanford university has the most average academic reputation and citation per paper. 
3. All the top 5 rank universities has the most Academic and Employer reputation.
4. The ranking was done most probably using Overall score.


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
python selenium_scraper/scrape.py --chromedriver_path <path_to_chromedriver>
```


