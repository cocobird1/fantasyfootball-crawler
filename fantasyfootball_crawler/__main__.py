from .ff_functions import soupInit, getResults, getTopPlayers

if __name__ == "__main__":
    soup = soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")
    results = getResults("a", True, soup)
    getTopPlayers(results)
