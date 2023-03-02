import bs4 as bs
from bs4 import BeautifulSoup
import pandas as pd
import requests

# To make this generalized across all websites, there is a searchTerm 
# associated with the HTML wrappers of the website.
def get_tables(url, searchTerm):
    soup = bs.BeautifulSoup(url, 'lxml')
    table = soup.find_all(searchTerm) 
    dataframe = pd.read_html(str(searchTerm))
    return dataframe

# This function gets the dataframe from a given table.
def read_tables(table, index):
    df = pd.read_html(str(table))[index]
    return df

# This function parses a URL, searchTerm (HTML wrapper), and prints the dataframe contents.
def parse_print(url, searchTerm):
    df = get_tables(url, searchTerm)
    for i in range(len(df)):
        curTable = read_tables(df, i)
        for j in range(len(curTable)):
            print(curTable[j])

# A dictionary containing the URL and search term, with the names as keys.
urlSearchDict = {
    "pff" : ["https://www.pff.com/fantasy/stats", 'main'],
    #"fantasyData" : ["https://fantasydata.com/nfl/fantasy-football-leaders", 'container'],
    #"pfr" : ["https://www.pro-football-reference.com/years/2022/advanced.htm", 'container'],
    #"nextGen" : ["https://nextgenstats.nfl.com/stats/top-plays/fastest-ball-carriers", 'container'],
    #"analyst" : ["https://theanalyst.com/na/2021/09/nfl-stats-zone/", 'container']
}

#for key in urlSearchDict.keys():
#    parse_print(urlSearchDict.get(key)[0], urlSearchDict.get(key)[1])
for key in urlSearchDict.keys():
    URL = urlSearchDict.get(key)[0]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id=urlSearchDict.get(key)[1])
    print(results.prettify())

URL = "https://fantasydata.com/nfl/fantasy-football-leaders"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", attrs={"class" : "stats-grid-container"})
print(results.prettify())

