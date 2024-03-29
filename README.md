# fantasyfootball-crawler
This is an open source project that will help people access all the important statistics for fantasy football.
I want to create crawlers for both team and player statistics, and package them into neat dataframes.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![github issues](https://img.shields.io/github/issues/cocobird1/fantasyfootball-crawler)
[![Build Status](https://github.com/cocobird1/fantasyfootball-crawler/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/cocobird1/fantasyfootball-crawler/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/cocobird1/fantasyfootball-crawler/branch/main/graph/badge.svg)](https://codecov.io/gh/cocobird1/fantasyfootball-crawler)
[![PyPI](https://img.shields.io/pypi/v/fantasyfootball-crawler)](https://pypi.org/project/fantasyfootball-crawler/)
[![Documentation](https://img.shields.io/badge/GitHub%20Page-Link-brightgreen)](https://cocobird1.github.io/fantasyfootball-crawler/)
[![version](https://img.shields.io/badge/Release-v0.1.2-green)](https://cocobird1.github.io/fantasyfootball-crawler/)
# Overview
Fantasy football is a game played by many Americans, however most are uneducated when it comes to the various in-depth statistics that are needed to "level up" your team, and potentially win big. Most websites gloss over important statistics, or don't include all of the information needed (think FantasyPros), or perhaps include too much information (think pro-football-reference). I want to build a one-stop-shop for these important statistics.

The Fantasy-Football Crawler library can now accept specified user inputs for the top players, and sort through specific players based on specific data. Before, the library would use getQBData(), getRBData(), and getWRData() to simply return DataFrames ranked and sorted based on factors that I personally thought were the most relevant. However, now, users can use getQBData(metrics), getRushData(metrics), and getRecMetrics(metrics) to sort QBs, receivers, and runners based on specified parameters (ex. Yds, Att), and receiving and rushing are both not limited to one position, but include all rushers and receivers across the league (ex. Rushing Data can include QBs, RBs, and WRs even), which finally allows us to incorporate players like Travis Kelce into the receiving data.

Further, an aggregate scoring method was also implemented, where users can specify a position to get a DataFrame that holds the top positional players in terms of Rushing Touchdowns, Receiving Touchdowns, and Total Touchdowns, which can be very helpful in terms of fantasy.

This project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution

# How to Install Library
pip install fantasyfootball-crawler

# How to Use Library
Use the library by calling the functions that have been written in ff_functions, after importing them.

### Get QB Data

Users can call getQBData(metrics) with specified throwing metrics, to return a DataFrame that sorts based on the throwing metrics.

`metrics`: An array of strings that specify specific metrics to sort players by. Can be any combination of these strings: Player  Age   QBR   Cmp%   Yds  TD  Int

```python
from fantasyfootball-crawler import ff_functions as ffc

metrics = ["TD", "Cmp%"]
print(ffc.getQBData(metrics))
```
Output:
```python
Player  Age   QBR   Cmp%   Yds  TD  Int
0    Patrick Mahomes*+   27  77.6   67.1  5250  41   12
4          Joe Burrow*   26  58.7   68.3  4475  35   12
6          Josh Allen*   26  71.4   63.3  4283  35   14
7          Geno Smith*   32  60.8   69.8  4282  30   11
3        Kirk Cousins*   34  49.9   65.9  4547  29   14
```
### Get Rushing Data

Users can call getRushData(metrics) with specified rushing metrics, to return a DataFrame that sorts based on the rushing metrics.

`metrics`: An array of strings that specify specific metrics to sort players by. Can be any combination of these strings: Player   Tm  Age Pos   G  GS  Att   Yds  TD  1D Lng  Y/A   Y/G Fmb

```python
from fantasyfootball-crawler import ff_functions as ffc

metrics = ["Yds", "Att"]
print(ffc.getRushData(metrics))
```
Output: 
```python
Player   Tm  Age Pos   G  GS  Att   Yds  TD  1D Lng  Y/A   Y/G Fmb
1    Josh Jacobs*+  LVR   24  RB  17  17  340  1653  12  93  86  4.9  97.2   3
0  Derrick Henry *  TEN   28  RB  16  16  349  1538  13  65  56  4.4  96.1   6
2      Nick Chubb*  CLE   27  RB  17  17  302  1525  12  69  41  5.0  89.7   1
3  Saquon Barkley*  NYG   25  RB  16  16  295  1312  10  62  68  4.4  82.0   1
7   Miles Sanders*  PHI   25  RB  17  15  259  1269  11  62  40  4.9  74.6   2
 ```
            
### Get Receiving Data

Users can call getRecData(metrics) with specified receiving metrics, to return a DataFrame that sorts based on the receiving metrics.

`metrics`: An array of strings that specify specific metrics to sort players by. Can be any combination of these strings:  Player Age Pos  Tgt  Rec   Yds  TD

```python
from fantasyfootball-crawler import ff_functions as ffc

metrics = ["TD", "Yds"]
print(ffc.getRecData(metrics))
```
Output:
```python
Player Age Pos  Tgt  Rec   Yds  TD
7        Davante Adams*+  30  WR  180  100  1516  14
11           A.J. Brown*  25  WR  145   88  1496  11
2          Stefon Diggs*  29  WR  154  108  1429  11
4           CeeDee Lamb*  23  WR  156  107  1359   9
21          Amari Cooper  28  WR  132   78  1160   9
```

### Get Scoring Data

Users can call getScoringData(pos) with a specified position, to see the top touchdown scorers at each position: QB, RB, WR, and K (most K don't score TD's though)

`pos`: A string that indicates the position specified, can be "QB", "RB", "WR", or "K"
```python
from fantasyfootball-crawler import ff_functions as ffc
print(ffc.getScoringData("QB"))
```
Output:
```python
Player  RshTD  RecTD  TotalTD
33         Jalen Hurts*     13      0       13
67        Justin Fields      8      0        8
70          Josh Allen*      7      0        7
78         Daniel Jones      7      0        7
112         Joe Burrow*      5      0        5
```

### Weighted Rankings

Users can call weightedRankings(df, weights) with a specified DF, and sort them with the corresponding weights. For most people, they can call another function, like getQBData() for example, to get a DataFrame, and then input their desired weights.

'df': A DataFrame with the statistics and corresponding players
'weights': An integer array that is the same size as the number of columns in df

```python
df = getQBData(["TD"])
print(weightedRankings(df, [0.1, 0.4, 0.1, 0.3, 0.1 , 0.1, 0.1]))
```
Output:
```python
Player  Age   QBR   Cmp%   Yds  TD  Int  weighted
0    Patrick Mahomes*+   27  77.6   67.1  5250  41   12    568.99
8     Trevor Lawrence*   23  54.5   66.3  4113  25    8    516.09
7          Geno Smith*   32  60.8   69.8  4282  30   11    513.28
4          Joe Burrow*   26  58.7   68.3  4475  35   12    497.36
1       Justin Herbert   24  58.2   68.2  4739  25   10    488.96
```
