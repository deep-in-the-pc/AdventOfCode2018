

flag = 1
frequency = 0
nFrequency = set()
count = 0
while(flag):
    numberfile = open("inputnardo.txt", "r")
    for i in numberfile:
        n = int(i)
        frequency += n
        if(frequency in nFrequency):
            print(str(frequency)+" is old and it was the "+ str(count) + " time it was added")
            flag = 0
            exit()
        else:
            count += 1
            nFrequency.add(frequency)
            #print(str(frequency) + " is new")