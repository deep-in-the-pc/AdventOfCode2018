def lineCompare(testline, testedline):
    fails = 0
    failpos = 0
    for i in range(len(testLine)):
        if testline[i] != testedline[i]:
            fails += 1
            failpos = i
    if fails == 1:
        return failpos
    else:
        return 0


TWOs = 0
THREEs = 0
FFLAG = 0;
charperline = set()

numberfile = open("input_david.txt", "r")
lineList = numberfile.readlines()

for i in range(len(lineList)):
    testLine = lineList[i]
    for n in range(i, len(lineList)):
        fp = lineCompare(testLine, lineList[n])
        if fp:
            finalid = testLine[:fp] + testLine[(fp+1):]
            print(finalid)
