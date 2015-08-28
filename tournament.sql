-- Table for player (id, name)
CREATE TABLE players ( name TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL PRIMARY KEY);

-- Table for matches between players (winner, losser)
CREATE TABLE games ( playerWin SERIAL references players(id),
                     playerLose SERIAL references players(id),
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL PRIMARY KEY);

-- View to access to results of palyers
CREATE VIEW players_standings AS
        SELECT
            players.id AS id,
            players.name AS name,
            wins.wonGames AS wins,
            SUM( wins.wonGames + defeats.numberGames ) AS defeats
        FROM
            players,
            (
                SELECT players.id, COUNT(games.playerWin) AS wonGames
                FROM players
                LEFT OUTER JOIN games ON games.playerWin = players.id
                GROUP BY players.id
            ) AS wins,
            (
                SELECT players.id, COUNT(games.playerLose) AS numberGames
                FROM players
                LEFT OUTER JOIN games ON games.playerLose = players.id
                GROUP BY players.id
            ) AS defeats
        WHERE
            wins.id = players.id AND defeats.id = players.id
        GROUP BY 
            players.id,
            players.name,
            wins.wonGames,
            defeats.numberGames
        ORDER BY
            wins.wonGames DESC
        ;