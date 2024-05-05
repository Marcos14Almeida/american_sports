import sys
import os
import pandas as pd

from scripts.classes import Colors
from scripts.country_names import CountryNames

#  Add the directory containing the module to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


class NBA:
    atlanta = "Atlanta Hawks"
    boston = "Boston Celtics"
    brooklyn = "Brooklyn Nets"
    charlotte = "Charlotte Hornets"
    chicago = "Chicago Bulls"
    cleveland = "Cleveland Cavaliers"
    dallas = "Dallas Mavericks"
    denver = "Denver Nuggets"
    detroit = "Detroit Pistons"
    golden_state = "Golden State Warriors"
    houston = "Houston Rockets"
    indiana = "Indiana Pacers"
    la_clippers = "LA Clippers"
    la_lakers = "Los Angeles Lakers"
    memphis = "Memphis Grizzlies"
    miami = "Miami Heat"
    milwaukee = "Milwaukee Bucks"
    minnesota = "Minnesota Timberwolves"
    new_orleans = "New Orleans Pelicans"
    new_york = "New York Knicks"
    oklahoma_city = "Oklahoma City Thunder"
    orlando = "Orlando Magic"
    philadelphia = "Philadelphia 76ers"
    phoenix = "Phoenix Suns"
    portland = "Portland Trail Blazers"
    sacramento = "Sacramento Kings"
    san_antonio = "San Antonio Spurs"
    toronto = "Toronto Raptors"
    utah = "Utah Jazz"
    washington = "Washington Wizards"

    # EURO
    barcelona = "FC Barcelona"
    real_madrid = "Real Madrid"
    cska_moscow = "CSKA Moscow"
    fenerbahce = "Fenerbahce Beko"
    olympiacos = "Olympiacos Piraeus"
    maccabi_tel_aviv = "Maccabi Tel Aviv"
    panathinaikos = "Panathinaikos Athens"
    anadolu_efes = "Anadolu Efes Istanbul"
    zenit = "Zenit Saint Petersburg"
    asvel = "ASVEL Basket"
    alba_berlin = "ALBA Berlin"
    bayern_munich = "FC Bayern Munich"
    milano = "AX Armani Exchange Milan"
    valencia = "Valencia Basket"
    zalgiris = "Zalgiris Kaunas"
    crvena_zvezda = "Crvena Zvezda mts Belgrade"
    khimki = "Khimki Moscow Region"
    baskonia = "TD Systems Baskonia Vitoria-Gasteiz"
    olimpia_milano = "Olimpia Milano"
    baskonia = "KIROLBET Baskonia Vitoria-Gasteiz"
    as_monaco = "AS Monaco Basket"
    ld_lc = "LDLC ASVEL Villeurbanne"
    promitheas = "Promitheas Patras"
    tsmoki_minsk = "Tsmoki-Minsk"
    hapoel_holon = "Hapoel Holon"
    paok = "PAOK Thessaloniki"
    aek_athens = "AEK Athens BC"
    nizhny_novgorod = "Nizhny Novgorod"
    rytas = "Rytas Vilnius"

    # BRASIL
    flamengo = "Flamengo"
    bauru = "Bauru Basket"
    corinthians = "Corinthians Basketball"
    saopaulo = "São Paulo Basketball"
    brasilia = "Brasília"
    franca = "Franca"
    mogi_das_cruzes = "Mogi das Cruzes"

    # SOUTH AMERICA
    san_lorenzo = "San Lorenzo"
    regatas = "Regatas Corrientes"
    atenas = "Atenas Córdoba"
    boca_juniors = "Boca Juniors"
    hebraica = "Hebraica Macabi"
    olimpia = "Olimpia"
    estudiantes = "Estudiantes Concordia"
    instituto = "Instituto de Córdoba"
    ferro_carril = "Ferro Carril Oeste"
    quimsa = "Quimsa"
    argentino = "Argentino de Junín"
    hispano = "Hispano Americano"
    libertad = "Libertad"
    gimnasia = "Gimnasia y Esgrima"
    atletico_nacional = "Atlético Nacional"
    universitario = "Universitario de Sucre"
    regatas = "Regatas Lima"
    universo = "Universo"
    academica = "Académica de Coimbra"
    sol = "Sol de América"
    malvin = "Malvín"

    # MOVED
    new_jersey_nets = "New Jersey Nets"
    stlouis_hawks = "St. Louis Hawks"
    vancouver_grizzlies = "Vancouver Grizzlies"
    washington_bullets = "Washington Bullets"

    # EXTINCT
    seattle = "Seattle SuperSonics"
    buffalo = "Buffalo Braves"


class Division_nba():

    atlantic = "Atlantic"
    central = "Central"
    southeast = "Southeast"

    northwest = "Northwest"
    pacific = "Pacific"
    southwest = "Southwest"


def nba_to_convert():

    c = Colors.transparent
    _c = CountryNames()
    d = Division_nba()
    n = NBA()

    map = {
        n.atlanta: [
            "ATL", 78.4, 1949, -1,
            _c.unitedstates, d.southeast, 'State Farm Arena', 18729, 0, 0,
            c.white, c.red, c.transparent, c.secondary, c.primary, []],
        n.boston: [
            "BOS", 81.6, 1946, -1,
            _c.unitedstates, d.atlantic, 'TD Garden', 18624, 0, 0,
            c.green, c.white, c.transparent, c.secondary, c.primary, []],
        n.brooklyn: [
            "BKN", 77.5, 1976, -1,
            _c.unitedstates, d.atlantic, 'Barclays Center', 0, 0, 0,
            c.black, c.white, c.transparent, c.secondary, c.primary, []],
        n.charlotte: [
            "CHA", 76.1, 1988, -1,
            _c.unitedstates, d.southeast, 'Spectrum Center', 19026, 0, 0,
            c.purple, c.lightblue, c.transparent, c.secondary, c.primary, []],
        n.chicago: [
            "CHI", 78.3, 1966, -1,
            _c.unitedstates, d.central, 'United Center', 21711, 0, 0,
            c.red, c.black, c.transparent, c.secondary, c.primary, []],
        n.cleveland: [
            "CLE", 77.1, 1970, -1,
            _c.unitedstates, d.central, 'Quicken Loans Arena', 20562, 0, 0,
            c.black, c.orange, c.transparent, c.secondary, c.primary, []],
        n.dallas: [
            "DAL", 77.8, 1980, -1,
            _c.unitedstates, d.southwest, 'American Airlines Center', 19200, 0, 0,
            c.blue, c.black, c.transparent, c.secondary, c.primary, []],
        n.denver: [
            "DEN", 79.4, 1976, -1,
            _c.unitedstates, d.northwest, 'Pepsi Center', 19099, 0, 0,
            c.darkblue, c.yellow, c.white, c.secondary, c.primary, []],
        n.detroit: [
            "DET", 75.6, 1948, -1,
            _c.unitedstates, d.central, 'Little Caesars Arena', 21000, 0, 0,
            c.blue, c.red, c.transparent, c.secondary, c.primary, []],
        n.golden_state: [
            "GSW", 79.7, 1946, -1,
            _c.unitedstates, d.pacific, 'Chase Center', 19596, 0, 0,
            c.blue, c.yellow, c.transparent, c.secondary, c.primary, []],
        n.houston: [
            "HOU", 77.0, 1967, -1,
            _c.unitedstates, d.southwest, 'Toyota Center', 18104, 0, 0,
            c.red, c.white, c.transparent, c.secondary, c.primary, []],
        n.indiana: [
            "IND", 77.2, 1976, -1,
            _c.unitedstates, d.central, 'Bankers Life Fieldhouse', 18345, 0, 0,
            c.yellow, c.blue, c.transparent, c.secondary, c.primary, []],
        n.la_clippers: [
            "LAC", 77.4, 1970, -1,
            _c.unitedstates, d.pacific, 'Staples Center', 19060, 0, 0,
            c.white, c.blue, c.red, c.secondary, c.primary, []],
        n.la_lakers: [
            "LAL", 79.9, 1948, -1,
            _c.unitedstates, d.pacific, 'Staples Center', 19060, 0, 0,
            c.yellow, c.purple, c.transparent, c.secondary, c.primary, []],
        n.memphis: [
            "MEM", 78.5, 1995, -1,
            _c.unitedstates, d.southwest, 'FedExForum', 18119, 0, 0,
            c.lightblue, c.black, c.transparent, c.secondary, c.primary, []],
        n.miami: [
            "MIA", 78.8, 1988, -1,
            _c.unitedstates, d.southeast, 'AmericanAirlines Arena', 19600, 0, 0,
            c.white, c.red, c.transparent, c.secondary, c.primary, []],
        n.milwaukee: [
            "MIL", 78.6, 1968, -1,
            _c.unitedstates, d.central, 'Fiserv Forum', 17500, 0, 0,
            c.green, c.white, c.transparent, c.secondary, c.primary, []],
        n.minnesota: [
            "MIN", 77.4, 1989, -1,
            _c.unitedstates, d.northwest, 'Target Center', 19356, 0, 0,
            c.darkblue, c.green, c.transparent, c.secondary, c.primary, []],
        n.new_orleans: [
            "NOP", 76.7, 2002, -1,
            _c.unitedstates, d.southwest, 'Smoothie King Center', 0, 0, 0,
            c.darkblue, c.gold, c.transparent, c.secondary, c.primary, []],
        n.new_york: [
            "NYK", 76.8, 1946, -1,
            _c.unitedstates, d.atlantic, 'Madison Square Garden', 19763, 0, 0,
            c.blue, c.orange, c.transparent, c.secondary, c.primary, []],
        n.oklahoma_city: [
            "OKC", 76.0, 1967, -1,
            _c.unitedstates, d.northwest, 'Chesapeake Energy Arena', 19163, 0, 0,
            c.blue, c.orange, c.black, c.secondary, c.primary, []],
        n.orlando: [
            "ORL", 75.3, 1989, -1,
            _c.unitedstates, d.southeast, 'Amway Center', 0, 0, 0,
            c.blue, c.black, c.transparent, c.secondary, c.primary, []],
        n.philadelphia: [
            "PHI", 78.2, 1949, -1,
            _c.unitedstates, d.atlantic, 'Wells Fargo Center', 0, 0, 0,
            c.red, c.blue, c.transparent, c.secondary, c.primary, []],
        n.phoenix: [
            "PHO", 77.9, 1968, -1,
            _c.unitedstates, d.pacific, 'Talking Stick Resort Arena', 0, 0, 0,
            c.purple, c.orange, c.transparent, c.secondary, c.primary, []],
        n.portland: [
            "POR", 74.6, 1970, -1,
            _c.unitedstates, d.northwest, 'Moda Center', 19980, 0, 0,
            c.black, c.red, c.white, c.secondary, c.primary, []],
        n.sacramento: [
            "SAC", 76.4, 1948, -1,
            _c.unitedstates, d.pacific, 'Golden 1 Center', 17500, 0, 0,
            c.purple, c.white, c.transparent, c.secondary, c.primary, []],
        n.san_antonio: [
            "SAS", 74.9, 1976, -1,
            _c.unitedstates, d.northwest, 'AT&T Center', 18694, 0, 0,
            c.grey, c.black, c.transparent, c.secondary, c.primary, []],
        n.toronto: [
            "TOR", 76.4, 1995, -1,
            _c.canada, d.atlantic, 'Scotiabank Arena', 19800, 0, 0,
            c.black, c.red, c.transparent, c.secondary, c.primary, []],
        n.utah: [
            "UTA", 76.3, 1974, -1,
            _c.unitedstates, d.northwest, 'Vivint Smart Home Arena', 20148, 0, 0,
            c.darkblue, c.green, c.yellow, c.secondary, c.primary, []],
        n.washington: [
            "WAS", 74.2, 1961, -1,
            _c.unitedstates, d.southeast, 'Capital One Arena', 20647, 0, 0,
            c.red, c.blue, c.transparent, c.secondary, c.primary, []],

        n.seattle: [
            "SEA", 76.2, 1967, -1,
            _c.unitedstates, d.northwest, 'KeyArena', 17000, 0, 0,
            c.green, c.yellow, c.transparent, c.secondary, c.primary, []],
        n.buffalo: [
            "BUF", 75.0, 1970, -1,
            _c.unitedstates, d.atlantic, 'Buffalo Memorial Auditorium', 18000, 0, 0,
            c.black, c.orange, c.white, c.secondary, c.primary, []],
    }

    return map


def save_nba_details():

    data = nba_to_convert()

    for key, value in data.items():
        if (len(value) != 16):
            print("Error in length:", key)

    # Convert the dictionary to a DataFrame

    df = pd.DataFrame(data).T
    df['name'] = df.index
    df = df.reset_index(drop=True)

    newcountrycolumns = [
                "abbreviation", "overall",
                "foundation", "extinct",
                "country", "division", "stadium_name", "stadium_size",
                "coord_lat", "coord_long",
                "color_primary", "color_secondary", "color_third",  "color_short", "color_socks",
                "rivals",
                "name"
        ]

    df.columns = newcountrycolumns

    # Move Column
    df = df[['name'] + [col for col in df.columns if col != 'name']]

    # Save the DataFrame to a CSV file
    df.to_csv('datasets/nba_details.csv', index=False)


save_nba_details()
