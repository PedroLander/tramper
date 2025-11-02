from __future__ import annotations
from random import randint
from ..items.blocks import GrassBlock
from ..items.rocks import Quartz
from ..items.plants import Grass, AchilleaMillefolium
from ..items.animals import RedFox
from ..items.player import Player
from ..items.entities import Item, MovingItem

from config import dynamic_config
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from config import DynamicConfig
    from .layout import Layout

from src.engine.funcs import create_tiles, tiles_to_pix

class Level:
    """
    The level objects are:
     - A list of the items being simulated.
     - A dict of the tiles simulated.
     - A dict of the tiles being rendered at the momment
    """
    def __init__(self, layout: Layout):
        
        # Bounding box of the simulated tiles
        self.layout = layout

        simulation_bbox_x0 = int((dynamic_config.N_X_TILES/2)-0.5)
        simulation_bbox_y0 = int((dynamic_config.N_Y_TILES/2)-0.5)
        simulation_bbox_z0 = int((dynamic_config.N_Z_TILES/2)-0.5)
        self.simulation_bbox = [-simulation_bbox_x0, simulation_bbox_x0,
                          -simulation_bbox_y0, simulation_bbox_y0,
                          -simulation_bbox_z0, simulation_bbox_z0]
        
        # Bounding box of the rendered tiles at z=0
        render_bbox_x0 = int((dynamic_config.N_X_TILES_SHOWN/2)-0.5)
        render_bbox_y0 = int((dynamic_config.N_Y_TILES_SHOWN/2)-0.5)
        self.render_bbox = [-render_bbox_x0, render_bbox_x0, 
                            -render_bbox_y0, render_bbox_y0]

        # Create the grid of tiles inside the bounding box
        self.tiles = create_tiles(self.simulation_bbox)

        # Dict of the tiles to be rendered.
        self.tiles_shown = tiles_to_pix(self.render_bbox, z_min=-1, z_max=7)

        # Make a list with all the items in the plot
        self.items: list[Item] = []

        # Create the ground blocks (z=0) and add them to the item list
        ground_tiles = [tile for tile in self.tiles if tile[2] <= 0]
        for tile in ground_tiles:
            self.items.append(GrassBlock((tile[0],tile[1],tile[2])))
        self.items.append(GrassBlock((2,2,1)))
        self.items.append(GrassBlock((2,2,2)))
        self.items.append(GrassBlock((3,2,1)))
        self.items.append(GrassBlock((-3,9,1)))
        self.items.append(GrassBlock((-3,9,2)))
        self.items.append(GrassBlock((-3,9,3)))
        self.items.append(GrassBlock((-3,9,4)))
        self.items.append(GrassBlock((-3,9,5)))

        # Create the player and add it to the item list
        self.player = Player((0, 0, 1))
        self.items.append(self.player)

        # Create other items and add them to the item list
        for _ in range(randint(10,20)):
            self.items.append(
                Quartz((randint(self.simulation_bbox[0], self.simulation_bbox[1]),
                        randint(self.simulation_bbox[2], self.simulation_bbox[3]), 
                        1)))
        for _ in range(randint(5,10)):
            self.items.append(
                AchilleaMillefolium((randint(self.simulation_bbox[0], self.simulation_bbox[1]),
                        randint(self.simulation_bbox[2], self.simulation_bbox[3]), 
                        1)))   
        for _ in range(randint(10,20)):
            self.items.append(
                Grass((randint(self.simulation_bbox[0], self.simulation_bbox[1]),
                    randint(self.simulation_bbox[2], self.simulation_bbox[3]),
                    1)))
        self.items.append(RedFox((2,5,1)))
        self.items.append(RedFox((1,-3,1)))
        self.items.append(RedFox((1,-3,1)))
        self.items.append(RedFox((1,-3,1)))
        self.items.append(RedFox((1,-3,1)))

        # Place the items in the tile
        for item in self.items:
            self.tiles[item.tile_pos].content=item

    def update_level(self):
        #Updates all item's state
        for item in self.items:
            item.update_item()
            if isinstance(item, MovingItem):
                item.roam_xy()

    def draw(self):
        self.layout.scene_surface.fill((0,0,0))
        item: Item
        for item in sorted(self.items, key=lambda item: (item.tile_pos[2], item.tile_pos[1])):
            # If the first 2 (x, y) coordinates of the item are in the box shown
            if item.tile_pos in self.tiles_shown:
                if item.display == True:
                    pix = self.tiles_shown[item.tile_pos].pix
                    # Ensure pixel positions are integers to avoid subpixel gaps
                    pix = (int(pix[0]), int(pix[1]))
                    item.draw(self.layout.scene_surface, pix)
