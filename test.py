import datetime
import random
import json

with open("score_list.json", "r") as scoreFile:
    scoreList = json.loads(scoreFile.read())
    topThree = sorted(scoreList, key=lambda item: item["attempts"])
    for player in topThree[:3]:
        print(player)
