

def checkWin(opp, you):
    if (opp == 'C' and you == 'X') or (opp == 'B' and you == 'Z') or (opp == 'A' and you == 'Y'):
        return 6
    elif (opp == 'A' and you == 'X') or (opp == 'B' and you == 'Y') or (opp == 'C' and you == 'Z'):
        return 3
    else:
        return 0


def checkSign(sign):
    if sign == 'X':
        return 1
    elif sign == 'Y':
        return 2
    else:
        return 3


def checkWin2(sign):
    if sign == 'X':
        return 0
    elif sign == 'Y':
        return 3
    else:
        return 6

def checkSign2(opp, res):
    if res == "X":
        if opp == "A":
            return 3
        elif opp == "B":
            return 1
        else:
            return 2
    elif res == "Y":
        if opp == "A":
            return 1
        elif opp == "B":
            return 2
        elif opp =="C":
            return 3
    elif res == "Z":
        if opp == "A":
            return 2
        elif opp == "B":
            return 3
        elif opp == "C":
            return 1

sum =0

h = open("Luke2input.txt", "r")
content = h.readlines()


#for line in content:
#    (key, value) = line.split(' ')
#    sum = sum + checkWin(key, value[0]) + checkSign(value[0])

for line in content:
    (key, value) = line.split(' ')
    sum = sum + checkSign2(key, value[0]) + checkWin2(value[0])

print(sum)