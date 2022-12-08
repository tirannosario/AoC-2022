# solution by @dualjk and @tirannosario

def checkAssignments():
    count_contain = 0
    pair_file = open("input.txt", 'r')
    for pair in pair_file.readlines():
        r1,r2 = pair.split(",")
        r11,r12 = [int(x) for x in r1.split("-")]
        r21,r22 = [int(x) for x in r2.split("-")]
        if (r11 >= r21 and r12<=r22) or (r21 >= r11 and r22<=r12):
            count_contain += 1
    print(count_contain)
        


if __name__ == "__main__":
    checkAssignments()