elfkcal = []
elftmp = 0

h = open("inputtext.txt", "r")
content = h.readlines()

for line in content:
    if line.strip():
        elftmp=elftmp+int(line)
    else:
        elfkcal.append(elftmp)
        elftmp = 0


k = sorted(elfkcal, reverse=True)

print(k[0]+k[1]+k[2])