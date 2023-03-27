from bs4 import BeautifulSoup
import pandas as pd
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


def getAggregateTopPlayers(results):
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
        ret += urlSearchDict.get(key)[0]
    return ret


def getQBData():
    page = requests.get("https://www.pro-football-reference.com/years/2022/passing.htm")
    soup = BeautifulSoup(page.content, "html.parser")
    categories = soup.findAll('tr')[0]
    headers = categories.findAll('th')
    passingCategories = []
    for header in headers:
        passingCategories.append(header.getText())

    playerStats = soup.findAll('tr')[1:]
    compiled = []
    for i in range(len(playerStats)):
        stats = playerStats[i].findAll('td')
        arr = []
        for stat in stats:
            arr.append(stat.getText())
        compiled.append(arr)

    df = pd.DataFrame(compiled, columns=passingCategories[1:])
    newCols = df.columns.values
    newCols[-6] = "YardsLostFromSack"
    df.columns = newCols
    df['TD'].fillna(value="0", inplace=True)
    df['TD'] = df["TD"].astype(int)
    dfFF = df.loc[:, ["Player", "Age", "QBR", "Cmp%", "Yds", "TD", "Int"]].sort_values(by=["TD"], ascending=False)
    print(dfFF.head())
    return dfFF


def getRBData():
    page = requests.get("https://www.pro-football-reference.com/years/2022/rushing.htm")
    soup = BeautifulSoup(page.content, "html.parser")
    categories = soup.findAll('tr')[1]
    headers = categories.findAll('th')
    rushingCategories = []
    for header in headers:
        rushingCategories.append(header.getText())

    playerStats = soup.findAll('tr')[1:]
    compiled = []
    for i in range(1, len(playerStats)):
        stats = playerStats[i].findAll('td')
        arr = []
        for stat in stats:
            arr.append(stat.getText())
        compiled.append(arr)

    df = pd.DataFrame(compiled, columns=rushingCategories[1:])
    df[df.columns.values[2]].fillna(value="0", inplace=True)
    df[df.columns.values[2]] = df[df.columns.values[2]].astype(int)
    df['Yds'].fillna(value="0", inplace=True)
    df['Yds'] = df["Yds"].astype(int)
    df['Att'].fillna(value="0", inplace=True)
    df['Att'] = df["Att"].astype(int)
    dfFF = df.sort_values(by=["Yds", "Att"], ascending=False)
    print(dfFF.head())


def getWRData():
    page = requests.get("https://www.pro-football-reference.com/years/2022/receiving.htm")
    soup = BeautifulSoup(page.content, "html.parser")
    categories = soup.findAll('tr')[0]
    headers = categories.findAll('th')
    receivingCategories = []
    for header in headers:
        receivingCategories.append(header.getText())

    playerStats = soup.findAll('tr')[1:]
    compiled = []
    for i in range(1, len(playerStats)):
        stats = playerStats[i].findAll('td')
        arr = []
        for stat in stats:
            arr.append(stat.getText())
        compiled.append(arr)
    df = pd.DataFrame(compiled, columns=receivingCategories[1:])
    df = df.loc[df['Pos'] == 'WR']
    df['Tgt'].fillna(value="0", inplace=True)
    df['Tgt'] = df["Tgt"].astype(int)
    df['Rec'].fillna(value="0", inplace=True)
    df['Rec'] = df["Rec"].astype(int)
    df['Yds'].fillna(value="0", inplace=True)
    df['Yds'] = df["Yds"].astype(int)
    dfFF = df.loc[:, ["Player", "Age", "Pos", "Tgt", "Rec", "Yds", "TD"]].sort_values(
        by=['Tgt', 'Rec', 'Yds'], ascending=False
    )
    print(dfFF.head())


def get_Dict():
    return len(urlSearchDict)


getQBData()
getRBData()
getWRData()
