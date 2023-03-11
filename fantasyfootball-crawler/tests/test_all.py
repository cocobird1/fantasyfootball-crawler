from ff_functions import getResults, getTopPlayers, read_pff, read_nextgen, get_Dict, read_dict, soupInit


def test_soup():
    assert soupInit("https://fantasydata.com/nfl/fantasy-football-leaders") is not None


def test_results():
    assert getResults("a", True, soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")) is not None


def test_getTopPlayers():
    soup = soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")
    assert getTopPlayers(getResults("a", True, soup)) is not None


def test_pff_empty():
    assert len(read_pff()) != 0


def test_dict():
    assert get_Dict() != 0


def test_read_dict():
    assert len(read_dict()) != 0


# Integration tests
def integrationTest1():
    soup = soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")
    results = getResults("a", True, soup)
    ret = getTopPlayers(results)
    assert ret is not None
