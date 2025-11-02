"""Module that contains the main game class"""
from __future__ import annotations
import pygame

from src.engine.level import Level
from src.engine.event_manager import EventManager
from .layout import Layout

from config import dynamic_config

class MainLoop():
    """The main game class"""
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # Surface layout
        self.layout = Layout()
        self.curr_scene = Level(self.layout)
        self.event_mngr = EventManager(self.curr_scene)
        self.running = True

    def run(self):
        """The loop to run the pygame game engine"""
        while self.running :

        # 1. Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.event_mngr.manage_event(keys, self.layout)

        # 2. Update scene... Calls to Level's updating method
            self.curr_scene.update_level()

        # 4. Update screen
            # Clean the screen
            self.screen.fill((0,0,0))

            # Draw the scene onto its surfaces (e.g., layout.surface1)
            self.curr_scene.draw()

            # Compose the layout by blitting panels onto the layout surface
            self.layout.blit_pans()

            # Blit the composed layout to the screen and flip
            self.screen.blit(self.layout,(0,0))
            pygame.display.flip()

            #The optional argument limits the fps (not very accurate).
            pygame.time.Clock().tick(10)

