import pygame
from  src.items.player import Player
from  ..items.plants import Quartz
from  src.engine.funcs import move_bbox, create_tiles

from itertools import product
#from ...config import Configuration

class Level:
    """
    The game objects are mainly a list of the items being simulated and a dict 
     of the plot currently being shown"""
    def __init__(self, config, screen):
        
        # Calculate bounding box of the plot
        self.screen = screen
        self.tile_bbox = [0, config.N_HORIZ_TILES_SHOWN-1,
                          0, config.N_VERT_TILES_SHOWN-1]

        # Create the grid of tiles inside the bounding box
        self.tiles = create_tiles(self.tile_bbox, config)
        # List of the tiles to be rendered
        self.tiles_shown = self.tiles

        # Create the player
        self.player = Player((0, 0))

        # Create other items
        self.rock = Quartz((0,0))

        # Make a list with all the items in the plot
        self.items = [self.player, self.rock]

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
                item.draw(self.screen,self.tiles[item.tile_pos]["pix"])

    def collision_mngr(self):
        pass

    def event_mngr(self, config, keys):
        ### I have to abstract this moving the repeating code to other files.
        if keys[pygame.K_DOWN]:
            self.player.set_facing("front")
            delta = (0, 1)
            # Check for obstacles
            dest = tuple([(a+b) for a, b in zip(self.player.tile_pos, delta)])
            if self.tiles[dest]["content"]==None:
                # Empty origin tile content
                self.tiles[self.player.tile_pos]["content"]=None
                # Update player's possition attribute
                self.player.move(delta)
                #Change plot being rendered if necesary
                if self.player.tile_pos[1]>self.tile_bbox[3]:
                    self.tile_bbox = move_bbox("down",self.tile_bbox,config)
                    self.tiles=create_tiles(self.tile_bbox, config)
                # Fill destination tile content
                self.tiles[self.player.tile_pos]["content"]=self.player

        if keys[pygame.K_UP]:
            self.player.set_facing("back")
            delta = (0, -1)
            # Check for obstacles
            dest = tuple([(a+b) for a, b in zip(self.player.tile_pos, delta)])
            if self.tiles[dest]["content"]==None:
                # Empty origin tile content
                self.tiles[self.player.tile_pos]["content"]=None
                # Update player's possition attribute
                self.player.move(delta)
                #Change plot being rendered if necesary
                if self.player.tile_pos[1]<self.tile_bbox[2]:
                    self.tile_bbox = move_bbox("up",self.tile_bbox,config)
                    self.tiles=create_tiles(self.tile_bbox, config)
                # Fill destination tile content
                self.tiles[self.player.tile_pos]["content"]=self.player

        if keys[pygame.K_LEFT]:
            self.player.set_facing("left")
            delta = (-1, 0)
            # Check for obstacles
            dest = tuple([(a+b) for a, b in zip(self.player.tile_pos, delta)])
            if self.tiles[dest]["content"]==None:
                # Empty origin tile content
                self.tiles[self.player.tile_pos]["content"]=None
                # Update player's possition attribute
                self.player.move(delta)
                #Change plot being rendered if necesary
                if self.player.tile_pos[0]<self.tile_bbox[0]:
                    self.tile_bbox = move_bbox("left",self.tile_bbox,config)
                    self.tiles=create_tiles(self.tile_bbox, config)
                # Fill destination tile content
                self.tiles[self.player.tile_pos]["content"]=self.player

        if keys[pygame.K_RIGHT]:
            self.player.set_facing("right")
            delta = (1, 0)
            # Check for obstacles
            dest = tuple([(a+b) for a, b in zip(self.player.tile_pos, delta)])
            if self.tiles[dest]["content"]==None:
                # Empty origin tile content
                self.tiles[self.player.tile_pos]["content"]=None
                # Update player's possition attribute
                self.player.move(delta)
                #Change plot being rendered if necesary
                if self.player.tile_pos[0]>self.tile_bbox[1]:
                    self.tile_bbox = move_bbox("right",self.tile_bbox,config)
                    self.tiles=create_tiles(self.tile_bbox, config)
                # Fill destination tile content
                self.tiles[self.player.tile_pos]["content"]=self.player
