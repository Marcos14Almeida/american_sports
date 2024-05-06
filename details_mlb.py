import sys
import os
import pandas as pd

from scripts.classes import Colors
from scripts.country_names import CountryNames

#  Add the directory containing the module to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


class mlb:

    arizona_diamondbacks = "Arizona Diamondbacks"
    atlanta_braves = "Atlanta Braves"
    baltimore_orioles = "Baltimore Orioles"
    boston_red_sox = "Boston Red Sox"
    chicago_cubs = "Chicago Cubs"
    chicago_white_sox = "Chicago White Sox"
    cincinnati_reds = "Cincinnati Reds"
    cleveland_guardians = "Cleveland Guardians"
    colorado_rockies = "Colorado Rockies"
    detroit_tigers = "Detroit Tigers"
    houston = "Houston Astros"
    kc_royals = "Kansas City Royals"
    la_angels = "Los Angeles Angels"
    la_dodgers = "Los Angeles Dodgers"
    miami = "Miami Marlins"
    milwaukee_brewers = "Milwaukee Brewers"
    minnesota_twins = "Minnesota Twins"
    ny_mets = "New York Mets"
    ny_yankees = "New York Yankees"
    oakland_athletics = "Oakland Athletics"
    philadelphia = "Philadelphia Phillies"
    pittsburgh_pirates = "Pittsburgh Pirates"
    sd_padres = "San Diego Padres"
    sf_giants = "San Francisco Giants"
    seattle_mariners = "Seattle Mariners"
    sl_cardinals = "St. Louis Cardinals"
    tb_rays = "Tampa Bay Rays"
    texas_rangers = "Texas Rangers"
    toronto_blue_jays = "Toronto Blue Jays"
    washington_nationals = "Washington Nationals"


def mlb_to_convert():

    c = Colors.transparent
    _c = CountryNames()
    n = mlb()

    return {
        n.arizona_diamondbacks: [
            50.0, 0, -1,
            _c.unitedstates, 'Chase Field', 48686, 0, 0,
            c.black, c.red, c.transparent, []],
        n.atlanta_braves: [
            50.0, 0, -1,
            _c.unitedstates, 'Truist Park', 41084, 0, 0,
            c.red, c.black, c.transparent, []],
        n.baltimore_orioles: [
            50.0, 0, -1,
            _c.unitedstates, 'Oriole Park', 45971, 0, 0,
            c.orange, c.black, c.transparent, []],
        n.boston_red_sox: [
            50.0, 0, -1,
            _c.unitedstates, 'Fenway Park', 37755, 0, 0,
            c.red, c.white, c.transparent, []],
        n.chicago_cubs: [
            50.0, 0, -1,
            _c.unitedstates, 'Wrigley Field', 41649, 0, 0,
            c.blue, c.red, c.transparent, []],
        n.chicago_white_sox: [
            50.0, 0, -1,
            _c.unitedstates, 'Guaranteed Rate Field', 40615, 0, 0,
            c.white, c.black, c.transparent, []],
        n.cincinnati_reds: [
            50.0, 0, -1,
            _c.unitedstates, 'Great American Ball Park', 42319, 0, 0,
            c.red, c.white, c.transparent, []],
        n.cleveland_guardians: [
            50.0, 0, -1,
            _c.unitedstates, 'Progressive Field', 34788, 0, 0,
            c.white, c.red, c.transparent, []],
        n.colorado_rockies: [
            50.0, 0, -1,
            _c.unitedstates, 'Coors Field', 50445, 0, 0,
            c.darkblue, c.white, c.transparent, []],
        n.detroit_tigers: [
            50.0, 0, -1,
            _c.unitedstates, 'Comerica Park', 41083, 0, 0,
            c.darkblue, c.white, c.transparent, []],
        n.houston: [
            50.0, 0, -1,
            _c.unitedstates, 'Minute Maid Park', 41168, 0, 0,
            c.orange, c.blue, c.transparent, []],
        n.kc_royals: [
            50.0, 0, -1,
            _c.unitedstates, 'Kauffman Stadium', 37903, 0, 0,
            c.blue, c.white, c.transparent, []],
        n.la_angels: [
            50.0, 0, -1,
            _c.unitedstates, 'Angel Stadium of Anaheim', 45517, 0, 0,
            c.red, c.white, c.transparent, []],
        n.la_dodgers: [
            50.0, 0, -1,
            _c.unitedstates, 'Dodger Stadium', 56000, 0, 0,
            c.blue, c.white, c.transparent, []],
        n.miami: [
            50.0, 0, -1,
            _c.unitedstates, 'Marlins Park', 36742, 0, 0,
            c.blue, c.orange, c.transparent, []],
        n.milwaukee_brewers: [
            50.0, 0, -1,
            _c.unitedstates, 'American Family Field', 41900, 0, 0,
            c.darkblue, c.yellow, c.transparent, []],
        n.minnesota_twins: [
            50.0, 0, -1,
            _c.unitedstates, 'Target Field', 38544, 0, 0,
            c.blue, c.red, c.transparent, []],
        n.ny_mets: [
            50.0, 0, -1,
            _c.unitedstates, 'Citi Field', 41922, 0, 0,
            c.orange, c.blue, c.transparent, []],
        n.ny_yankees: [
            50.0, 0, -1,
            _c.unitedstates, 'Yankee Stadium', 47309, 0, 0,
            c.white, c.black, c.transparent, []],
        n.oakland_athletics: [
            50.0, 0, -1,
            _c.unitedstates, 'RingCentral Coliseum', 46847, 0, 0,
            c.darkgreen, c.yellow, c.transparent, []],
        n.philadelphia: [
            50.0, 0, -1,
            _c.unitedstates, 'Citizens Bank Park', 42792, 0, 0,
            c.red, c.white, c.transparent, []],
        n.pittsburgh_pirates: [
            50.0, 0, -1,
            _c.unitedstates, 'PNC Park', 38747, 0, 0,
            c.yellow, c.black, c.transparent, []],
        n.sd_padres: [
            50.0, 0, -1,
            _c.unitedstates, 'Petco Park', 40209, 0, 0,
            c.black, c.white, c.transparent, []],
        n.sf_giants: [
            50.0, 0, -1,
            _c.unitedstates, 'Oracle Park', 41915, 0, 0,
            c.white, c.white, c.transparent, []],
        n.seattle_mariners: [
            50.0, 0, -1,
            _c.unitedstates, 'T-Mobile Park', 47929, 0, 0,
            c.darkblue, c.white, c.transparent, []],
        n.sl_cardinals: [
            50.0, 0, -1,
            _c.unitedstates, 'Busch Stadium', 45494, 0, 0,
            c.red, c.white, c.transparent, []],
        n.tb_rays: [
            50.0, 0, -1,
            _c.unitedstates, 'Tropicana Field', 25000, 0, 0,
            c.darkblue, c.white, c.transparent, []],
        n.texas_rangers: [
            50.0, 0, -1,
            _c.unitedstates, 'Globe Life Field', 40300, 0, 0,
            c.blue, c.red, c.transparent, []],
        n.toronto_blue_jays: [
            50.0, 0, -1,
            _c.canada, 'Rogers Centre', 53506, 0, 0,
            c.blue, c.white, c.transparent, []],
        n.washington_nationals: [
            50.0, 0, -1,
            _c.unitedstates, 'Nationals Park', 41339, 0, 0,
            c.red, c.white, c.transparent, []],
    }


def save_mlb_details():

    data = mlb_to_convert()

    for key, value in data.items():
        if (len(value) != 12):
            print("Error in:", key)

    # Convert the dictionary to a DataFrame

    df = pd.DataFrame(data).T
    df['name'] = df.index
    df = df.reset_index(drop=True)

    newcountrycolumns = [
                "overall",
                "foundation", "extinct",
                "country", "stadium_name", "stadium_size",
                "coord_lat", "coord_long",
                "color_primary", "color_secondary", "color_third",
                "rivals",
                "name"
        ]

    df.columns = newcountrycolumns

    # Move Column
    df = df[['name'] + [col for col in df.columns if col != 'name']]

    # Save the DataFrame to a CSV file
    df.to_csv('datasets/mlb_details.csv', index=False)


# ###########################################################
# MAIN
# ###########################################################

save_mlb_details()
