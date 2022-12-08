# solution by @dualjk and @tirannosario

rules = {"A":[3,6,0], "B":[0,3,6], "C":[6,0,3]}
assignment = {"X":1, "Y":2, "Z":3}

def totalScore():
    game_score = 0
    game_file = open("input.txt", 'r')
    for game in game_file.readlines():
        p1,p2 = game.split(" ")
        game_score += assignment[p2.strip()] + rules[p1][assignment[p2.strip()]-1]
    print("game score: ", game_score)


if __name__ == "__main__":
    totalScore()