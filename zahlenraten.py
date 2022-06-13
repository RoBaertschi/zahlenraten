import random
import json
import os
import leaderboard

def result(streak, beststreak, lost, won):
    print("""  ____                 _ _   
 |  _ \ ___  ___ _   _| | |_ 
 | |_) / _ \/ __| | | | | __|
 |  _ <  __/\__ \ |_| | | |_ 
 |_| \_\___||___/\__,_|_|\__|
                             """)
    print("Win Streak: " + str(streak))
    print("Best Streak of all time: " + str(beststreak))
    print("You lost " + str(lost) + " times!")
    print("You won " + str(won) + " times!")
    print("Winrate: " + str(won / (won + lost) * 100))

if __name__ == "__main__":
    print("""
    __________      .__    .__                  __________         __                 
    \____    /____  |  |__ |  |   ____   ____   \______   \_____ _/  |_  ____   ____  
      /     /\__  \ |  |  \|  | _/ __ \ /    \   |       _/\__  \\   __\/ __ \ /    \\
     /     /_ / __ \|   Y  \  |_\  ___/|   |  \  |    |   \ / __ \|  | \  ___/|   |  \\
    /_______ (____  /___|  /____/\___  >___|  /  |____|_  /(____  /__|  \___  >___|  /
            \/    \/     \/          \/     \/          \/      \/          \/     \/ """)

    
    
    beststreak = 0
    streak = 0
    lost = 0
    won = 0
    lb = leaderboard.LeaderBoard()

    pathOfSaveFile = os.path.expanduser(os.path.join("~", ".", ".data.json"))


    if os.path.exists(pathOfSaveFile):
        with open(pathOfSaveFile, "r") as f:
            content = json.loads(f.read())
            beststreak = content["beststreak"]
            lost = content["lost"]
            won = content["won"]
            lb = leaderboard.LeaderBoard(content)
    else:
        print("There is now data.json aviable. Looks like you never played this game yet!")

    while True:
        randomnumber = random.randint(1,10)

        tries = 3

        while tries > 0:
            while True:
                try:
                    userinput = int(input("Enter a Number between 1 and 10! "))
                    break
                except ValueError:
                    print("Please input a Number!")
                
            if randomnumber == userinput:
                print('You won!')
                streak += 1
                won += 1
                if streak > beststreak:
                    beststreak = streak
                result(streak, beststreak, lost, won)
                break

            else:
                tries -= 1
                if tries <= 0:
                    print('You have lost!')
                    print('The number was:' + str(randomnumber))
                    lost += 1
                    result(streak, beststreak, lost, won)
                    streak = 0
                else:
                    if userinput > randomnumber:
                        print("Your number is to big!")
                    else:
                        print("Your number is too little!")
                    print('You have ' + str(tries) + ' tries left!')


        if input("Try again? [Y/n]: ") == "n":
            break

    print("Thanks for playing!")

    save = {"beststreak": beststreak, "lost": lost, "won": won}
    with open(pathOfSaveFile, "w") as f:
        f.write(json.dumps(save, indent=2))

    

