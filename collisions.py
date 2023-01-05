import pygame

class Collisions:
    def __init__(self,  xtext, ytext,type,screen):
        self.blue =  (0, 0, 128)
        self.screen = screen
        self.type=type
        self.xtext = xtext
        self.ytext = ytext
        self.Ytext = ytext
        self.txt = ""
    def display_coordinates(self, x, y):

        self.ytext = self.Ytext
        j=0
        for i in self.type:
            self.txt = ""
            self.txt += (i+ " : " + str(round(x[j])) + "x" + str(round(y[j])))
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(self.txt, True, self.blue)
            textRect = text.get_rect()
            textRect.center = (self.xtext // 2, self.ytext // 2)
            self.screen.blit(text, textRect)
            self.ytext+=80
            j+=1

    def display_score(self,car):
        self.txt = "Score: " + str(car.score)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.txt, True, self.blue)
        textRect = text.get_rect()
        textRect.center = (600,50)
        self.screen.blit(text, textRect)

    def binary_search(self, arr, low, high, x):

        if high >= low:

            mid = (high + low) // 2

            # print(arr[mid], " ",x," ", x[0])

            if arr[mid] == x:
                return mid

            if arr[mid][0] > x[0]:
                return self.binary_search(arr, low, mid - 1, x)

            if arr[mid][0] == x[0]:
                if arr[mid][1] > x[1]:
                    return self.binary_search(arr, low, mid - 1, x)
                if arr[mid][1] < x[1]:
                    return self.binary_search(arr, mid + 1, high, x)

            if arr[mid][0] < x[0]:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            return -1

    def colision_detection(self,world_table,car_table):
        sorted(car_table,reverse=False)
        sorted(world_table, reverse=False)
        result = -1
        for i in car_table:

            result = self.binary_search(world_table, 0, len(world_table) - 1, i)
            if result != -1:
                break


        if result != -1:
            # print("Chłop po wojaku chyba bo wrombał bez kitu", str(result))
            return 1
        else:
            # print("Brak kolizji")
            return 2

    def measure_distance_to_obstacle(self):
        pass