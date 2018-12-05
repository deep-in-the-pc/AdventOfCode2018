def polymerReactor(string):
    oldString = ""
    while (oldString != string):
        oldString = string
        for i in range(65, 91):
            string = ''.join(string.split(chr(i) + chr(i + 32)))
            string = ''.join(string.split(chr(i + 32) + chr(i)))
    return string

with open("input_david.txt", "r") as fileline:
    inputs = [line.rstrip('\n') for line in fileline]
inputstring = inputs[0]

inputstringP1 = polymerReactor(inputstring)

print("Part One")
print(len(inputstringP1))

smallestPolymerLen = len(inputstring)

for i in range(65, 91):
    inputstringP2 = inputstring
    inputstringP2 = ''.join(inputstringP2.split(chr(i)))
    inputstringP2 = ''.join(inputstringP2.split(chr(i + 32)))
    inputstringP2 = polymerReactor(inputstringP2)
    if(smallestPolymerLen>len(inputstringP2)):
        smallestPolymerLen = len(inputstringP2)

print("Part Two")
print(smallestPolymerLen)