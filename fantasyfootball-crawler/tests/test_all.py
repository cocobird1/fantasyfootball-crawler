from unittest.mock import patch
from ff_functions import *

def test_ffl_empipty():
    assert len(getTopPlayers()) != 0

def test_pff_empty():
    assert len(read_pff()) != 0

def test_next_gen():
    assert len(read_nextgen()) != 0

def test_dict():
    assert len(get_Dict()) != 0

def test_read_dict():
    assert len(read_dict()) != 0
    

