"""Configuration file"""

class Configuration:
    """Configuration class"""
    ZOOM_LEVEL = 0.5
    TILE_WIDTH = 64*ZOOM_LEVEL
    TILE_HEIGHT = 64*ZOOM_LEVEL
    N_HORIZ_TILES = 30 # Multiple of three
    N_VERT_TILES = 30 # Multiple of three
    N_HORIZ_TILES_SHOWN = 19 # Odd number
    N_VERT_TILES_SHOWN = 17 # Odd number
    SCREEN_WIDTH = TILE_WIDTH*N_HORIZ_TILES_SHOWN
    SCREEN_HEIGHT = TILE_HEIGHT*N_VERT_TILES_SHOWN
