#Swiss tournament

### What is?

This is a Swiss tournament to results is an PostgreSQL database. ets you see the list of matches for next round.

### How it works?

To run this app you need to run the terminal as follows:
```sh
$ cd /vagrant/tournament
$ psql
$ CREATE DATABASE tournament
$ \c tournament
$ \i tournament.sql
```

Usage:
```sh
# Registe Player
registerPlayer('Player Name')

# Delete all players
deletePlayers():

# Records the outcome of a single match between two players.
reportMatch(winnerID, loserID)

# Delete All games
def deleteMatches()

#  Returns a list of the players and their win records, sorted by wins
playerStandings()

# Returns a list of pairs of players for the next round of a match.
swissPairings()
```
### Version
1.0.0

### Tech

Dillinger uses a number of open source projects to work properly:

* [Python] - HTML enhanced for web apps!
* [PostgreSQL] - Databse in SQL

License
----

The MIT License (MIT)

Copyright (c) 2015 Movie Trailer Website

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


[Python]:https://www.python.org/
[PostgreSQL]:http://www.postgresql.org/