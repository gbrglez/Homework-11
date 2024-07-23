import datetime
import random
import json
secret = random.randint(1, 30)
#print(secret)
attempts = 0
guessList = []
with open("score_list.json", "r") as scoreFile:
    scoreList = json.loads(scoreFile.read())
    #scoreList.sort()

    # numberOfPlayedGames = len(scoreList)
    # print(numberOfPlayedGames)

    #print("Top scores: " + str(scoreList[:3]))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1


    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        playerName = input("Input your name for the records: ")
        scoreData = {
            "name": playerName,
            "attempts": attempts,
            "date": str(datetime.datetime.now()),
            "wrong_guesses": guessList
        }
        scoreList.append(scoreData)
        with open("score_list.json", "w") as scoreFile:
            scoreFile.write(json.dumps(scoreList))
        break
    elif guess > secret:
        guessList.append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        guessList.append(guess)
        print("Your guess is not correct... try something bigger")

with open("score_list.json", "r") as scoreFile:
    scoreList = json.loads(scoreFile.read())
    topThree = sorted(scoreList, key=lambda item: item["attempts"])
    print("Best results: ")
    for player in topThree[:3]:
        print(player)


