from bs4 import BeautifulSoup
import requests


urlSearchDict = {
    "pff": ["https://www.pff.com/fantasy/stats", 'main'],
    # "fantasyData" : ["https://fantasydata.com/nfl/fantasy-football-leaders", 'container'],
    # "pfr" : ["https://www.pro-football-reference.com/years/2022/advanced.htm", 'container'],
    # "nextGen" : ["https://nextgenstats.nfl.com/stats/top-plays/fastest-ball-carriers", 'container'],
    # "analyst" : ["https://theanalyst.com/na/2021/09/nfl-stats-zone/", 'container']
}


def soupInit(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def getResults(label1, hrefBool, soup):
    results = soup.find_all(label1, href=hrefBool)
    return results


def getTopPlayers(results):
    topPlayers = []
    for result in results:
        if "nfl/" in result.get("href") and "-fantasy/" in result.get("href"):
            x = result.text.split()
            name = x[0] + " " + x[1]
            topPlayers.append(name)
    return topPlayers


def read_pff():
    URL = "https://www.pff.com/fantasy/stats"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", attrs={"class": "g-mb-4"})
    print(results.prettify())
    return results


def read_nextgen():
    URL = "https://nextgenstats.nfl.com/stats/top-plays/fastest-ball-carriers"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("main", attrs={"id": "main-content"})
    return results


def read_dict():
    # for key in urlSearchDict.keys():
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
    return len(urlSearchDict)
