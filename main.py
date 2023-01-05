import sys

import keras.models

import collisions_generation
from car import *
from collisions import *
from world import *
from collisions_generation import *
from Checkpoints import Checkpoints

class Play:
    def __init__(self,model=None,control="player"):
        pygame.init()

        # okno gry
        self.w = 1800
        self.h = 900
        self.screen = pygame.display.set_mode((self.w, self.h))

        # inicjalizacja
        self.world = World()

        self.type = ["left","middle","right"]
        self.xtext1 = 550
        self.ytext1 = 70
        self.collisions = Collisions(self.xtext1,self.ytext1,self.type, self.screen)
        self.model = model
        self.control = control
        self.car = Car(900,230,self.screen,cols=self.world.colisions,collisions=self.collisions,model=self.model)
        self.checkpoints = Checkpoints(self.screen,cols=self.world.colisions,car=self.car)

    # only for colision generate json !!!
    # screen.blit(world.background_image, [0, 0])
    # collisions_generation.generate_list("col.json",screen)
    def run(self):
        while True:
            # obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # only for show colision generated
            # for i in world.colisions:
            #     screen.set_at(i, (255,0,0))

            self.screen.blit(self.world.background_image, [0, 0])
            self.car.render(self.car.x,self.car.y)
            self.checkpoints.checkReache(carXY=[self.car.x,self.car.y])
            # checkpoints.render()

            if(self.collisions.colision_detection(self.world.colisions, self.car.car_edges)==1):
                return self.car.score
                """
                car.x=900
                car.y=230
                car.angle=90
                car.table=[]
                """

            if self.control == "player":
                self.car.player_control()
            if self.control == "keras":
                self.car.keras_control()

            xendall = [self.car.xend2,self.car.xend, self.car.xend1]
            yendall = [self.car.yend2,self.car.yend, self.car.yend1]
            #collisions.display_coordinates(xendall, yendall)
            self.collisions.display_score(self.car)
            pygame.display.update()
            if self.car.score >= 15:
                self.model.save(f'model_{self.car.score}.h5')


if __name__ == "__main__":
    game = Play(control="keras",model=keras.models.load_model('model_15.h5'))
    game.run()