from ff_functions import (
    getQBData,
    getRushData,
    getRecData,
    getScoringData,
    getResults,
    getAggregateTopPlayers,
    read_pff,
    read_dict,
    soupInit,
)


def test_soup():
    assert soupInit("https://fantasydata.com/nfl/fantasy-football-leaders") is not None


def test_results():
    assert getResults("a", True, soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")) is not None


def test_getTopPlayers():
    soup = soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")
    assert getAggregateTopPlayers(getResults("a", True, soup)) is not None


def test_getQBData():
    assert getQBData(["QBR", "Int"]) is not None


def test_getRushData():
    assert getRushData(["Y/A", "Yds"]) is not None


def test_getRecData():
    assert getRecData(["Rec", "Yds"]) is not None


def test_getScoringData():
    assert getScoringData("WR") is not None


def test_pff_empty():
    assert len(read_pff()) != 0


def test_read_dict():
    assert len(read_dict()) != 0


# Integration tests
def integrationTest1():
    soup = soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")
    results = getResults("a", True, soup)
    ret = getAggregateTopPlayers(results)
    assert ret is not None
