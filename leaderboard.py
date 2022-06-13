import json


class LeaderBoard:
    def __init__(self, content=None) -> None:
        if content:
            self.leaderboard = content["leaderboard"]
            self.sort()
        else:
            self.leaderboard = {}
    
    def sort(self):
        self.leaderboard = dict(sorted(self.leaderboard.items(), key=lambda item: item[1]))

    
    def print(self):
        for player in self.leaderboard:
            print(player + self.leaderboard[player], sep=" ", end="\n")
    
    def add_score(self, name, score):
        self.leaderboard[name] = score
        self.sort()
    
    def getLeaderBoard(self) -> dict:
        return self.leaderboard