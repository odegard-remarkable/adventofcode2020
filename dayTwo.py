import re
import time

def splitString(line):
    return [char for char in line]

def findValidPasswords():
    start_time = time.time()
    countValid = 0

    with open("./resource/daytwoPasswords.txt","r") as f:
        for line in f:
            rawLine = re.match("([0-9]+)-([0-9]+) ([^:]+): ([^\n$]+)", line).groups()
            n1 = int(rawLine[0])
            n2 = int(rawLine[1])
            letter = rawLine[2]
            password = rawLine[3]

            if password.count(letter) >= n1 and password.count(letter) <= n2:
                countValid += 1

    end_time = time.time()
    run_time = end_time-start_time

    return(countValid, run_time)

def findValidPasswordsUpdated():
    start_time = time.time()
    countValid = 0

    with open("./resource/daytwoPasswords.txt","r") as f:
        for line in f:
            rawLine = re.match("([0-9]+)-([0-9]+) ([^:]+): ([^\n$]+)", line).groups()
            n1 = int(rawLine[0])
            n2 = int(rawLine[1])
            letter = rawLine[2]
            password = rawLine[3]

            dictonary = splitString(password)

            if dictonary[n1-1] == letter and dictonary[n2-1] != letter:
                countValid += 1
            elif dictonary[n1-1] != letter and dictonary[n2-1] == letter:
                countValid += 1
            else:
                print("nothing")

    end_time = time.time()
    run_time = end_time-start_time

    return(countValid, run_time)

print(findValidPasswords())
print(findValidPasswordsUpdated())