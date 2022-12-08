
plus = {"A":[3,1,2], "B":[1,2,3], "C":[2,3,1]}
assignment = {"X":0, "Y":1, "Z":2}
rules={"X":0, "Y":3, "Z":6}

def totalScore():
    game_score = 0
    game_file = open("input.txt", 'r')
    for game in game_file.readlines():
        p1,p2 = game.split(" ")
        print("Game round " + p1 + " vs " + p2 + ":" + str(plus[p1][assignment[p2.strip()]] + rules[p2.strip()]))
        game_score += plus[p1][assignment[p2.strip()]] + rules[p2.strip()]
    print("game score: ", game_score)


if __name__ == "__main__":
    totalScore()