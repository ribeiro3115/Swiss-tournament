# This file has the responsability to connect with the databse

import psycopg2

# Function to connect with the database
def connect():
	return psycopg2.connect("dbname=tournament")

# Registe Player
def registerPlayer(name):
	DB = connect()
	c = DB.cursor()
	c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
	DB.commit()
	DB.close

# Delete All games
def deleteMatches():
	DB = connect()
	c = DB.cursor()
	c.execute("DELETE FROM games")
	DB.commit()
	DB.close

# Delete all players
def deletePlayers():
	DB = connect()
	c = DB.cursor()
	c.execute("DELETE FROM players")
	DB.commit()
	DB.close

# Count numbers of players
def countPlayers():
	DB = connect()
	c = DB.cursor()
	c.execute("SELECT * FROM players")
	players = c.fetchall()
	DB.close
	return len(players)

#  Returns a list of the players and their win records, sorted by wins
def playerStandings():
	DB = connect()
	c = DB.cursor()
	c.execute("SELECT * From players_standings")
	playersStandings = c.fetchall()
	DB.close
	return playersStandings

# Records the outcome of a single match between two players.
def reportMatch(winner, loser):
	DB = connect()
	c = DB.cursor()
	c.execute("INSERT INTO games (playerWin,playerLose) VALUES (%s,%s)", (winner,loser,))
	DB.commit()
	DB.close


# Returns a list of pairs of players for the next round of a match.
def swissPairings():

	standings = playerStandings();

	playerNumbers = len(standings);

	pairings = [];

	if playerNumbers % 2 == 0 and playerNumbers > 2:
		for i in xrange(0,playerNumbers,2):
			player = i;

			pair = i+1;

			pairings.append( 
                    [ 
                        standings[player][0], standings[player][1], 
                        standings[pair][0], standings[pair][1] 
                    ] 
                )


	return pairings
