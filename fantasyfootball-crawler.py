import bs4 as bs
import pandas as pd

def get_tables(url):
    soup = bs.BeautifulSoup(url, 'lxml')
    # mostly all of the statistics sites are built on <table_wrapper> tags, so this will retrieve them
    table = soup.find_all('table') 
    dataframe = pd.read_html(str(table))
    return dataframe

def read_tables(table, index):
    df = pd.read_html(str(table))[index]
    return df

# this is a generalized parsing function, but I will make specific ones for each site because each has different format
def parse(url):
    df = get_tables(url)
    for i in range(len(df)):
        curTable = read_tables(df, i)
        for j in range(len(curTable)):
            print(curTable[j])

urlList = ["https://www.pro-football-reference.com/years/2022/advanced.htm", 
"https://fantasydata.com/nfl/fantasy-football-leaders", "https://www.pff.com/fantasy/stats", 
"https://nextgenstats.nfl.com/", "https://theanalyst.com/na/2021/09/nfl-stats-zone/"]

for i in range(len(urlList)):
    parse(urlList[i])




