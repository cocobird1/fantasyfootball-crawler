from ff_functions import (
    getQBData,
    getRushData,
    getRecData,
    getScoringData,
)


def test_getQBData1():
    assert getQBData(["QBR", "Int"]) is not None


def test_getQBData2():
    assert getQBData(["QBR", "Int", "Age"]) is not None


def test_getQBData3():
    assert getQBData([]) is None


def test_getQBData4():
    assert getQBData(["lol"]) is None


def test_getRushData1():
    assert getRushData(["Y/A", "Yds"]) is not None


def test_getRushData2():
    assert getRushData(["Y/A", "Yds", "Att", "G"]) is not None


def test_getRushData3():
    assert getRushData([]) is None


def test_getRushData4():
    assert getRushData(["lol"]) is None


def test_getRecData1():
    assert getRecData(["Rec", "Yds"]) is not None


def test_getRecData2():
    assert getRecData(["Rec", "Tgt", "TD"]) is not None


def test_getRecData3():
    assert getRecData([]) is None


def test_getRecData4():
    assert getRecData(["lol"]) is None


def test_getScoringData1():
    assert getScoringData("QB") is not None


def test_getScoringData2():
    assert getScoringData("RB") is not None


def test_getScoringData3():
    assert getScoringData("WR") is not None


def test_getScoringData4():
    assert getScoringData("K") is not None


def test_getScoringData5():
    assert getScoringData("pos") is None


def test_getScoringData6():
    assert getScoringData("") is None


# Integration tests
def integrationTest1():
    dfQB = getQBData(["QBR"])
    dfRush = getRushData(["Y/A"])
    dfRec = getRecData(["Rec"])
    assert dfQB is not None
    assert dfRush is not None
    assert dfRec is not None
