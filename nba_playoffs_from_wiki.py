import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd


def renameTeams(teamName):
    map = {}
    map[teamName] = teamName
    map['Atlanta'] = "Atlanta Hawks"
    map['Boston'] = "Boston Celtics"
    map['Brooklyn'] = "Brooklyn Nets"
    map['New Jersey'] = "Brooklyn Nets"
    map['Charlotte'] = "Charlotte Hornets"
    map['Chicago'] = "Chicago Bulls"
    map['Cleveland'] = "Cleveland Cavaliers"
    map['Dallas'] = "Dallas Mavericks"
    map['Denver'] = "Denver Nuggets"
    map['Detroit'] = "Detroit Pistons"
    map['Golden State'] = "Golden State Warriors"
    map['Houston'] = "Houston Rockets"
    map['Indiana'] = "Indiana Pacers"
    map['LA Lakers'] = "Los Angeles Lakers"
    map['Memphis'] = "Memphis Grizzlies"
    map['Miami'] = "Miami Heat"
    map['Milwaukee'] = "Milwaukee Bucks"
    map['Minnesota'] = "Minnesota Timberwolves"
    map['New York'] = "New York Knicks"
    map['New Orleans'] = "New Orleans Pelicans"
    map['Oklahoma City'] = "Oklahoma City Thunder"
    map['Orlando'] = "Orlando Magic"
    map['Philadelphia'] = "Philadelphia 76ers"
    map['Phoenix'] = "Phoenix Suns"
    map['Portland'] = "Portland Trail Blazers"
    map['San Antonio'] = "San Antonio Spurs"
    map['Seattle'] = "Seattle SuperSonics"
    map['Sacramento'] = "Sacramento Kings"
    map['Toronto'] = "Toronto Raptors"
    map['Utah'] = "Utah Jazz"
    map['Washington'] = "Washington Wizards"
    return map[teamName]


def move_column(df, number):
    row_to_move = df.iloc[number].copy()  # Copy the row to be moved
    df = df.drop(number)  # Drop the row from its original position
    df = df.append(row_to_move)
    return df


def get_playoffs(year):

    # URL of the webpage
    url = f"https://en.wikipedia.org/wiki/{year}_NBA_playoffs"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        tree = html.fromstring(response.content)

        # Find the element using the specified XPath
        xpath = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[4]'

        a = False
        table_n = 1
        while a is False:
            try:
                xpath = f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[{table_n}]'
                target_element = tree.xpath(xpath)
                if target_element:
                    tbody_text = target_element[0].text_content()
                    lines = tbody_text.split("\n")
                    i = 0
                    match = []
                    for object in lines:
                        if all(object not in line for line in lines[:4]):
                            print("a", object)
                            if len(object) != 2 and len(object) != 0 and len(object) <= 13 and "Conference" not in object or object == "Oklahoma City Thunder":
                                object = object.replace("*", "")
                                # print(object)
                                match.append(object)
                                if (i % 4 == 3):
                                    print()
                                i += 1
                match = [match[i:i+4] for i in range(0, len(match), 4)]
                print(table_n)
                print(year)
                print(match)
                if len(match) > 0 and len(match) > 10 and len(match[0][1]) == 1 and len(match[0][0]) > 1:
                    a = True
                else:
                    table_n += 1
            except ValueError:
                a = False
                table_n += 1

        df = pd.DataFrame(match, columns=['team1', 'score1', 'team2', 'score2'])
        if year >= 1984:
            new_column_values = [
                "First round", "Conference semifinals", "First round",
                "Conference finals",
                "First round", "Conference semifinals", "First round",
                "NBA Finals",
                "First round", "Conference semifinals", "First round",
                "Conference finals",
                "First round", "Conference semifinals", "First round"
                ]
            matchs = [
                1, 1, 2,
                1,
                3, 2, 4,
                1,
                5, 3, 6,
                2,
                7, 4, 8,
            ]
        else:
            new_column_values = [
                "Conference semifinals", "First round", "Conference finals",
                "Conference semifinals", "First round", "Conference finals",
                "Conference semifinals", "First round", "Conference finals",
                "Conference semifinals", "First round"
                ]
            matchs = [
                1, 1, 1,
                2, 2, 2,
                3, 3, 3,
                4, 4,
            ]
        df['stage'] = new_column_values
        df['matchs'] = matchs
        df['year'] = year
        df['team1'] = df['team1'].apply(renameTeams)
        df['team2'] = df['team2'].apply(renameTeams)

        columns = ['year'] + [col for col in df if col != 'year']
        df = df[columns]

        # Sort the DataFrame based on the custom order
        custom_order = ["First round", "Conference semifinals", "Conference finals", "NBA Finals"]
        df['stage'] = pd.Categorical(df['stage'], categories=custom_order, ordered=True)
        df = df.sort_values(by='stage')

        save_file = 'datasets/nba_playoffs.csv'
        # Get DF from file
        try:
            df_csv = pd.read_csv(save_file)
            df = pd.concat([df_csv, df], ignore_index=True)
            df = df.drop_duplicates()
        except:
            df = df

        # Save the DataFrame to a CSV file
        df.to_csv(save_file, index=False)

        print("Data saved to nba_playoffs.csv")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)


# ###########################################################
# MAIN
# ###########################################################

for year in range(2000, 2005):
    get_playoffs(year)
