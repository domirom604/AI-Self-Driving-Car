import json
import pygame

def generate_list(file_name,screen):

    file = open(file_name,'w')
    colisions_new = []
    image = pygame.image.load("track.png").convert()
    for x in range(1800):
        for y in range(900):
            if (screen.get_at((x,y)) == (0,0,0)) or (screen.get_at((x,y)) == (34,177,76)):
                colisions_new.append([x,y])

    dict = {'list':colisions_new}
    json.dump(dict,file)