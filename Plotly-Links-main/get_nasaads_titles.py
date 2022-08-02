# @author: Evan Anthopoulos

# This program searches the NASA ADS database for the titles of the papers 
# that discovered a pulsar for a given survey based on the Surveys.xlsx file
# and returns the given titles for each survey in an individual file.
# Note: Would run much faster if done in one txt file, but is also more difficult to extract data from
# Note: Does not matter what search engine you normally use, the program will run either way
    
import selenium.webdriver as webdriver # pip install selenium anywhere in terminal
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver_manager anywhere in terminal
# from selenium.webdriver.support.ui import WebDriverWait # Use if latency issue occurs, such as missing letters in title
import pandas as pd

# Function that prints a list of titles to a txt file
def get_title(url_list):
    sel_url_list = url_list # passing a list of URLs makes the process go much faster because Chrome does not have to close and re-open every time.
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Installs if first time. Else, just runs the program.
    for sel_url in sel_url_list:
        browser.get(sel_url)
        title = browser.title
        title = title.strip(' - NASA/ADS')
        title = title.strip('.')
        print(str(sel_url) + '~' + str(title))
        print(str(sel_url) + '~' + str(title), file = txt_file)



# Main function - Set Variables, Declare Stuff
survey_file = 'Surveys.xlsx'
xl = pd.read_excel(survey_file, header=None)

survey_col = 0
survey_name_col = 1
xl_survey_list = xl.iloc[:,survey_col]
xl_survey_name_list = xl.iloc[:,survey_name_col]

survey_title = []
url =''

for i in range(len(xl_survey_list)):
    url_list = [] # Inside loop to reset list each iteration
    survey = str(xl_survey_list[i]).strip()
    survey_title.append(xl_survey_list[i])
    txt_file = open(survey + 'link_titles.txt', 'w+') # No need to manually delete files that have no links / titles because survey_htmls.py does not output them. In fact, it is necessary to keep them.
    survey_row = xl.iloc[i,3:]
    for link in survey_row:
        if str(link) != 'nan':
            url = str(link)
            url_list.append(url)
    sel_title_list = get_title(url_list)
    txt_file.close()

















