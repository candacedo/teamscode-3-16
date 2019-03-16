# hello world
# imports
import os

def main():
    path = "C:\\Users\\mketk\\Desktop\\SampleFiles\\"
    #path = "E:\\JudgeFiles\\"
    file = open(os.path.join(path, "wowordrd.txt"), "r")
    # word = file.read()
    # line = file.readLine()
    """
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)

    for i in range(numTimes):
        line = lines[i+1]
        numbers = line.split(" ")
        sum = 0
        for number in numbers:
            number = int(number.strip())
            sum += number
        print (sum)
    """
    alien(file)

def indexOf (str, word):
    for i in range (len(str)-len(word)):
        if word == str[i:i + len(word)]:
            return i

def alien(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numwords = int(numTimes)
    alien = lines[-1].strip()
    alien = alien[0].lower() + alien[1:]

    words = []
    for i in range (1, numwords + 1):
        words.append(lines[i].strip())
    sentence = []
    while not alien == "":
        for word in words:
            i = -1
            if word in alien:
                i = indexOf(alien, word)
            sentence.append(word)
            if i == 0:
                alien == ""
            else:
                newalien = alien[:i] + alien[i+len(word):]
                alien = newalien
                print (alien)

    original = ""
    for i in range (len(sentence)-1, 0, -1):
        original += sentence[i] + " "
    print (original)
"""
def structure(file):
    input = file.read()
    lines = input.split("\n")
    numLevels = lines[0].strip()
    numLevels = int(numLevels)
    damage = int(lines[-1].strip())

    building = []
    for i in range (1, numLevels + 1):
        level = lines[i].strip()
        newlevel = []
        for char in level:
            if not char == ".":
                num = int(char)
                if num - damage < 0:
                    newnum = 0
                else:
                    newnum = num - damage
                newlevel.append(str(newnum))
            elif char == ".":
                newlevel.append(char)
        building.append(newlevel)
    newbuilding = []
    for i in range (len(building)-1):
        level = building[i]
        newlevel = []
        for j in range (len(level)):
            if j == 0:
                if (building[i][j+1] in "0.") and (building[i+1][j] in "0.") and (building[i+1][j+1] in "0."):
                    newlevel.append("0")
            elif j == (len(level)-1):
                if (building[i][j-1] in "0.") and (building[i+1][j] in "0.") and (building[i+1][j-1] in "0."):
                    newlevel.append("0")
            else:
                if (building[i][j-1] in "0.") and (building[i][j+1] in "0.") and (building[i+1][j-1] in "0.") and (building[i+1][j] in "0.") and (building[i+1][j-1] in "0."):
                    newlevel.append("0")
        print (newlevel)

def shoe(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)
    passed = 1
    for i in range(1, numTimes+1):
        sortcounter = 0
        numpairs = int(lines[i].strip())
        unsorted = []
        for j in range(numpairs):
            left = lines[i + j + 1].strip().split(" ")[0]
            right = lines[i + j + 1].strip().split(" ")[1]
            if left != right:
                unsorted.append([left, right])
        for j in range(len(unsorted)):
            temp = ''
            quer = unsorted[j][1]
            for k in range(len(unsorted)):
                if unsorted[k][1] == quer:
                    temp = quer
                    unsorted[j][1] = unsorted[k][1]
                    unsorted[k][1] = temp
                    sortcounter += 1
        print(sortcounter)


def wowowrd(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)
    vocab = []
    for i in range(0, numTimes - 1):
        vocab.append(lines[0])

    alien = lines[numTimes]
    startind = -1
    endind = -2
    for i in range(len(alien)):


def art(file):
    input = file.read()
    lines = input.split("\n")
    key = "-AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz .:*"
    for i in range(len(lines)):
        line = lines[i].strip().split(" ")
        str = ""
        for i in range(len(line)):
            strnum = ""
            for char in line[i]:
                if char in "0123456789":
                    strnum += char
            num = int(strnum)
            str += key[num]
        print(str)

def boxp(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)

    for i in range(1, numTimes+1):
        line = lines[i]
        numbs = line.split(" ")
        #print(numbs)
        levs = int(numbs[0].strip()) # number of levels
        num = int(numbs[1].strip()) # number you want to find

        print (givelevel(num, levs))

def givelevel(num, levs):
    sum = 0
    count = 0
    for i in range (levs, 0, -1):
        count += 1
        if (sum + i) >= num:
            return count
        sum += i

        print ("number to find: " + str(num))
        foundlev = 1 # current level tracking
        for j in range(1, levs + 1):
            if num - j >= 0:
                num -= j
                #print (str(num + j) + " -> " + str(num) + ", " + "j: " + str(j))
                foundlev = j
        print("foundlev: " + str(foundlev))
        """
"""
def sletters(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)

    for i in range(numTimes):
        line = lines[i+1].strip()
        message = ""
        for i in range (len(line)):
            char = line[i]
            if not char in "abcd.":
                message += char
            elif char in ".":
                message += " "
            elif (not i == len(line)-1) and (char in "abcd") and (line[i+1] == char):
                message += char
        print (message)


def right(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)

    for i in range(numTimes):
        line = lines[i+1]
        strs = line.split(" ")
        numbers = []
        for str in strs:
            numbers.append(int(str))
        numbers.sort()

        ab = numbers[0]**2 + numbers[1]**2
        c = numbers[2]**2
        if ab == c:
            print ("right")
        else:
            print ("not right")


def reverse(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)

    for i in range (numTimes):
        newwords = []
        line = lines[i+1].strip()
        words = line.split(" ")
        for word in words:
            changed = reversefunc(word)
            newwords.append(changed)
        newsentence = ""
        for word in newwords:
            newsentence += word + " "
        print (newsentence)

def reversefunc(word): #for reverse()
    newword = ""
    for i in range (len(word)-1, -1, -1):
        newword += word[i]
    return newword


def notelength(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)

    for i in range (numTimes):
        total = 0
        line = lines[i+1].strip()
        for char in line:
            if char == "q":
                total += 1
            elif char == "h":
                total += 2
            elif char == "w":
                total += 4
        print (total)

def french(file):
    input = file.read()
    lines = input.split("\n")
    numTimes = lines[0].strip()
    numTimes = int(numTimes)

    for i in range (numTimes):
        newwords = []
        line = lines[i+1].strip()
        words = line.split(" ")
        for word in words:
            changed = word
            if not len(word) == 1:
                if (len(word) > 2) and (word[0] == "h"):
                    changed = changed[1:]
                if not changed[-1] in "clfr":
                    changed = changed[:-1]
            newwords.append(changed)
        newsentence = ""
        for word in newwords:
            newsentence += word + " "
        print (newsentence)

def owl():
    print(" /\\______/\\")
    print("| (o) __(o)|")
    print("|     \\/   |")
    print("/\"\"\"\"\"\"\"\"\"\"\\")
    print("." * 12)
    print("\\" + ("." * 10) + "/")
    print("/___  __  _\\")
    print("    \\\\   \\\\")
"""
if __name__ == "__main__":
    main()
