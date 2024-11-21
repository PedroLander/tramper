"""Module that contains the main game class"""
import pygame
from src.engine.level import Level
from src.engine.event_manager import EventManager
from .layout import Layout

class MainLoop():
    """The main game class"""
    def __init__(self, config, screen):
        self.screen = screen
        self.curr_scene = Level(config, self.screen)
        self.event_mngr = EventManager(self.curr_scene)
        self.running = True


        # Text background
        self.layout = Layout(config)

    def run(self, config):
        """The loop to run the pygame game engine"""
        while self.running :

        # 1. Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.event_mngr.manage_event(config, keys, self.layout)

        # 2. Update scene... Calls to Level's updating method
            self.curr_scene.update_level()

        # 4. Update screen
            # Clean the screen
            self.screen.fill((0,0,0))
            self.screen.blit(self.layout,(0,0))
            self.curr_scene.draw()

            pygame.display.flip()

            #The optional argument limits the fps (not very accurate).
            pygame.time.Clock().tick(10)

