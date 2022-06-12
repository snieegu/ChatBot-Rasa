# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
#
# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import pprint


class actionMovePlayer(Action):

    def name(self) -> Text:
        return "action_move_player"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open('./eSportData/players.json', 'r')
        data = json.load(file)

        current_player = next(tracker.get_latest_entity_values("player"), None)
        current_team = next(tracker.get_latest_entity_values("team"), None)
        current_number = next(tracker.get_latest_entity_values("number"), None)

        if not current_player:
            msg = "Player name not provided."
            dispatcher.utter_message(text=msg)

        if not current_team:
            msg = "Player team not provided."
            dispatcher.utter_message(text=msg)

        playerData = data.get(current_player, None)
        if not playerData:
            msg = "Bad spelling or the player doesn't exist in DB"
            dispatcher.utter_message(text=msg)

        if current_player:
            if playerData[1] == current_team:
                msg = "Player already in the team"
                dispatcher.utter_message(text=msg)
            else:
                file.close()
                file = open('./eSportData/players.json', 'w')
                new_player = current_player
                data[new_player] = [current_number, current_team]
                json.dump(data, file)
                msg = "Added " + new_player + " to " + current_team + " with number " + current_number
                dispatcher.utter_message(text=msg)

        file.close()
        return []


class actionShowTable(Action):

    def name(self) -> Text:
        return "action_show_table"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open('./eSportData/players.json', 'r')
        data = json.load(file)
        # pprint.pprint(data)
        teamTable = []

        msg = data
        dispatcher.utter_message(text=msg)
        file.close()
        return []


class actionShowTeamInfo(Action):
    def name(self) -> Text:
        return "action_show_team_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open('./eSportData/players.json', 'r')
        data = json.load(file)
        current_team = next(tracker.get_latest_entity_values("team"), None)

        msg = "In " + current_team + " play: "
        dispatcher.utter_message(text=msg)

        for player, info in data.items():
            if info[1] == current_team:
                print(player)
                msg = player
                dispatcher.utter_message(text=msg)
        file.close()
        return []


class actionWhereHePlays(Action):
    def name(self) -> Text:
        return "action_show_where_plays"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open('./eSportData/players.json', 'r')
        data = json.load(file)
        current_player = next(tracker.get_latest_entity_values("player"), None)
        if current_player:
            playerData = data.get(current_player, None)

            msg = "Player " + current_player + " plays in " + playerData[1] + " with number " + playerData[0]

        else:
            msg = "Where who play ?"

        dispatcher.utter_message(text=msg)
        file.close()
        return []
