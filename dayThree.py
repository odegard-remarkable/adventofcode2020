# ratinal number 3|1
# Start top left corner, =1
# move 3 right, 1 down, continue
# Count trees you hit in the way

def splitString(line):
    line = line.rstrip("\n")
    return [char for char in line]

def findTree(character):
    if character == '#':
        return 1
    else:
        return 0

def getSlope()
    with open("./resource/slopes.txt", "r") as f:
        for line in f:
            sideway = line[0]
            down = line [1]


slopes = []

rightMove = 1
sideway = 0
down = 0
trees = 0
l = 1

with open("./resource/daythreeslope.txt","r") as f:
    for line in f:
        x = splitString(line)
        chars = len(x)

        if l != 1:
            rightMove += 3

        if rightMove > chars:
            rightMove = rightMove % chars

            #Only for debugging
            print("index: ", rightMove, " ", x[rightMove])

        trees += findTree(x[rightMove-1])
        print("line:", l, "index:", rightMove,"trees", trees, "symbol:", x[rightMove-1])
        
        #Only for debugging
        l += 1

        