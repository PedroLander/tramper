"""Configuration file"""

class StaticConfig:
    """Static parameters configuration class"""
    directions = {"down":(0,1),"up":(0,-1),"left":(-1,0),"right":(1,0)}
    ICONS_PATH="assets/images/icons/"

class DynamicConfig:
    """Dynamic parameters configuration class"""
    def __init__(self):
        # Screen size
        self.display_width = 800
        self.display_height = 580

        self.zoom: float = 1.0

        self.N_X_TILES = 42 # Multiple of three
        self.N_Y_TILES = 42 # Multiple of three
        self.N_Z_TILES = 11 # Multiple of three
        self.N_X_TILES_SHOWN = 13 # Odd number [-X ... 0 ... +X]
        self.N_Y_TILES_SHOWN = 13 # Odd number [-Y ... 0 ... +Y]

        # (TILE_WIDTH/TILE_HEIGHT will be computed after surface dimensions are declared)

        # Layout structure. view layout.png fow diagram.
        self.scene_surface_x_pos = 0 # x coordinate of the top left corner
        self.scene_surface_y_pos = 0 # y coordinate of the top left corner
        
        self.scene_surface_width = 805
        self.scene_surface_height = 435

        # Compute tile size from the surface where tiles are drawn so pixels are integers
        # Use integer division so TILE_WIDTH/TILE_HEIGHT are ints and align to pixel grid
        self.TILE_WIDTH = self.scene_surface_width // self.N_X_TILES_SHOWN
        self.TILE_HEIGHT = self.scene_surface_height // self.N_Y_TILES_SHOWN

        self.messages_surface_x_pos = 50 # x coordinate of the top left corner
        self.messages_surface_y_pos = 455 # y coordinate of the top left corner
        
        self.messages_surface_width = 560 
        self.messages_surface_height = 160

        self.options_surface_x_pos = 590 # x coordinate of the top left corner
        self.options_surface_y_pos = 455 # y coordinate of the top left corner
        
        self.options_surface_width = 185
        self.options_surface_height = 160

dynamic_config = DynamicConfig()