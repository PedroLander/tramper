from itertools import product
from typing import Tuple
"""Auxiliary functions"""

def move_bbox(side, tile_bbox, config):
    """Updates the object bounding box after pressing a key"""
    match side:
        case "down":
            tile_bbox[2]=tile_bbox[3]+1
            tile_bbox[3]=tile_bbox[3]+config.N_Y_TILES_SHOWN
        case "up":
            tile_bbox[3]=tile_bbox[2]-1
            tile_bbox[2]=tile_bbox[2]-config.N_Y_TILES_SHOWN
        case "left":
            tile_bbox[1]=tile_bbox[0]-1
            tile_bbox[0]=tile_bbox[0]-config.N_X_TILES_SHOWN
        case "right":
            tile_bbox[0]=tile_bbox[1]+1
            tile_bbox[1]=tile_bbox[1]+config.N_X_TILES_SHOWN
    return tile_bbox

def bbox_to_grid(bbox) -> list[tuple[int, int]] | list[tuple[int, int, int]]:
    """Creates a list of tuples with the coordinates of the tiles inside the
    bounding box.
    Args:
        bbox: bounding box of the plot.
    Returns:
        list of tuples with the coordinates of the tiles inside the bounding box.
    Example:
        [(-2, -2), (-2, -1), (-2, 0),...]
    """
    if len(bbox)<5:
        grid = [(x, y) for x, y in product(
                                range(bbox[0],bbox[1]+1),
                                range(bbox[2],bbox[3]+1))]
    elif len(bbox)>5:
        grid = [(x, y, z) for x, y, z in product(
                                range(bbox[0],bbox[1]+1),
                                range(bbox[2],bbox[3]+1),
                                range(bbox[4],bbox[5]+1))]
    return grid

def create_tiles(tile_bbox:Tuple[int, int, int, int, int, int, ]) -> dict:
    """
    Creates a dictionary with the coordinates as keys and properties and 
    content of the tile as a value.
    Args:
        tile_bbox: bounding box of the plot.
        config: configuration data with number of tiles and tile sizes.
    Returns:
        dict: plot content 
    Example:
        {(1, 2): {'pix': (64, 128),
          'content': <Player Sprite(in 0 groups)>,...}
    """
    tile_nums = bbox_to_grid(tile_bbox)

    tiles = {}
    for tile in tile_nums:
        new_tile = {}
        new_tile["content"] = None
        new_tile["light"] = 5
        tiles[tile] = new_tile
    return tiles

def tiles_to_pix(tile_bbox_shown, config) -> dict:
    """Creates a dictionary with the coordinates of the tiles to be shown as
    keys and the pixel position in the surface as values.
    Args:
        tile_bbox_shown: bounding box of the tiles to be shown.
        config: configuration data with number of tiles and tile sizes.
    Returns:
        dict: tiles to be shown with pixel position.
    Example:
        {(1, 2): {'pix': (64, 128)},
         (1, 3): {'pix': (64, 192)},...}
    """
    tile_nums = [(a, b) for a, b in product(
                            range(tile_bbox_shown[0],tile_bbox_shown[1]+1),
                            range(tile_bbox_shown[2],tile_bbox_shown[3]+1))]
    tile_pixels = [(config.TILE_WIDTH*h, config.TILE_HEIGHT*v)
                        for h, v in product(
                            range(config.N_X_TILES_SHOWN),
                            range(config.N_Y_TILES_SHOWN))]
    tiles = {}
    for a, b in zip(tile_nums, tile_pixels):
        tiles[a] = {"pix":b}
    return tiles

def save_configuration(configuration):
    pass