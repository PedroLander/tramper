"""Configuration file"""

class Configuration:
    """Configuration class"""
    TILE_WIDTH = 64
    TILE_HEIGHT = 64
    N_HORIZ_TILES = 15 # Multiple of three
    N_VERT_TILES = 15 # Multiple of three
    N_HORIZ_TILES_SHOWN = 7 # Odd number
    N_VERT_TILES_SHOWN = 7 # Odd number
    SCREEN_WIDTH = TILE_WIDTH*N_HORIZ_TILES_SHOWN
    SCREEN_HEIGHT = TILE_HEIGHT*N_VERT_TILES_SHOWN
