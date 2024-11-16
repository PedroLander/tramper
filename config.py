"""Configuration file"""

class Configuration:
    """Configuration class"""
    TILE_WIDTH = 64
    TILE_HEIGHT = 64
    N_HORIZ_TILES_SHOWN = 5
    N_VERT_TILES_SHOWN = 5
    SCREEN_WIDTH = TILE_WIDTH*N_HORIZ_TILES_SHOWN
    SCREEN_HEIGHT = TILE_HEIGHT*N_VERT_TILES_SHOWN
