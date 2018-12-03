TWOs = 0
THREEs = 0
FFLAG = 0;
charperline = set()

numberfile = open("input_david.txt", "r")
for i in numberfile:
    print("NSTART\n"+i)
    for c in i:
        if(i.count(c)==2 and not (FFLAG & 0b00000001)):
            TWOs+=1
            FFLAG |= 0b00000001
            print(c)
        elif(i.count(c)==3 and not (FFLAG & 0b00000010)):
            THREEs+=1
            FFLAG |= 0b00000010
            print(c)
    FFLAG = 0

print(str(TWOs) +"x"+ str(THREEs)+"="+str(TWOs*THREEs))