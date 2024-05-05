# https://github.com/swar/nba_api
from datetime import timezone
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static import teams
from nba_api.stats.static import players
import pandas as pd
from dateutil import parser
from nba_api.live.nba.endpoints import boxscore


# ######################################################
def get_teams():

    teams_dict = teams.get_teams()
    df_teams = pd.DataFrame(teams_dict)
    print(df_teams)

    return df_teams


# ######################################################
def get_data(df_all_players, player_id):

    career = playercareerstats.PlayerCareerStats(player_id=player_id)

    # pandas data frames (optional: pip install pandas)
    career.get_data_frames()[0]

    career.get_json()

    career.get_dict()

    df_player = career.get_data_frames()[0]
    player_name = df_all_players[df_all_players['id'] == int(player_id)]['full_name'].item()
    df_player['PLAYER_NAME'] = player_name
    print(df_player)
    file_name = 'datasets/nba_player.csv'
    df_player.to_csv(file_name, mode='a')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Write the DataFrame back to a new CSV file
    df.to_csv(file_name, index=False)


# ######################################################
def get_players():

    nba_players = players.get_players()
    print("Number of players fetched: {}".format(len(nba_players)))
    df_all_players = pd.DataFrame(nba_players)
    print(df_all_players)

    return df_all_players


# ######################################################
def nba_live_data():

    # Today's Score Board
    board = scoreboard.ScoreBoard()
    print("ScoreBoardDate: " + board.score_board_date)

    games = board.get_dict()['scoreboard']['games']

    f = "{gameId}: {awayTeam} vs. {homeTeam} @ {gameTimeLTZ}"

    for game in games:
        gameTimeLTZ = parser.parse(game["gameTimeUTC"]).replace(tzinfo=timezone.utc).astimezone(tz=None)
        print(f.format(
            gameId=game['gameId'],
            awayTeam=game['awayTeam']['teamName'],
            homeTeam=game['homeTeam']['teamName'],
            gameTimeLTZ=gameTimeLTZ
        ))
        box = boxscore.BoxScore(game['gameId'])
        box_dict = box.game.get_dict()
        print(box_dict)
# ######################################################


df = get_players()
get_data(df, '203999')
