# Fantasy Football Project

## Table of Contents

## Origin of Data

League Data
- Origin: https://www.pro-football-reference.com/years/{year}/fantasy.htm#fantasy. 
- Contents: season-level data on passing, rushing, and receiving; fantasy points in different formats; games played; position; and age.
- Years Included: 1970 to 2023
- Location: data/league

Advanced Player Stats
- Origin: https://www.pro-football-reference.com/{last_name_initial}/{pro-football-ref_player_id}.htm
- Contents: season-by-season stats for individual players, links to pages with game-level data 
    - WARNING: as of 2024-11-22, trying to retreive the game log pages results in a 502 Bad Gateway error
- Years Included: 1970 to Present
- Location: data/players/pro-football-reference_player_pages 

Player Physical Information
- Origin: https://www.pro-football-reference.com/{last_name_initial}/{pro-football-ref_player_id}.htm
- Contents: height, weight
- Alternative source: https://www.nfl.com/players

Player Injury Reports:
- Origin: https://www.nfl.com/injuries/ 
- Years Included: 2009 - Present
- NOTE: injury reports are high-level; that is, an injury report will report an ankle injury but won't specify what type

ESPN Player IDs
- Origin: https://sports.core.api.espn.com/v3/sports/football/nfl/athletes?limit=20000


