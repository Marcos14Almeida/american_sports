import sys
import os
import pandas as pd

from scripts.classes import Colors
from scripts.country_names import CountryNames

#  Add the directory containing the module to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


class NFL:

    arizona = "Arizona Cardinals"
    atlanta = "Atlanta Falcons"
    baltimore = "Baltimore Ravens"
    buffalo = "Buffalo Bills"
    carolina = "Carolina Panthers"
    cincinnati = "Cincinnati Bengals"
    cleveland = "Cleveland Browns"
    chicago = "Chicago Bears"
    dallas = "Dallas Cowboys"
    denver = "Denver Broncos"
    detroit = "Detroit Lions"
    lv_raiders = "Las Vegas Raiders"
    la_chargers = "Los Angeles Chargers"
    la_rams = "Los Angeles Rams"
    green_bay = "Green Bay Packers"
    houston = "Houston Texans"
    indianapolis = "Indianapolis Colts"
    jaguars = "Jacksonville Jaguars"
    kansas = "Kansas City Chiefs"
    miami = "Miami Dolphins"
    vikings = "Minnessota Vikings"
    nepatriots = "New England Patriots"
    nyjets = "New York Jets"
    nygiants = "New York Giants"
    nosaints = "New Orleans Saints"
    pittsburgh = "Pittsburgh Steelers"
    peagles = "Philadelphia Eagles"
    seattle = "Seattle Seahawks"
    sf49ers = "San Francisco 49ers"
    tampa_bay = "Tampa Bay Buccanners"
    tenesse = "Tennesse Titans"
    washington = "Washington Commanders"


class Conference_nfl():

    afc = "AFC"
    nfc = "NFC"


class Division_nfl():

    east = "East"
    west = "West"
    north = "North"
    south = "South"


def nfl_to_convert():

    c = Colors.transparent
    _c = CountryNames()
    d = Division_nfl()
    co = Conference_nfl()
    n = NFL()

    return {
        n.arizona: [
            "ARZ", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.west, 'University of Phoenix Stadium', 63400, 0, 0,
            c.red, c.white, c.transparent, c.secondary, []],
        n.atlanta: [
            "ATL", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.south, 'Mercedes-Benz Stadium', 71000, 0, 0,
            c.red, c.black, c.white, c.secondary, []],
        n.baltimore: [
            "BAL", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.north, 'M&T Bank Stadium', 71008, 0, 0,
            c.purple, c.black, c.transparent, c.secondary, []],
        n.buffalo: [
            "BUF", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.east, 'Highmark Stadium', 71608, 0, 0,
            c.blue, c.red, c.transparent, c.secondary, []],
        n.carolina: [
            "CAR", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.south, 'Bank of America Stadium', 75525, 0, 0,
            c.blue, c.black, c.white, c.secondary, []],
        n.chicago: [
            "CHI", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.north, 'Soldier Field', 61500, 0, 0,
            c.darkblue, c.orange, c.transparent, c.secondary, [n.green_bay]],
        n.cincinnati: [
            "CIN", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.north, 'Paul Brown Stadium', 65515, 0, 0,
            c.black, c.orange, c.transparent, c.secondary, []],
        n.cleveland: [
            "CLE", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.north, 'FirstEnergy Stadium', 67895, 0, 0,
            c.orange, c.brown, c.transparent, c.secondary, []],
        n.dallas: [
            "DAL", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.east, 'AT&T Stadium', 80000, 0, 0,
            c.white, c.blue, c.transparent, c.secondary, []],
        n.denver: [
            "DEN", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.west, 'Empower Field', 76125, 0, 0,
            c.orange, c.blue, c.white, c.secondary, []],
        n.detroit: [
            "DET", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.north, 'Ford Field', 65000, 0, 0,
            c.blue, c.white, c.transparent, c.secondary, []],
        n.green_bay: [
            "GB", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.north, 'Lambeau Field', 81441, 0, 0,
            c.green, c.yellow, c.transparent, c.secondary, [n.chicago]],
        n.houston: [
            "HOU", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.south, 'NRG Stadium', 72220, 0, 0,
            c.darkblue, c.red, c.transparent, c.secondary, []],
        n.indianapolis: [
            "IND", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.south, 'Lucas Oil Stadium', 62421, 0, 0,
            c.blue, c.white, c.transparent, c.secondary, []],
        n.jaguars: [
            "JAC", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.south, 'TIAA Bank Field', 64428, 0, 0,
            c.blue, c.green, c.transparent, c.secondary, []],
        n.kansas: [
            "KC", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.west, 'Arrowhead Stadium', 76416, 0, 0,
            c.white, c.red, c.transparent, c.secondary, []],
        n.lv_raiders: [
            "LV", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.west, 'Allegiant Stadium', 65000, 0, 0,
            c.black, c.white, c.transparent, c.secondary, []],
        n.la_chargers: [
            "LAC", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.west, 'SoFI Stadium', 70242, 0, 0,
            c.blue, c.yellow, c.white, c.secondary, []],
        n.la_rams: [
            "LAR", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.west, 'SoFI Stadium', 70242, 0, 0,
            c.blue, c.yellow, c.white, c.secondary, []],
        n.miami: [
            "MIA", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.east, 'Hard Rock Stadium', 65326, 0, 0,
            c.white, c.lightgreen, c.orange, c.secondary, []],
        n.vikings: [
            "MIN", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.north, 'U.S. Bank Stadium', 66655, 0, 0,
            c.purple, c.yellow, c.transparent, c.secondary, []],
        n.nepatriots: [
            "NE", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.east, 'Gillette Stadium', 66829, 0, 0,
            c.white, c.blue, c.transparent, c.secondary, []],
        n.nosaints: [
            "NO", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.south, 'Caesars Superdome', 76468, 0, 0,
            c.black, c.gold, c.transparent, c.secondary, []],
        n.nyjets: [
            "NYJ", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.east, 'MetLife Stadium', 82500, 0, 0,
            c.darkgreen, c.white, c.transparent, c.secondary, []],
        n.nygiants: [
            "NYG", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.east, 'MetLife Stadium', 82500, 0, 0,
            c.blue, c.white, c.transparent, c.secondary, []],
        n.peagles: [
            "PHI", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.east, 'Lincoln Financial Stadium', 69176, 0, 0,
            c.darkgreen, c.white, c.transparent, c.secondary, []],
        n.pittsburgh: [
            "PIT", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.north, 'Acrisure Stadium', 68400, 0, 0,
            c.yellow, c.black, c.transparent, c.secondary, []],
        n.seattle: [
            "SEA", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.west, 'Lumen Field', 68740, 0, 0,
            c.darkblue, c.green, c.transparent, c.secondary, []],
        n.sf49ers: [
            "SF", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.west, 'Levi\'s Stadium', 68500, 0, 0,
            c.red, c.white, c.transparent, c.secondary, []],
        n.tampa_bay: [
            "TB", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.south, 'Raymond James Stadium', 65890, 0, 0,
            c.red, c.black, c.transparent, c.secondary, []],
        n.tenesse: [
            "TEN", 75.0, 0, -1,
            _c.unitedstates, co.afc, d.south, 'Nissan Stadium', 69143, 0, 0,
            c.blue, c.lightblue, c.transparent, c.secondary, []],
        n.washington: [
            "WAS", 75.0, 0, -1,
            _c.unitedstates, co.nfc, d.east, 'FedEx Field', 82000, 0, 0,
            c.red, c.yellow, c.transparent, c.secondary, []],
    }


def save_nfl_details():

    data = nfl_to_convert()

    for key, value in data.items():
        if (len(value) != 16):
            print("Error in:", key)

    # Convert the dictionary to a DataFrame

    df = pd.DataFrame(data).T
    df['name'] = df.index
    df = df.reset_index(drop=True)

    newcountrycolumns = [
                "abbreviation", "overall",
                "foundation", "extinct",
                "country", "conference", "division", "stadium_name", "stadium_size",
                "coord_lat", "coord_long",
                "color_primary", "color_secondary", "color_third",  "color_short",
                "rivals",
                "name"
        ]

    df.columns = newcountrycolumns

    # Move Column
    df = df[['name'] + [col for col in df.columns if col != 'name']]

    # Save the DataFrame to a CSV file
    df.to_csv('datasets/nfl_details.csv', index=False)


save_nfl_details()
