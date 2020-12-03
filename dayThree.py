# ratinal number 3|1
# Start top left corner, =1
# move 3 right, 1 down, continue
# Count trees you hit in the way

import re

def splitString(line):
    line = line.rstrip("\n")
    return [char for char in line]

def findTree(character):
    if character == '#':
        return 1
    else:
        return 0
    
slopes = []
rightMove = 1
sideway = 0
down = 0
trees = 0
l = 1

with open("./resource/daythreeslope.txt","r") as slope:
    with open("./resource/slopes.txt", "r") as paths:
        for path in paths:
            path = re.match("([0-9]+),([0-9]+)", path).groups()
            sideway = int(path[0])
            down = int(path[1])
            print(sideway,down)
            for line in slope:
                x = splitString(line)
                chars = len(x)

                if l != 1:
                    rightMove += sideway

                if rightMove > chars:
                    rightMove = rightMove % chars

                    #Only for debugging
                    #print("index: ", rightMove, " ", x[rightMove])

                trees += findTree(x[rightMove-1])
                #print("line:", l, "index:", rightMove,"trees", trees, "symbol:", x[rightMove-1])

                #Only for debugging
                l += 1
        print(trees)
                

        