from __future__ import annotations
import pygame

from config import dynamic_config
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from config import DynamicConfig

class Layout(pygame.Surface):
    def __init__(self):
        
        super().__init__((dynamic_config.display_width, dynamic_config.display_height))
        
        self.scene_surface = pygame.Surface((dynamic_config.scene_surface_width,dynamic_config.scene_surface_height))
        self.messages_surface = pygame.Surface((dynamic_config.messages_surface_width,dynamic_config.messages_surface_height))
        self.options_surface = pygame.Surface((dynamic_config.options_surface_width,dynamic_config.options_surface_height))

        self.font = 'Comic Sans MS'
        self.font_size = 20
        self.font_colour = (200,200,200)

        self.my_font = pygame.font.SysFont(self.font, self.font_size)

        self.inventory_surface = pygame.Surface((self.scene_surface.get_width(),
                                                self.scene_surface.get_height()))
        self.message_surface = pygame.Surface((self.messages_surface.get_width(),
                                               self.messages_surface.get_height()))
        self.options_surface = pygame.Surface((self.options_surface.get_width(),
                                              self.options_surface.get_height()))

        init_msg = ["Welcome to Tramper!"]
        init_options = ["<awsd>: move",
                        "<e>: grab things"]

        self.show_msg(init_msg)
        self.show_options(init_options)

    def blit_pans(self):
        self.blit(self.scene_surface,(dynamic_config.scene_surface_x_pos,dynamic_config.scene_surface_y_pos))
        self.blit(self.messages_surface,(dynamic_config.messages_surface_x_pos,dynamic_config.messages_surface_y_pos))
        self.blit(self.options_surface,(dynamic_config.options_surface_x_pos,dynamic_config.options_surface_y_pos))

    def show_msg(self, msg:list) -> None:
        self.message_surface.fill((0,0,50))
        self.multiline_blit(self.message_surface, msg)
        self.messages_surface.blit(self.message_surface,(0,0))
        self.blit_pans()

    def show_options(self, options:list) -> None:
        self.options_surface.fill((50,0,0))
        self.multiline_blit(self.options_surface, options)
        self.options_surface.blit(self.options_surface,(0,0))
        self.blit_pans()

    def show_inventory(self, inv:list) -> None:
        self.inventory_surface.fill((0,50,0))
        self.multiline_blit(self.inventory_surface, inv)
        self.scene_surface.blit(self.inventory_surface,(0,0))
        self.blit_pans()


    def multiline_blit(self, surface: pygame.Surface, text: list[str]):
        """Method for rendering a multiple line text in a pygame Surface 
        object"""
        pos_x = (surface.get_width() * 1/10)
        pos_y = (surface.get_height() * 1/10)
        position = pos_x, pos_y

        label = []
        for line in text: 
            label.append(self.my_font.render(str(line), True, self.font_colour))

        for line in enumerate(label):
            surface.blit(line[1],(position[0],position[1]+(line[0]*self.font_size)+(5*line[0])))
