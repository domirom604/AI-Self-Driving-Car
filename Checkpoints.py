class Checkpoint:
    def __init__(self,pos,type):
        self.pos = pos
        self.type = type
        self.reached = False

    def getCoord(self,cols):
        self.coords = []
        if self.type == "H":
            x = self.pos[0]
            Y = self.pos[1]
            while 1:
                if [x,Y] in cols:
                    break
                else:
                    self.coords.append([x,Y])
                    x += 1
            x = self.pos[0]
            Y = self.pos[1]
            while 1:
                if [x, Y] in cols:
                    break
                else:
                    self.coords.append([x, Y])
                    x -= 1
        if self.type == "V":
            X = self.pos[0]
            y = self.pos[1]
            while 1:
                if [X, y] in cols:
                    break
                else:
                    self.coords.append([X, y])
                    y += 1
            X = self.pos[0]
            y = self.pos[1]
            while 1:
                if [X, y] in cols:
                    break
                else:
                    self.coords.append([X, y])
                    y -= 1


class Checkpoints:
    def __init__(self,screen,cols,car):
        self.screen = screen
        self.cols = cols
        self.car = car
        self.coordinates = []
        for i in range(12):
            self.coordinates.append([[260+((i+1)*100),230],"V"])
        self.coordinates.append([[1550,400],"H"])
        self.coordinates.append([[1550, 500], "H"])
        for i in range(5):
            self.coordinates.append([[270+((i+1)*100),700],"V"])
        for i in range(6):
            self.coordinates.append([[770+((i+1)*100),535],"V"])
        self.coordinates.append([[1470, 550], "V"])
        self.coordinates.append([[200, 550], "H"])
        self.coordinates.append([[200, 650], "H"])
        self.coordinates.append([[200, 470], "H"])

        self.checkpoints = []
        for coord in self.coordinates:
            self.checkpoints.append(Checkpoint(pos=coord[0],type=coord[1]))
        for checkpoint in self.checkpoints:
            checkpoint.getCoord(self.cols)

    def checkReache(self,carXY):
        carXY = [int(carXY[0]),int(carXY[1])]
        for checkpoint in self.checkpoints:
            if carXY in checkpoint.coords and checkpoint.reached == False:
                checkpoint.reached = True
                self.car.score += 1

            all_reached = True
            for checkpoint in self.checkpoints:
                if checkpoint.reached == False:
                    all_reached = False
            if all_reached == True:
                for checkpoint in self.checkpoints:
                    checkpoint.reached = False

    def render(self):
        for checkpoint in self.checkpoints:
            for coord in checkpoint.coords:
                if checkpoint.reached == True:
                    color = (0,255,0)
                else:
                    color = (255,0,0)
                self.screen.set_at(coord, color)