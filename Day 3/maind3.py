import numpy

with open("input_david.txt", "r") as fileline:
    inputs = [line.rstrip('\n') for line in fileline]

class fabric():
    def __init__(self, *args, **kwargs):
        self.AllFabricPieces = list()
        self.MaxX = 0
        self.MaxY = 0
        for i in args[0]:
            fp = fabricpiece(i.split(' @')[0][1:],
            i.split(' @ ')[1].split(",")[0],
            i.split(' @ ')[1].split(",")[1].split(": ")[0],
            i.split(' @ ')[1].split(",")[1].split(": ")[1].split("x")[0],
            i.split(' @ ')[1].split(",")[1].split(": ")[1].split("x")[1])
            self.AllFabricPieces.append(fp)
        self.MaxX = self.findMaxX()
        self.MaxY = self.findMaxY()
        self.CompleteFabric = numpy.zeros((self.MaxX, self.MaxY))

    def findMaxX(self):
        maxX = 0
        for i in self.AllFabricPieces:
            if(i.posx+i.width > maxX):
                maxX = i.posx+i.width
        return maxX
    def findMaxY(self):
        maxY = 0

        for i in self.AllFabricPieces:
            if(i.posy+i.heigth > maxY):
                maxY = i.posy+i.heigth
        return maxY
    def patchFabric(self):
        count = 0
        for i in self.AllFabricPieces:
            overlap = 0
            for y in range(i.heigth):
                for x in range(i.width):
                    #print(i.posy+y, i.posx+x)
                    if self.CompleteFabric[i.posy+y][i.posx+x] < 2:
                        self.CompleteFabric[i.posy + y][i.posx + x]+=1
                        if self.CompleteFabric[i.posy + y][i.posx + x]==2:
                            count+=1
        for i in self.AllFabricPieces:
            overlap = 0
            for y in range(i.heigth):
                for x in range(i.width):
                    # print(i.posy+y, i.posx+x)
                    if self.CompleteFabric[i.posy + y][i.posx + x] == 2:
                        overlap = 1
                        break
            if overlap == 0:
                print("this one didn't overlap  " + str(i.id))
        numpy.savetxt('test.txt', self.CompleteFabric, fmt='%d')

        return count
class fabricpiece():
    def __init__(self, id, posx, posy, width, heigth):

        self.id = int(id)
        self.posx = int(posx)
        self.posy = int(posy)
        self.width = int(width)
        self.heigth = int(heigth)



day3 = fabric(inputs, size=len(inputs))

print(day3.patchFabric())