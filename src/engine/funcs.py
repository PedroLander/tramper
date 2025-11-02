from itertools import product
from ..items.entities import Item

"""Auxiliary functions"""
from config import dynamic_config
def move_bbox(side, tile_bbox):
    """Updates the object bounding box after pressing a key"""
    match side:
        case "down":
            tile_bbox[2]=tile_bbox[3]+1
            tile_bbox[3]=tile_bbox[3]+dynamic_config.N_Y_TILES_SHOWN
        case "up":
            tile_bbox[3]=tile_bbox[2]-1
            tile_bbox[2]=tile_bbox[2]-dynamic_config.N_Y_TILES_SHOWN
        case "left":
            tile_bbox[1]=tile_bbox[0]-1
            tile_bbox[0]=tile_bbox[0]-dynamic_config.N_X_TILES_SHOWN
        case "right":
            tile_bbox[0]=tile_bbox[1]+1
            tile_bbox[1]=tile_bbox[1]+dynamic_config.N_X_TILES_SHOWN
    return tile_bbox

def bbox_to_grid(bbox):
    grid = [(x, y, z) for x, y, z in product(
                                range(bbox[0],bbox[1]+1),
                                range(bbox[2],bbox[3]+1), 
                                range(bbox[4],bbox[5]+1))]
    return grid

class Cell:
    __slots__ = ('content', 'light')

    def __init__(self, content, light):
        self.content: Item | None = content
        self.light = light


def create_tiles(tile_bbox):
    """
    Creates a dictionary with the coordinates as keys and properties and 
    content of the tile as a value.

    Args:
        tile_bbox: bounding box of the plot.
        config: configuration data with number of tiles and tile sizes.

    Returns:
        dict: plot content
        
    Example:
        {(1, 2): Cell(content=<Player Sprite(in 0 groups)>, light=5)}
    """
    tile_nums = bbox_to_grid(tile_bbox)

    tiles = {tile: Cell(content=None, light=5) for tile in tile_nums}
    return tiles

class Tile:
    __slots__ = ('pix')
    def __init__(self, pix):
        self.pix = pix


def tiles_to_pix(render_bbox, z_min: int, z_max: int):
    """
    Build a dictionary of *visible* tiles from a 3D bbox.
    
    Args:
        render_bbox: [x_min, x_max, y_min, y_max, z_min, z_max]
        screen_size: (screen_width, screen_height)
    
    Returns:
        dict[(x, y, z)] = Tile(pix=(px, py))
    """

    screen_w, screen_h = dynamic_config.display_width, dynamic_config.display_height

    tiles = {}
    for x, y, z in product(
        range(render_bbox[0], render_bbox[1] + 1),
        range(render_bbox[2] + z_min, render_bbox[3] + 1 + z_max),
        range(-3, 4),
    ):
        px = (x-render_bbox[0]) * dynamic_config.TILE_WIDTH
        py = (y-render_bbox[2]) * dynamic_config.TILE_HEIGHT - z * (dynamic_config.TILE_HEIGHT)

        # --- Culling: only keep visible tiles ---
        if (0 <= px < screen_w) and (0 <= py < screen_h):
            tiles[(x, y, z)] = Tile(pix=(px, py))

    return tiles