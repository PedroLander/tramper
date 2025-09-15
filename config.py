"""Configuration file"""

class Configuration:
    """Configuration class"""
    
    # Screen size
    display_width = 800
    display_height = 600

    ZOOM_LEVEL = 1

    N_X_TILES = 18 # Multiple of three
    N_Y_TILES = 18 # Multiple of three
    N_Z_TILES = 18 # Multiple of three
    N_X_TILES_SHOWN = 12 # Odd number
    N_Y_TILES_SHOWN = 11 # Odd number

    # (TILE_WIDTH/TILE_HEIGHT will be computed after surface dimensions are declared)



    # Layout structure. view layout.png fow diagram.
    surface1_x_pos = 50 # x coordinate of the top left corner
    surface1_y_pos = 50 # y coordinate of the top left corner
    
    surface1_width = 750
    surface1_height = 400

    # Compute tile size from the surface where tiles are drawn so pixels are integers
    # Use integer division so TILE_WIDTH/TILE_HEIGHT are ints and align to pixel grid
    TILE_WIDTH = surface1_width // N_X_TILES_SHOWN
    TILE_HEIGHT = surface1_height // N_Y_TILES_SHOWN

    surface2_x_pos = 50 # x coordinate of the top left corner
    surface2_y_pos = 455 # y coordinate of the top left corner
    
    surface2_width = 560 
    surface2_height = 160

    surface3_x_pos = 590 # x coordinate of the top left corner
    surface3_y_pos = 455 # y coordinate of the top left corner
    
    surface3_width = 185
    surface3_height = 160


    directions = {"down":(0,1),"up":(0,-1),"left":(-1,0),"right":(1,0)}
    ICONS_PATH="assets/images/icons/"

