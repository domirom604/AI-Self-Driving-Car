import pygame
import math
import numpy as np

def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points


class Car:
    def __init__(self,x,y,screen,cols,collisions,model=None):
        vec = pygame.math.Vector2
        self.cols = cols
        self.collisions = collisions
        self.sensor_mid = 0
        self.sensor_left = 0
        self.sensor_right = 0
        self.score = 0
        self.x = x
        self.y = y

        self.xend = x
        self.yend = y

        self.xend1 = x
        self.yend1 = y

        self.xend2 = x
        self.yend2 = y

        self.xA = x
        self.yA = y

        self.xB = x
        self.yB = y

        self.xC = x
        self.yC = y

        self.xD = x
        self.yD = y

        self.xAB = []
        self.yAB = []

        self.xBC = []
        self.yBC = []

        self.xCD = []
        self.yCD = []

        sensor_length = 120
        self.length_obstacle_detector = sensor_length
        self.length_obstacle_detector_right = sensor_length
        self.length_obstacle_detector_left = sensor_length
        self.length_car = 44
        self.length_car_one = 79
        self.length_car_two = 40

        self.car_edge_to_detect_colision =[]
        self.screen = screen
        self.car_image_rotate = pygame.image.load("car1.png").convert_alpha()
        self.angle = 90
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.vel = vec(self.x, self.y)
        self.keyW_ispressed=0
        self.velocity = 1
        self.model = model

    def player_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.keyW_ispressed==1:
            if (self.angle > 360):
                self.angle = 0
            self.angle+=self.velocity/2

            self.xAB = []
            self.yAB = []

            self.xBC = []
            self.yBC = []

            self.xCD = []
            self.yCD = []

            self.xend = self.x + math.cos(math.radians(-self.angle+90)) * self.length_obstacle_detector
            self.yend = self.y + math.sin(math.radians(-self.angle+90)) * self.length_obstacle_detector

            self.xend1 = self.x + math.cos(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right
            self.yend1 = self.y + math.sin(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right

            self.xend2 = self.x + math.cos(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left
            self.yend2 = self.y + math.sin(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left

            self.xA = self.x + math.cos(math.radians(-self.angle -63)) * self.length_car
            self.yA = self.y + math.sin(math.radians(-self.angle -63)) * self.length_car

            self.xB = self.x + math.cos(math.radians(-self.angle + 63)) * self.length_car
            self.yB = self.y + math.sin(math.radians(-self.angle + 63)) * self.length_car

            self.xC = self.x + math.cos(math.radians(-self.angle + 117)) * self.length_car
            self.yC = self.y + math.sin(math.radians(-self.angle + 117)) * self.length_car

            self.xD = self.x + math.cos(math.radians(-self.angle - 117)) * self.length_car
            self.yD = self.y + math.sin(math.radians(-self.angle - 117)) * self.length_car

            for i in range (self.length_car_one):
                self.xAB .append (self.xA + math.cos(math.radians(-self.angle +90)) * i)
                self.yAB  .append(self.yA + math.sin(math.radians(-self.angle +90)) * i)

            for i in range (self.length_car_two):
                self.xBC .append (self.xB + math.cos(math.radians(-self.angle +180)) * i)
                self.yBC .append(self.yB + math.sin(math.radians(-self.angle +180)) * i)

            for i in range(self.length_car_one):
                self.xCD.append(self.xC + math.cos(math.radians(-self.angle + 270)) * i)
                self.yCD.append(self.yC + math.sin(math.radians(-self.angle + 270)) * i)

            # self.xend = self.x + math.cos(math.radians(self.angle)) * self.length
            # self.yend = self.y + math.sin(math.radians(self.angle)) * self.length

            #print(self.angle)
        if keys[pygame.K_a] and self.keyW_ispressed==1:
            if (self.angle<0):
                self.angle=360

            self.xAB = []
            self.yAB = []

            self.xBC = []
            self.yBC = []

            self.xCD = []
            self.yCD = []

            self.xend = self.x + math.cos(math.radians(-self.angle+90)) * self.length_obstacle_detector
            self.yend = self.y + math.sin(math.radians(-self.angle+90)) * self.length_obstacle_detector

            self.xend1 = self.x + math.cos(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right
            self.yend1 = self.y + math.sin(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right

            self.xend2 = self.x + math.cos(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left
            self.yend2 = self.y + math.sin(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left

            self.xA = self.x + math.cos(math.radians(-self.angle - 63)) * self.length_car
            self.yA = self.y + math.sin(math.radians(-self.angle - 63)) * self.length_car

            self.xB = self.x + math.cos(math.radians(-self.angle + 63)) * self.length_car
            self.yB = self.y + math.sin(math.radians(-self.angle + 63)) * self.length_car

            self.xC = self.x + math.cos(math.radians(-self.angle + 117)) * self.length_car
            self.yC = self.y + math.sin(math.radians(-self.angle + 117)) * self.length_car

            self.xD = self.x + math.cos(math.radians(-self.angle - 117)) * self.length_car
            self.yD = self.y + math.sin(math.radians(-self.angle - 117)) * self.length_car

            for i in range (self.length_car_one):
                self.xAB .append (self.xA + math.cos(math.radians(-self.angle +90)) * i)
                self.yAB  .append(self.yA + math.sin(math.radians(-self.angle +90)) * i)

            for i in range (self.length_car_two):
                self.xBC .append (self.xB + math.cos(math.radians(-self.angle +180)) * i)
                self.yBC .append(self.yB + math.sin(math.radians(-self.angle +180)) * i)

            for i in range(self.length_car_one):
                self.xCD.append(self.xC + math.cos(math.radians(-self.angle + 270)) * i)
                self.yCD.append(self.yC + math.sin(math.radians(-self.angle + 270)) * i)

            self.angle-=self.velocity/2


        if keys[pygame.K_w]:

            self.xAB = []
            self.yAB = []

            self.xBC = []
            self.yBC = []

            self.xCD = []
            self.yCD = []

            self.keyW_ispressed=1
            self.x += math.sin(self.angle * 0.0174532925 )*self.velocity
            self.y += math.cos(self.angle * 0.0174532925 )*self.velocity

            self.xend = self.x + math.cos(math.radians(-self.angle+90)) * self.length_obstacle_detector
            self.yend = self.y + math.sin(math.radians(-self.angle+90)) * self.length_obstacle_detector

            self.xend1 = self.x + math.cos(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right
            self.yend1 = self.y + math.sin(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right

            self.xend2 = self.x + math.cos(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left
            self.yend2 = self.y + math.sin(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left

            self.xA = self.x + math.cos(math.radians(-self.angle - 63)) * self.length_car
            self.yA = self.y + math.sin(math.radians(-self.angle - 63)) * self.length_car

            self.xB = self.x + math.cos(math.radians(-self.angle + 63)) * self.length_car
            self.yB = self.y + math.sin(math.radians(-self.angle + 63)) * self.length_car

            self.xC = self.x + math.cos(math.radians(-self.angle + 117)) * self.length_car
            self.yC = self.y + math.sin(math.radians(-self.angle + 117)) * self.length_car

            self.xD = self.x + math.cos(math.radians(-self.angle - 117)) * self.length_car
            self.yD = self.y + math.sin(math.radians(-self.angle - 117)) * self.length_car

            for i in range (self.length_car_one):
                self.xAB .append (self.xA + math.cos(math.radians(-self.angle +90)) * i)
                self.yAB  .append(self.yA + math.sin(math.radians(-self.angle +90)) * i)

            for i in range (self.length_car_two):
                self.xBC .append (self.xB + math.cos(math.radians(-self.angle +180)) * i)
                self.yBC .append(self.yB + math.sin(math.radians(-self.angle +180)) * i)

            for i in range(self.length_car_one):
                self.xCD.append(self.xC + math.cos(math.radians(-self.angle + 270)) * i)
                self.yCD.append(self.yC + math.sin(math.radians(-self.angle + 270)) * i)

            #print("angle:",self.angle)
            #print(self.x, " ", self.y)
            #print(self.x+20, " ", self.y+40)

            #print(self.y)
        else :
            self.keyW_ispressed = 0

    def keras_control(self):
        if 1:
            self.xAB = []
            self.yAB = []

            self.xBC = []
            self.yBC = []

            self.xCD = []
            self.yCD = []

            self.keyW_ispressed=1
            self.x += math.sin(self.angle * 0.0174532925 )*self.velocity
            self.y += math.cos(self.angle * 0.0174532925 )*self.velocity

            self.xend = self.x + math.cos(math.radians(-self.angle+90)) * self.length_obstacle_detector
            self.yend = self.y + math.sin(math.radians(-self.angle+90)) * self.length_obstacle_detector

            self.xend1 = self.x + math.cos(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right
            self.yend1 = self.y + math.sin(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right

            self.xend2 = self.x + math.cos(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left
            self.yend2 = self.y + math.sin(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left

            self.xA = self.x + math.cos(math.radians(-self.angle - 63)) * self.length_car
            self.yA = self.y + math.sin(math.radians(-self.angle - 63)) * self.length_car

            self.xB = self.x + math.cos(math.radians(-self.angle + 63)) * self.length_car
            self.yB = self.y + math.sin(math.radians(-self.angle + 63)) * self.length_car

            self.xC = self.x + math.cos(math.radians(-self.angle + 117)) * self.length_car
            self.yC = self.y + math.sin(math.radians(-self.angle + 117)) * self.length_car

            self.xD = self.x + math.cos(math.radians(-self.angle - 117)) * self.length_car
            self.yD = self.y + math.sin(math.radians(-self.angle - 117)) * self.length_car

            for i in range (self.length_car_one):
                self.xAB .append (self.xA + math.cos(math.radians(-self.angle +90)) * i)
                self.yAB  .append(self.yA + math.sin(math.radians(-self.angle +90)) * i)

            for i in range (self.length_car_two):
                self.xBC .append (self.xB + math.cos(math.radians(-self.angle +180)) * i)
                self.yBC .append(self.yB + math.sin(math.radians(-self.angle +180)) * i)

            for i in range(self.length_car_one):
                self.xCD.append(self.xC + math.cos(math.radians(-self.angle + 270)) * i)
                self.yCD.append(self.yC + math.sin(math.radians(-self.angle + 270)) * i)

        sensors = [self.collisions.colision_detection(self.cols, self.line_left),
                   self.collisions.colision_detection(self.cols, self.line_mid),
                   self.collisions.colision_detection(self.cols, self.line_right)]
        m = []
        for s in sensors:
            if s == 1:
                m.append(0)
            if s == 2:
                m.append(1)
        sensors = m
        sensors = np.asarray([sensors])
        #print(sensors)
        result = self.model.predict(sensors,verbose=0)
        result = list(result)
        result = list(result[0])
        #print(result)
        if result.index(max(result)) == 0: # w lewo
            if (self.angle > 360):
                self.angle = 0
            self.angle += self.velocity / 2

            self.xAB = []
            self.yAB = []

            self.xBC = []
            self.yBC = []

            self.xCD = []
            self.yCD = []

            self.xend = self.x + math.cos(math.radians(-self.angle + 90)) * self.length_obstacle_detector
            self.yend = self.y + math.sin(math.radians(-self.angle + 90)) * self.length_obstacle_detector

            self.xend1 = self.x + math.cos(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right
            self.yend1 = self.y + math.sin(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right

            self.xend2 = self.x + math.cos(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left
            self.yend2 = self.y + math.sin(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left

            self.xA = self.x + math.cos(math.radians(-self.angle - 63)) * self.length_car
            self.yA = self.y + math.sin(math.radians(-self.angle - 63)) * self.length_car

            self.xB = self.x + math.cos(math.radians(-self.angle + 63)) * self.length_car
            self.yB = self.y + math.sin(math.radians(-self.angle + 63)) * self.length_car

            self.xC = self.x + math.cos(math.radians(-self.angle + 117)) * self.length_car
            self.yC = self.y + math.sin(math.radians(-self.angle + 117)) * self.length_car

            self.xD = self.x + math.cos(math.radians(-self.angle - 117)) * self.length_car
            self.yD = self.y + math.sin(math.radians(-self.angle - 117)) * self.length_car

            for i in range(self.length_car_one):
                self.xAB.append(self.xA + math.cos(math.radians(-self.angle + 90)) * i)
                self.yAB.append(self.yA + math.sin(math.radians(-self.angle + 90)) * i)

            for i in range(self.length_car_two):
                self.xBC.append(self.xB + math.cos(math.radians(-self.angle + 180)) * i)
                self.yBC.append(self.yB + math.sin(math.radians(-self.angle + 180)) * i)

            for i in range(self.length_car_one):
                self.xCD.append(self.xC + math.cos(math.radians(-self.angle + 270)) * i)
                self.yCD.append(self.yC + math.sin(math.radians(-self.angle + 270)) * i)

            # self.xend = self.x + math.cos(math.radians(self.angle)) * self.length
            # self.yend = self.y + math.sin(math.radians(self.angle)) * self.length

            # print(self.angle)
        if result.index(max(result)) == 1: # w prawo
            if (self.angle < 0):
                self.angle = 360

            self.xAB = []
            self.yAB = []

            self.xBC = []
            self.yBC = []

            self.xCD = []
            self.yCD = []

            self.xend = self.x + math.cos(math.radians(-self.angle + 90)) * self.length_obstacle_detector
            self.yend = self.y + math.sin(math.radians(-self.angle + 90)) * self.length_obstacle_detector

            self.xend1 = self.x + math.cos(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right
            self.yend1 = self.y + math.sin(math.radians(-self.angle + 125)) * self.length_obstacle_detector_right

            self.xend2 = self.x + math.cos(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left
            self.yend2 = self.y + math.sin(math.radians(-self.angle + 55)) * self.length_obstacle_detector_left

            self.xA = self.x + math.cos(math.radians(-self.angle - 63)) * self.length_car
            self.yA = self.y + math.sin(math.radians(-self.angle - 63)) * self.length_car

            self.xB = self.x + math.cos(math.radians(-self.angle + 63)) * self.length_car
            self.yB = self.y + math.sin(math.radians(-self.angle + 63)) * self.length_car

            self.xC = self.x + math.cos(math.radians(-self.angle + 117)) * self.length_car
            self.yC = self.y + math.sin(math.radians(-self.angle + 117)) * self.length_car

            self.xD = self.x + math.cos(math.radians(-self.angle - 117)) * self.length_car
            self.yD = self.y + math.sin(math.radians(-self.angle - 117)) * self.length_car

            for i in range(self.length_car_one):
                self.xAB.append(self.xA + math.cos(math.radians(-self.angle + 90)) * i)
                self.yAB.append(self.yA + math.sin(math.radians(-self.angle + 90)) * i)

            for i in range(self.length_car_two):
                self.xBC.append(self.xB + math.cos(math.radians(-self.angle + 180)) * i)
                self.yBC.append(self.yB + math.sin(math.radians(-self.angle + 180)) * i)

            for i in range(self.length_car_one):
                self.xCD.append(self.xC + math.cos(math.radians(-self.angle + 270)) * i)
                self.yCD.append(self.yC + math.sin(math.radians(-self.angle + 270)) * i)

            self.angle -= self.velocity / 2

    def render(self,x,y):

        self.car_image = pygame.transform.rotate(self.car_image_rotate, self.angle)

        #self.line=pygame.draw.lines(self.screen, self.red, True, [(20+self.x, 40+self.y), (self.xend,self.yend)], 1)

        self.line_mid = get_line(x1=int(self.x + 20), y1=int(self.y + 40), x2=int(self.xend + 20),y2=int(self.yend + 40))
        color = (255, 0, 0)
        self.sensor_mid = 0
        if (self.collisions.colision_detection(self.cols, self.line_mid) == 1):
            color = (0, 0, 255)
            self.sensor_mid = 1
        pygame.draw.line(self.screen, color, (self.x + 20,self.y+40), (self.xend+20, self.yend+40), 1)

        self.line_right = get_line(x1=int(self.x + 20), y1=int(self.y + 40), x2=int(self.xend1 + 20),y2=int(self.yend1 + 40))
        color = (255, 0, 0)
        self.sensor_right = 0
        if (self.collisions.colision_detection(self.cols, self.line_right) == 1):
            color = (0, 0, 255)
            self.sensor_right = 1
        pygame.draw.line(self.screen, color, (self.x + 20, self.y + 40), (self.xend1 + 20, self.yend1 + 40), 1)

        self.line_left = get_line(x1=int(self.x + 20), y1=int(self.y + 40), x2=int(self.xend2 + 20),y2=int(self.yend2 + 40))
        color = (255, 0, 0)
        self.sensor_left = 0
        if (self.collisions.colision_detection(self.cols, self.line_left) == 1):
            color = (0, 0, 255)
            self.sensor_left = 0
        pygame.draw.line(self.screen, color, (self.x + 20, self.y + 40), (self.xend2 + 20, self.yend2 + 40), 1)
        pygame.draw.line(self.screen, self.red, (self.x + 20, self.y + 40), (self.xA + 20, self.yA + 40), 1)
        pygame.draw.line(self.screen, self.red, (self.x + 20, self.y + 40), (self.xC + 20, self.yC + 40), 1)
        pygame.draw.line(self.screen, self.red, (self.x + 20, self.y + 40), (self.xB + 20, self.yB + 40), 1)
        pygame.draw.line(self.screen, self.red, (self.x + 20, self.y + 40), (self.xD + 20, self.yD + 40), 1)


        #pygame.draw.line(self.screen, self.red, (self.xA + 20, self.yA + 40), (self.xB + 20, self.yB + 40), 1)
        #pygame.draw.line(self.screen, self.red, (self.xB + 20, self.yB + 40), (self.xC + 20, self.yC + 40), 1)
        #pygame.draw.line(self.screen, self.red, (self.xD + 20, self.yD + 40), (self.xC + 20, self.yC + 40), 1)


        #pygame.draw.line(self.screen, self.red, (20+self.x, 40+self.y), (self.xend, self.yend), 1)

        self.car_image1 = self.car_image.get_rect(center=self.car_image.get_rect(center=(20+self.x, 40+self.y)).center)
        #print(type(self.car_image))

        self.car_edges = []
        j = 0
        for i in self.xAB:
            self.screen.set_at((int(i)+20, int(self.yAB[j]+40)), self.blue)
            self.car_edges.append([int(i)+20,int(self.yAB[j]+40)])
            j+=1


        j = 0
        for i in self.xCD:
            self.screen.set_at((int(i) + 20, int(self.yCD[j] + 40)), self.blue)
            self.car_edges.append([int(i) + 20, int(self.yCD[j] + 40)])
            j += 1


        self.screen.blit(self.car_image, self.car_image1)

        j = 0
        for i in self.xBC:
            self.screen.set_at((int(i) + 20, int(self.yBC[j] + 40)), self.blue)
            self.car_edges.append([int(i) + 20, int(self.yBC[j] + 40)])
            j += 1


        self.xAB = []
        self.yAB = []

        self.xBC = []
        self.yBC = []

        self.xCD = []
        self.yCD = []