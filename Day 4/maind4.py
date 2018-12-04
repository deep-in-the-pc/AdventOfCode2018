class guard():

    def __init__(self, id):
        self.id = id
        self.minutesAsleep = [0] * 60
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.id == other.id

    def addSleep(self, sleepStart, sleepEnd):

        for i in range(int(sleepStart.split(":")[1][:2]), int(sleepEnd.split(":")[1][:2])):
            self.minutesAsleep[i]+=1

with open("input_david.txt", "r") as fileline:
    inputs = [line.rstrip('\n') for line in fileline]

inputs.sort()
guardSet = set()
guardList = []
linecount = 0
guardLinesList = []
for line in inputs:
    if (line.find("Guard #") != -1):
        guardLinesList.append(linecount)
    linecount+=1
linecount = 0
for line in inputs:

    if(line.find("Guard #")!=-1):
        guardIDobject = guard(int(line[26:].split(" ")[0]))
        guardID = int(line[26:].split(" ")[0])
        if(not guardIDobject in guardSet):
            newGuard = guard(int(line[26:].split(" ")[0]))
            guardSet.add(newGuard)
            guardList.append(newGuard)
        for x in guardList:
            if x.id == guardID:
                if(linecount!=999):
                    for i in range(guardLinesList[guardLinesList.index(linecount)]+1, guardLinesList[guardLinesList.index(linecount)+1], 2):
                        x.addSleep(inputs[i], inputs[i+1])
                else:
                    x.addSleep(inputs[1000], inputs[1001])



    linecount += 1

maxSleeptimeP1 = 0
maxSleepinminIndexP1 = 0
maxSleepinminIDP1 = 0

maxSleeptimeP2 = 0
maxSleepinminIndexP2 = 0
maxSleepinminIDP2 = 0

for nguard in guardList:

    if (maxSleeptimeP2 < max(nguard.minutesAsleep)):
        maxSleeptimeP2 = max(nguard.minutesAsleep)
        maxSleepinminIndexP2 = nguard.minutesAsleep.index(max(nguard.minutesAsleep))
        maxSleepinminIDP2 = nguard.id

    if(maxSleeptimeP1<sum(nguard.minutesAsleep)):
        maxSleeptimeP1 = sum(nguard.minutesAsleep)
        maxSleepinminIndexP1 = nguard.minutesAsleep.index(max(nguard.minutesAsleep))
        maxSleepinminIDP1 = nguard.id



print("Part One")
print(str(maxSleepinminIndexP1) + "x" + str(maxSleepinminIDP1) + "=" + str(maxSleepinminIndexP1 * maxSleepinminIDP1))

print("Part Two")
print(str(maxSleepinminIndexP2) + "x" + str(maxSleepinminIDP2) + "=" + str(maxSleepinminIndexP2 * maxSleepinminIDP2))