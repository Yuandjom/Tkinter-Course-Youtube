import re

#Extracting Digits and Summing them
TheFile = open("work.txt")
numberlist = []

for line in TheFile:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = float(extract[i])
        numberlist.append(num)

print(sum(numberlist))