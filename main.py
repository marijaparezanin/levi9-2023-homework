import csv
import os
from flask import Flask, jsonify

separator = os.path.sep
csv_file_path = "files" + separator + "L9HomeworkChallengePlayersInput.csv"
players_App = Flask(__name__)

def load_CSV(path):
    players_basic_info = {}
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        #skipping header
        next(csv_reader, None)

        for row in csv_reader:
            if(row[0] not in players_basic_info):
                players_basic_info[row[0]] = {"playerName": row[0], "position": row[1], "FTM": int(row[2]), "FTA": int(row[3]), "2PM": int(row[4]), "2PA": int(row[5]), "3PM": int(row[6]), "3PA" : int(row[7]), "REB": int(row[8]), "BLK" : int(row[9]), "AST": int(row[10]), "STL": int(row[11]), "TOV" : int(row[12]), "GAMES" :1}
            else:
                players_basic_info[row[0]]["FTM"] += int(row[2])
                players_basic_info[row[0]]["FTA"] += int(row[3])
                players_basic_info[row[0]]["2PM"] += int(row[4])
                players_basic_info[row[0]]["2PA"] += int(row[5])
                players_basic_info[row[0]]["3PM"] += int(row[6])
                players_basic_info[row[0]]["3PA"] += int(row[7])
                players_basic_info[row[0]]["REB"] += int(row[8])
                players_basic_info[row[0]]["BLK"] += int(row[9])
                players_basic_info[row[0]]["AST"] += int(row[10])                
                players_basic_info[row[0]]["STL"] += int(row[11])
                players_basic_info[row[0]]["TOV"] += int(row[12])
                players_basic_info[row[0]]["GAMES"] += 1
    return players_basic_info

def calculate_player_stats(player):
    freeThrows = {
        "attempts": round(player["FTA"]/player["GAMES"],1),
        "made" : round(player["FTM"]/player["GAMES"],1),
        "shootingPercentage":round(player["FTM"]/player["FTA"]*100,1)
    }

    twoPoints =  { "attempts":  round(player["2PA"]/player["GAMES"],1),
                   "made":  round(player["2PM"]/player["GAMES"], 1),
                 "shootingPercentage":  round(player["2PM"]/player["2PA"]*100, 1) },

    threePoints =  { "attempts": round(player["3PA"]/player["GAMES"], 1),
                   "made": round(player["3PM"]/player["GAMES"], 1),
                 "shootingPercentage":  round(player["3PM"]/player["3PA"]*100 ,1)},

    PTS = player["FTM"] + 2*player["2PM"] + 3*player["3PM"]
    valorization =  round(((player["FTM"] + 2*player["2PM"] + 3*player["3PM"] + player["REB"] + player["BLK"] + player["AST"] + player["STL"]) - (player["FTA"]-player["FTM"] + player["2PA"]-player["2PM"] + player["3PA"]-player["3PM"] + player["TOV"]))/player["GAMES"],1)
    effectiveFieldGoalPercentage = round((player["2PM"] + player["3PM"] + 0.5 * player["3PM"]) / (player["2PA"] + player["3PA"]) * 100,1)
    trueShootingPercentage = round(PTS / (2 * (player["2PA"] + player["3PA"] +0.475 * player["FTA"])) * 100, 1)
    hollingerAssistRatio = round(player["AST"] / (player["2PA"] + player["3PA"] + 0.475 * player["FTA"] + player["AST"] + player["TOV"]) * 100, 1)



    return {"playerName" : player["playerName"],
            "gamesPlayed" : player["GAMES"],
            "traditional": {
                "freeThrows": freeThrows,
                "twoPoints" :twoPoints,
                "threePoints" : threePoints,
                "points" : round(PTS/player["GAMES"],1),
                "rebounds" : round(player["REB"] / player["GAMES"],1),
                "blocks":round(player["BLK"] / player["GAMES"],1),
                "assists":round(player["AST"] / player["GAMES"],1),
                "steals":round(player["STL"] / player["GAMES"],1),
                "turnovers":round(player["TOV"] / player["GAMES"],1),
            }, 
            "advanced":{
                "valorization":valorization,
                "effectiveFieldGoalPercentage":effectiveFieldGoalPercentage,
                "trueShootingPercentage":trueShootingPercentage,
                "hollingerAssistRatio":hollingerAssistRatio
            }
            }

@players_App.route('/stats/player/<player_full_name>', methods=['GET'])
def get_player_stats(player_full_name):
    players_data = load_CSV(csv_file_path)
    if player_full_name in players_data:
        player_stats = calculate_player_stats(players_data[player_full_name])
        return jsonify(player_stats)
    else:
        return jsonify({'error': 'Player not found'}), 404

if __name__ == '__main__':
    players_App.run()