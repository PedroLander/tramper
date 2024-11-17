"""Module that contains the main game class"""
import pygame
from config import Configuration
from src.engine.level import Level
from src.engine.event_manager import EventManager
from .panel import Panel



class MainLoop():
    """The main game class"""
    def __init__(self, config, screen):
        self.screen = screen
        self.curr_scene = Level(config, self.screen)
        self.event_mngr = EventManager(self.curr_scene)

        # Text
        pygame.font.init()
        # Text background
        self.panel = Panel(Configuration)

    def run(self, config):
        """The loop to run the pygame game engine"""
        running = True
        while running :

        # 1. Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.event_mngr.manage_event(config, keys, self.panel)

        # 2. Update scene... Calls to Level's updating method
            self.curr_scene.update_level()

        # 3. Manage collisions... Calls to Level's collision manager method
            self.curr_scene.collision_mngr()

        # 4. Update screen
            # Clean the screen
            self.screen.fill((0,100,0))
            self.curr_scene.draw()

            self.screen.blit(self.panel,(0,config.TILE_HEIGHT*config.N_VERT_TILES_SHOWN))

            pygame.display.flip()

            #The optional argument limits the fps (not very accurate).
            pygame.time.Clock().tick(10)

