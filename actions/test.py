import json
import pprint


def actionMovePlayer(current_player, current_number, current_team):
    file = open('players.json', 'r')
    data = json.load(file)

    if not current_player:
        print("Player name not provided.")

    if not current_team:
        print("Player team not provided.")

    playerData = data.get(current_player, None)
    if not playerData:
        print("Bad spelling or the player doesn't exist in DB")

    if playerData[1] == current_team:
        print("Player already in the team")
    else:
        file.close()
        file = open('players.json', 'w')
        new_player = current_player
        data[new_player] = [current_number, current_team]
        json.dump(data, file)

    file.close()


def actionShowTable():
    file = open('players.json')
    data = json.load(file)
    pprint.pprint(data)
    file.close()


def actionShowTeamInfo(current_team):
    file = open('../eSportData/players.json', 'r')
    data = json.load(file)


    for player, info in data.items():
        if info[1] == current_team:
            print(player)


if __name__ == '__main__':
    # actionMovePlayer("Lewandowski", 9, "Barcelona")
    # actionShowTable()
    actionShowTeamInfo("Bayern")