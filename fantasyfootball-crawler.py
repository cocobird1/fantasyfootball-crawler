import bs4 as bs
import pandas as pd

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
    pff : ["https://www.pff.com/fantasy/stats", 'kyber-table-body___rows'],
    fantasyData : ["https://fantasydata.com/nfl/fantasy-football-leaders", 'stats_grid'],
    pfr : ["https://www.pro-football-reference.com/years/2022/advanced.htm", 'tbody'],
    nextGen : ["https://nextgenstats.nfl.com/stats/top-plays/fastest-ball-carriers", 'el-table__body-wrapper'],
    analyst : ["https://theanalyst.com/na/2021/09/nfl-stats-zone/", 'colgroup']
}

for key in urlSearchDict.keys():
    parse_print(urlSearchDict.get(key)[0], urlSearchDict.get(key)[1])




