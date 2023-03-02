import bs4 as bs
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import requests


urlSearchDict = {
    "pff" : ["https://www.pff.com/fantasy/stats", 'main'],
    #"fantasyData" : ["https://fantasydata.com/nfl/fantasy-football-leaders", 'container'],
    #"pfr" : ["https://www.pro-football-reference.com/years/2022/advanced.htm", 'container'],
    #"nextGen" : ["https://nextgenstats.nfl.com/stats/top-plays/fastest-ball-carriers", 'container'],
    #"analyst" : ["https://theanalyst.com/na/2021/09/nfl-stats-zone/", 'container']
}

def read_ffl():
    URL = "https://fantasydata.com/nfl/fantasy-football-leaders"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", attrs={"class" : "stats-grid-container"})
    print(results.prettify())
    return results

def read_pff():
    URL = "https://www.pff.com/fantasy/stats"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", attrs={"class" : "main"})
    print(results.prettify())
    return results

def read_nextgen():
    URL = "https://nextgenstats.nfl.com/stats/top-plays/fastest-ball-carriers"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", attrs={"id" : "stats-top-plays-view"})
    print(results.prettify())
    return results

def read_dict():
    #for key in urlSearchDict.keys():
    #    parse_print(urlSearchDict.get(key)[0], urlSearchDict.get(key)[1])
    ret = ""
    for key in urlSearchDict.keys():
        URL = urlSearchDict.get(key)[0]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id=urlSearchDict.get(key)[1])
        print(results.prettify())
        ret = ret + results
    return ret

def get_Dict():
    return urlSearchDict

read_ffl()