from unittest.mock import patch
from ff_functions import *

# Unit tests
def test_soup():
    assert soupInit("https://fantasydata.com/nfl/fantasy-football-leaders") != None

def test_results():
    assert getResults("a", True, soup) != None

def test_getTopPlayers():
    assert getTopPlayers(results) !=  None

def test_pff_empty():
    assert len(read_pff()) != 0

def test_next_gen():
    assert len(read_nextgen()) != 0

def test_dict():
    assert len(get_Dict()) != 0

def test_read_dict():
    assert len(read_dict()) != 0

# Integration tests
def integrationTest1():
    soup = soupInit("https://fantasydata.com/nfl/fantasy-football-leaders")
    results = getResults("a", True, soup)
    ret = getTopPlayers(results)
    assert ret != None