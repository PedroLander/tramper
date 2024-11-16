"""Configuration file"""

class Configuration:
    """Configuration class"""
    ZOOM_LEVEL = 1
    TILE_WIDTH = 64*ZOOM_LEVEL
    TILE_HEIGHT = 64*ZOOM_LEVEL
    N_HORIZ_TILES = 17 # Multiple of three
    N_VERT_TILES = 17 # Multiple of three
    N_HORIZ_TILES_SHOWN = 13  # Odd number
    N_VERT_TILES_SHOWN = 7 # Odd number
    TEXT_WIDTH = TILE_WIDTH*N_HORIZ_TILES_SHOWN
    TEXT_HEIGHT = 100
    SCREEN_WIDTH = TILE_WIDTH*N_HORIZ_TILES_SHOWN
    SCREEN_HEIGHT = TILE_HEIGHT*N_VERT_TILES_SHOWN+TEXT_HEIGHT

    directions = {"down":(0,1),"up":(0,-1),"left":(-1,0),"right":(1,0)}
    ICONS_PATH="assets/images/icons/"

