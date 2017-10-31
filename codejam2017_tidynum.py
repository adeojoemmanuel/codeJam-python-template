import sys
OCC = 1

fileContent = open("B-small-practice.in", "r")
writeFile = open("output.txt", "w")

for line in fileContent:
        currentLine = int(line)
        for i in range(currentLine):
                val = list(str(i))
                mainSort = (int(e) for e in val)
                newData = sorted(mainSort)
                list1 = ''.join(str(v) for v in newData)

        print("Case #{}: {}".format(OCC, list1))
        writeFile.write("Case #{}: {}".format(OCC, newData) + '\n')

        OCC += 1
