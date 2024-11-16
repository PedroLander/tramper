"""Module that contains the main game class"""
import pygame
from src.engine.level import Level
class MainLoop():
    """The main game class"""
    def __init__(self, config, screen):
        self.screen = screen
        self.curr_scene = Level(config, self.screen)

    def run(self, config):
        """The loop to run the pygame game engine"""
        running = True
        while running :

        # 1. Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.curr_scene.event_mngr(config, keys)

        # 2. Update scene... Calls to Level's updating method
            self.curr_scene.update_level()

        # 3. Manage collisions... Calls to Level's collision manager method
            self.curr_scene.collision_mngr()

        # 4. Update screen
            self.curr_scene.draw()
            pygame.display.flip()

            #The optional argument limits the fps (not very accurate).
            pygame.time.Clock().tick(10)

