import pygame
from random import randint
from  src.items.player import Player
from  ..items.plants import Quartz
from  src.engine.funcs import move_bbox, create_tiles, tiles_to_pix

from itertools import product
#from ...config import Configuration

class Level:
    """
    The level objects are:
     - A list of the items being simulated.
     - A dict of the tiles simulated.
     - A dict of the tiles being rendered at the momment
    """
    def __init__(self, config, screen):
        
        # Calculate bounding box of the plot
        self.screen = screen
        horiz_bbox_limit_ini = int((config.N_HORIZ_TILES/2)-0.5)
        vert_bbox_limit_ini = int((config.N_VERT_TILES/2)-0.5)
        self.tile_bbox = [-horiz_bbox_limit_ini, horiz_bbox_limit_ini,
                          -vert_bbox_limit_ini, vert_bbox_limit_ini]
        horiz_bbox_shown_limit_ini = int((config.N_HORIZ_TILES_SHOWN/2)-0.5)
        vert_bbox_shown_limit_ini = int((config.N_VERT_TILES_SHOWN/2)-0.5)
        self.tile_bbox_shown = [-horiz_bbox_shown_limit_ini, 
                                horiz_bbox_shown_limit_ini, 
                                -vert_bbox_shown_limit_ini, 
                                vert_bbox_shown_limit_ini]

        # Create the grid of tiles inside the bounding box
        self.tiles = create_tiles(self.tile_bbox, config)

        # Dict of the tiles to be rendered.
        self.tiles_shown = tiles_to_pix(self.tile_bbox_shown, config)

        # Map tiles to pixels

        # Make a list with all the items in the plot
        self.items = []

        # Create the player and add it to the item list
        self.player = Player((0, 0))
        self.items.append(self.player)

        # Create other items and add them to the item list
        for _ in range(randint(10,20)):
            self.items.append(
                Quartz((randint(self.tile_bbox[0], self.tile_bbox[1]),
                        randint(self.tile_bbox[2], self.tile_bbox[3]))))

        # Place the items in the tile
        for item in self.items:
            self.tiles[item.tile_pos]["content"]=item

    def update_level(self):
        #Updates all item's state
        for item in self.items:
            item.update_item()

    def draw(self):
        # Clean the screen
        self.screen.fill((0,100,0))
        # Draw the items in the screen
        for item in self.items:
            if item.tile_pos in self.tiles_shown:
                item.draw(self.screen,self.tiles_shown[item.tile_pos]["pix"])

    def collision_mngr(self):
        pass
