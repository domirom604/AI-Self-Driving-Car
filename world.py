import pygame
import json

class World:
    def __init__(self):
        self.background_image = pygame.image.load("track.png").convert()
        file = open("colision.json",'r')
        self.colisions = json.load(file)['list']
        file.close()
