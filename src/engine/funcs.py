from itertools import product
"""Auxiliary functions"""

def move_bbox(side, tile_bbox, config):
    """Updates the object bounding box after pressing a key"""
    match side:
        case "down":
            tile_bbox[2]=tile_bbox[3]+1
            tile_bbox[3]=tile_bbox[3]+config.N_VERT_TILES_SHOWN
        case "up":
            tile_bbox[3]=tile_bbox[2]-1
            tile_bbox[2]=tile_bbox[2]-config.N_VERT_TILES_SHOWN
        case "left":
            tile_bbox[1]=tile_bbox[0]-1
            tile_bbox[0]=tile_bbox[0]-config.N_HORIZ_TILES_SHOWN
        case "right":
            tile_bbox[0]=tile_bbox[1]+1
            tile_bbox[1]=tile_bbox[1]+config.N_HORIZ_TILES_SHOWN
    return tile_bbox

def bbox_to_grid(bbox):
    grid = [(a, b) for a, b in product(
                            range(bbox[0],bbox[1]+1),
                            range(bbox[2],bbox[3]+1))]
    return grid

def create_tiles(tile_bbox, config):
    """
    Creates a dictionary with the coordinates of a plot as keys and the 
    properties and content of the tile as a value.

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

def tiles_to_pix(tile_bbox_shown, config):
    tile_nums = [(a, b) for a, b in product(
                            range(tile_bbox_shown[0],tile_bbox_shown[1]+1),
                            range(tile_bbox_shown[2],tile_bbox_shown[3]+1))]
    tile_pixels = [(config.TILE_WIDTH*h, config.TILE_HEIGHT*v)
                        for h, v in product(
                            range(config.N_HORIZ_TILES_SHOWN),
                            range(config.N_VERT_TILES_SHOWN))]
    tile_num_pix =[(a, b) for a, b in zip(tile_nums, tile_pixels)]
    tiles = {}
    for tile in tile_num_pix:
        new_tile = {}
        new_tile["pix"] = tile[1]
        tiles[tile[0]] = new_tile
    return tiles


    # new_tile["pix"] = tile[1]