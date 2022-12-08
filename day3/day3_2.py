# solution by @dualjk and @tirannosario

items = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 

def sumPriorities():
    sum = 0
    rucksack_file = open("input.txt", 'r')
    linesReaded = 0
    i = 0
    groups = []
    for line in rucksack_file.readlines():
        if(linesReaded==0):
            groups.append([list(set(line))])
        else:
            groups[i].append(list(set(line)))
        linesReaded += 1
        if(linesReaded==3):
            # # find group item
            occurrences = {}
            for elf in groups[i]:
                for c in elf:
                    if c != "\n":
                        if occurrences.get(c) != None:
                            occurrences[c]+=1
                        else:
                            occurrences[c] = 1 
            duplicates = [items.index(dup)+1 for dup in [x for x in occurrences.keys() if occurrences[x] == 3]]
            sum += duplicates[0] if len(duplicates) > 0 else 0

            # clean cycle var
            linesReaded = 0
            i+=1
    print(sum)

if __name__ == "__main__":
    sumPriorities()