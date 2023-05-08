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
    """
    Returns a BeautifulSoup object

    Parameters
    ----------
    URL : str
        The URL of the page desired to be queried

    Returns
    -------
    BeautifulSoup
        A BeautifulSoup object that queries the specified URL

    Examples
    --------
    >>> soupInit("bing.com")
    BeautifulSoup object

    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def getResults(label1, hrefBool, soup):
    """
    A results table of a soup query

    Parameters
    ----------
    label1 : str
        The label used to query the HTML result
    hrefBool : str
        Another label to query the desired results
    soup : BeautifulSoup
        The soup object to query the website

    Returns
    -------
    str[]
        A list of strings that depict the results queried

    Examples
    --------
    >>> getResults("ref", "hi", soup)
    str[] containing results of the website

    """
    results = soup.find_all(label1, href=hrefBool)
    return results


def getAggregateTopPlayers(results):
    """
    Returns the best NFL players for Fantasy regardless of position

    Parameters
    ----------
    results : str[]
        The results object that can be dissected for the players

    Returns
    -------
    str[]
        A list of the top players

    Examples
    --------
    >>> getAggregateTopPlayers(results)
    [Joe Burrow, Tom Brady, ...]

    """
    topPlayers = []
    for result in results:
        if "nfl/" in result.get("href") and "-fantasy/" in result.get("href"):
            x = result.text.split()
            name = x[0] + " " + x[1]
            topPlayers.append(name)
    return topPlayers


def read_pff():
    """
    Returns the results for the PFF website specifically

    Parameters
    ----------
    None

    Returns
    -------
    str[]
        A results list that contains players

    Examples
    --------
    >>> read_pff()
    [Joe Burrow, Tom Brady, ...]

    """
    URL = "https://www.pff.com/fantasy/stats"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", attrs={"class": "g-mb-4"})
    print(results.prettify())
    return results


def read_nextgen():
    """
    Returns the results for the nextGen website specifically

    Parameters
    ----------
    None

    Returns
    -------
    str[]
        A results list that contains players

    Examples
    --------
    >>> read_nextgen()
    [Joe Burrow, Tom Brady, ...]

    """
    URL = "https://nextgenstats.nfl.com/stats/top-plays/fastest-ball-carriers"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("main", attrs={"id": "main-content"})
    return results


def read_dict():
    """
    Returns a string of the keys in the website dict

    Parameters
    ----------
    None

    Returns
    -------
    str
        A concactenated string that contains all of the key values

    Examples
    --------
    >>> read_dict()
    "main container"

    """
    # for key in urlSearchDict.keys():
    #    parse_print(urlSearchDict.get(key)[0], urlSearchDict.get(key)[1])
    ret = ""
    for key in urlSearchDict.keys():
        ret += urlSearchDict.get(key)[0] + " "
    return ret


def getQBData(metrics):
    """
    Returns a DataFrame of the best QB's and their various stats, filtered and ordered on specific variables

    Parameters
    ----------
    String Array
        Metrics, a String Array of Metrics used to sort the dataframe, from the given statistics in the DF.

    Returns
    -------
    DataFrame
        A a DataFrame of the best QB's and their various stats, filtered and ordered on specific variables

    Examples
    --------
    >>> getQBData(["TD", "Cmp%"])
                    Player  Age   QBR   Cmp%   Yds  TD  Int
                    0    Patrick Mahomes*+   27  77.6   67.1  5250  41   12
                    4          Joe Burrow*   26  58.7   68.3  4475  35   12
                    6          Josh Allen*   26  71.4   63.3  4283  35   14
                    7          Geno Smith*   32  60.8   69.8  4282  30   11
                    3        Kirk Cousins*   34  49.9   65.9  4547  29   14
    >>> getQBData(["Int", "Age"])
                   Player  Age    QBR   Cmp%   Yds  TD  Int
                    19           Dak Prescott   29   57.9   66.2  2860  23   15
                    15            Davis Mills   24   33.1   61.0  3118  17   15
                    3           Kirk Cousins*   34   49.9   65.9  4547  29   14
                    13            Derek Carr*   31   55.5   60.8  3522  24   14
                    6             Josh Allen*   26   71.4   63.3  4283  35   14
    """
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
    for metric in metrics:
        if not hasattr(df, metric):
            print("Invalid Statistic Requested, Aborting")
            return None
    df.replace('', "0", inplace=True)
    df.fillna("0", inplace=True)
    df["Age"] = df["Age"].astype(int)
    df["QBR"] = df["QBR"].astype(float)
    df["Cmp%"] = df["Cmp%"].astype(float)
    df["Yds"] = df["Yds"].astype(int)
    df["TD"] = df["TD"].astype(int)
    df["Int"] = df["Int"].astype(int)
    dfFF = df.loc[:, ["Player", "Age", "QBR", "Cmp%", "Yds", "TD", "Int"]].sort_values(by=metrics, ascending=False)
    return dfFF


def getRushData(metrics):
    """
    Returns a DataFrame of the best RB's and their various stats, filtered and ordered on specific variables

    Parameters
    ----------
    String Array
        Metrics, a String Array of Metrics used to sort the dataframe, from the given statistics in the DF.

    Returns
    -------
    DataFrame
        A a DataFrame of the best RB's and their various stats, filtered and ordered on specific variables

    Examples
    --------
    >>> getRushData(["Yds", "Att"])
                Player   Tm  Age Pos   G  GS  Att   Yds  TD  1D Lng  Y/A   Y/G Fmb
                1    Josh Jacobs*+  LVR   24  RB  17  17  340  1653  12  93  86  4.9  97.2   3
                0  Derrick Henry *  TEN   28  RB  16  16  349  1538  13  65  56  4.4  96.1   6
                2      Nick Chubb*  CLE   27  RB  17  17  302  1525  12  69  41  5.0  89.7   1
                3  Saquon Barkley*  NYG   25  RB  16  16  295  1312  10  62  68  4.4  82.0   1
                7   Miles Sanders*  PHI   25  RB  17  15  259  1269  11  62  40  4.9  74.6   2
    >>> getRushData(["Att", "Y/A"])
                Player    Tm  Age   Pos   G    GS  Att   Yds  TD  1D  Lng  Y/A   Y/G  Fmb
                0   Derrick Henry*   TEN   28    RB  16    16  349  1538  13  65   56  4.4  96.1    6
                1   Josh Jacobs*+   LVR   24    RB  17    17  340  1653  12  93   86  4.9  97.2    3
                2   Nick Chubb*   CLE   27    RB  17    17  302  1525  12  69   41  5.0  89.7    1
                3   Saquon Barkley*   NYG   25    RB  16    16  295  1312  10  62   68  4.4  82.0    1
                4   Najee Harris   PIT   24    RB  17    17  272  1034   7  45   36  3.8  60.8    3
    """
    if len(metrics) == 0:
        print("No Metrics Given")
        return None
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
    for metric in metrics:
        if not hasattr(df, metric):
            print("Invalid Statistic Requested, Aborting")
            return None
    df.replace('', "0", inplace=True)
    df.fillna("0", inplace=True)
    df['Att'] = df['Att'].astype(int)
    df['G'] = df['G'].astype(int)
    df['Yds'] = df['Yds'].astype(int)
    df['TD'] = df['TD'].astype(int)
    df['Lng'] = df['Lng'].astype(int)
    df['Y/A'] = df['Y/A'].astype(float)
    df['Y/G'] = df['Y/G'].astype(float)
    df['Fmb'] = df['Fmb'].astype(int)
    df['1D'] = df['1D'].astype(int)
    dfFF = df.sort_values(by=metrics, ascending=False)
    return dfFF


def getRecData(metrics):
    """
    Returns a DataFrame of the best receivers and their various stats, filtered and ordered on specific variables

    Parameters
    ----------
    String Array
        Metrics, a String Array of Metrics used to sort the dataframe, from the given statistics in the DF.

    Returns
    -------
    DataFrame
        A a DataFrame of the best receivers (yes, that includes Travis Kelce) and
        their various stats, filtered and ordered on specific variables

    Examples
    --------
    >>> getRecData(["Tgt", "Rec"])
                Player Age Pos  Tgt  Rec   Yds  TD
                7   Davante Adams*+  30  WR  180  100  1516  14
                0     Tyreek Hill*+  28  WR  170  119  1710   7
                4      CeeDee Lamb*  23  WR  156  107  1359   9
                2     Stefon Diggs*  29  WR  154  108  1429  11
                14  Diontae Johnson  26  WR  147   86   882   0
    >>> getRecData(["TD", "Yds"])
                Player Age Pos  Tgt  Rec   Yds  TD
                7        Davante Adams*+  30  WR  180  100  1516  14
                11           A.J. Brown*  25  WR  145   88  1496  11
                2          Stefon Diggs*  29  WR  154  108  1429  11
                4           CeeDee Lamb*  23  WR  156  107  1359   9
                21          Amari Cooper  28  WR  132   78  1160   9

    """
    if len(metrics) == 0:
        print("No Metrics Given")
        return None
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

    for metric in metrics:
        if not hasattr(df, metric):
            print("Invalid Statistic Requested, Aborting")
            return None
    df.replace('', "0", inplace=True)
    df.fillna("0", inplace=True)
    df["Age"] = df["Age"].astype(int)
    df["Tgt"] = df["Tgt"].astype(int)
    df["Rec"] = df["Rec"].astype(int)
    df["Yds"] = df["Yds"].astype(int)
    df["TD"] = df["TD"].astype(int)

    dfFF = df.loc[:, ["Player", "Age", "Pos", "Tgt", "Rec", "Yds", "TD"]].sort_values(by=metrics, ascending=False)
    return dfFF


def getScoringData(pos):
    """
    Returns a DataFrame of the highest point scorers in the NFL, of RB, WR, and K, depending on the parameter given.

    Parameters
    ----------
    String
        Pos string, which determines which position to show the top scorers for

    Returns
    -------
    DataFrame
        a DataFrame of the highest point scorers in the NFL, of RB, WR, and K, depending on the parameter given.

    Examples
    --------
    >>> getScoringData("WR")
                Player Age Pos  Tgt  Rec   Yds  TD
                7   Davante Adams*+  30  WR  180  100  1516  14
                0     Tyreek Hill*+  28  WR  170  119  1710   7
                4      CeeDee Lamb*  23  WR  156  107  1359   9
                2     Stefon Diggs*  29  WR  154  108  1429  11
                14  Diontae Johnson  26  WR  147   86   882   0
    >>> getScoringData("QB")
                Player  RshTD  RecTD  TotalTD
                33         Jalen Hurts*     13      0       13
                67        Justin Fields      8      0        8
                70          Josh Allen*      7      0        7
                78         Daniel Jones      7      0        7
                112         Joe Burrow*      5      0        5

    """
    if pos != "WR" and pos != "RB" and pos != "QB" and pos != "K":
        print("Invalid Parameters, please use RB, WR, QB or K")
        return None
    page = requests.get("https://www.pro-football-reference.com/years/2022/scoring.htm")
    soup = BeautifulSoup(page.content, "html.parser")
    categories = soup.findAll('tr')[0]
    headers = categories.findAll('th')
    scoringCategories = []
    for header in headers:
        scoringCategories.append(header.getText())

    playerStats = soup.findAll('tr')[1:]
    compiled = []
    for i in range(1, len(playerStats)):
        stats = playerStats[i].findAll('td')
        arr = []
        for stat in stats:
            arr.append(stat.getText())
        compiled.append(arr)
    df = pd.DataFrame(compiled, columns=scoringCategories[1:])
    df = df.loc[df['Pos'] == pos]
    df.replace('', "0", inplace=True)
    df.fillna("0", inplace=True)
    df['RshTD'] = df["RshTD"].astype(int)
    df['RecTD'] = df["RecTD"].astype(int)
    df['TotalTD'] = df['RshTD'] + df['RecTD']
    dfFF = df.loc[:, ["Player", "RshTD", "RecTD", "TotalTD"]].sort_values(by=['TotalTD'], ascending=False)
    return dfFF


# print(getScoringData("RB"))
# print(getRecData(["TD", "Yds"]))
# print(getRushData(["Att", "Y/A"]))
print(getQBData(["TD", "Cmp%"]))
print(getQBData(["Int", "Age"]))
