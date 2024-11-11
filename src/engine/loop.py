"""Module that contains the main game class"""
import pygame
from ..scenes.level import Level

class MainLoop():
    """The main game class"""
    def __init__(self, screen):
        self.screen = screen
        self.curr_scene = Level(self.screen)
        self.clock = pygame.time.Clock()
        """"""
    def run(self):
        running = True
        while running :
            #The optional argument limits the fps (not very accurate).
            self.clock.tick(40)

        # 1. Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.curr_scene.event_mngr(event)
        
        # 2. Update scene... Calls to Level's updating method
            self.curr_scene.update()
        # 3. Manage collisions... Calls to Level's collision manager method
            self.curr_scene.collision_mngr()
        # 4. Update screen
            pygame.display.flip()
        


    def load_tile(self, side):
        """Updates the object bounding box after pressing a key"""
        match side:
            case "down":
                self.bbox[2]=self.bbox[3]
                self.bbox[3]=self.bbox[3]-self.screen_height
            case "up":
                self.bbox[3]=self.bbox[2]
                self.bbox[2]=self.bbox[2]+self.screen_height
            case "left":
                self.bbox[1]=self.bbox[0]
                self.bbox[0]=self.bbox[0]-self.screen_width
            case "right":
                self.bbox[0]=self.bbox[1]
                self.bbox[1]=self.bbox[1]+self.screen_width
