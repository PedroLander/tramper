import pygame
from random import randint
from ..items.blocks import GrassBlock
from ..items.rocks import Quartz
from ..items.plants import Grass, AchilleaMillefolium
from ..items.animals import RedFox
from ..items.player import Player

from src.engine.funcs import move_bbox, create_tiles, tiles_to_pix

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
        x_bbox_limit_ini = int((config.N_X_TILES/2)-0.5)
        y_bbox_limit_ini = int((config.N_Y_TILES/2)-0.5)
        z_bbox_limit_ini = int((config.N_Z_TILES/2)-0.5)
        self.tile_bbox = [-x_bbox_limit_ini, x_bbox_limit_ini,
                          -y_bbox_limit_ini, y_bbox_limit_ini,
                          -z_bbox_limit_ini, z_bbox_limit_ini]
        x_bbox_shown_limit_ini = int((config.N_X_TILES_SHOWN/2)-0.5)
        y_bbox_shown_limit_ini = int((config.N_Y_TILES_SHOWN/2)-0.5)
        self.tile_bbox_shown = [-x_bbox_shown_limit_ini, 
                                x_bbox_shown_limit_ini, 
                                -y_bbox_shown_limit_ini, 
                                y_bbox_shown_limit_ini]

        # Create the grid of tiles inside the bounding box
        self.tiles = create_tiles(self.tile_bbox)

        # Dict of the tiles to be rendered.
        self.tiles_shown = tiles_to_pix(self.tile_bbox_shown, config)

        # Make a list with all the items in the plot
        self.items = []

        # Create the ground blocks (z=0) and add them to the item list
        for tile in self.tiles:
            self.items.append(GrassBlock((tile[0],tile[1],0)))


        # Create the player and add it to the item list
        self.player = Player((0, 0, 1))
        self.items.append(self.player)

        # Create other items and add them to the item list
        for _ in range(randint(10,20)):
            self.items.append(
                Quartz((randint(self.tile_bbox[0], self.tile_bbox[1]),
                        randint(self.tile_bbox[2], self.tile_bbox[3]), 
                        1)))
        for _ in range(randint(5,10)):
            self.items.append(
                AchilleaMillefolium((randint(self.tile_bbox[0], self.tile_bbox[1]),
                        randint(self.tile_bbox[2], self.tile_bbox[3]), 
                        1)))   
        for _ in range(randint(10,20)):
            self.items.append(
                Grass((randint(self.tile_bbox[0], self.tile_bbox[1]),
                    randint(self.tile_bbox[2], self.tile_bbox[3]),
                    1)))
        self.items.append(RedFox((2,5,0)))
        self.items.append(RedFox((1,-3,0)))
        self.items.append(RedFox((1,-3,0)))
        self.items.append(RedFox((1,-3,0)))
        self.items.append(RedFox((1,-3,0)))

        # Place the items in the tile
        for item in self.items:
            self.tiles[item.tile_pos]["content"]=item

    def update_level(self):
        #Updates all item's state
        for item in self.items:
            item.update_item()
            try:
                item.roam()
            except: continue

    def draw(self):
        # Draw the items in the screen
        for item in self.items:
            # If the first 2 (x, y) coordinates of the item are in the box shown
            if item.tile_pos[:2] in self.tiles_shown:
                if item.display == True:
                    item.draw(self.screen,self.tiles_shown[item.tile_pos[:2]]["pix"])
