"""Module for implementation of the objects"""
import pygame
import random
from config import Configuration

class Item(pygame.sprite.Sprite):
    """Generic item class, for all beings in the game"""
    def __init__(self, name, tile_pos, size):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.tile_pos = tile_pos
        self.rel_tile_pos = tuple(map(sum, zip(self.tile_pos[:2], (0, -self.tile_pos[2]))))
        #size is a tuple of (width, height) pixels
        self.size = []
        self.size.append(size[0]*Configuration.ZOOM_LEVEL)
        self.size.append(size[1]*Configuration.ZOOM_LEVEL)
        self.size = tuple(self.size)
        self.inventory = []
        self.img = pygame.Surface
        self.display = True

    def load_img(self, img_name):
        """Loads an image and returns the Surface object sized"""
        img_path = Configuration.ICONS_PATH
        img = pygame.image.load(img_path+img_name+".png").convert_alpha()
        img = pygame.transform.scale(img, self.size)
        return img
    
    def draw(self, screen, pix):
        try:
            # Default blit at the tile pixel (used as fallback)
            screen.blit(self.img, (int(pix[0]), int(pix[1])))
        except Exception:
            # Show something if picture is not loaded
            pass
    
    def update_item(self):
        self.rel_tile_pos = tuple(map(sum, zip(self.tile_pos[:2], (0, -self.tile_pos[2]))))
            

class StaticItem(Item):
    """Class defining an item that can not move and will show always the same 
    face"""
    def __init__(self, name, tile_pos, size, img_name):
        super().__init__(name, tile_pos, size)
        self.img = super().load_img(img_name)

    def draw(self, screen, pix):
        """Draw static items (blocks) so their bottom aligns with the
        tile bottom. This places the block's front (lower ~1/3) in the
        lower part of the tile so moving entities can be drawn above the
        block top area.
        """
        try:
            draw_x = int(pix[0])
            draw_y = int(pix[1] + Configuration.TILE_HEIGHT - self.size[1])
            screen.blit(self.img, (draw_x, draw_y))
        except Exception:
            pass

class MovingItem(Item):
    """Class for an item that will move and can show different faces"""
    def __init__(self, name, tile_pos, size, facing, speed, img_name, frec_movement=0.0):
        super().__init__(name, tile_pos, size)
        self.facing = facing
        self.speed = speed
        self.frec_movement = frec_movement

        self.f_img = super().load_img(img_name+"_down")
        self.b_img = super().load_img(img_name+"_up")
        self.l_img = super().load_img(img_name+"_left")
        self.r_img = super().load_img(img_name+"_right")

        self.set_facing("down")

    def set_facing(self, facing):
        """Method for selecting the image that will be shown"""
        if facing == "down":
            self.facing = "down"
            self.img = self.f_img
        if facing == "up":
            self.facing = "up"
            self.img = self.b_img
        if facing == "left":
            self.facing = "left"
            self.img = self.l_img
        if facing == "right":
            self.facing = "right"
            self.img = self.r_img
         
    def move(self, delta):
        """Method for updating the possition of the item"""
        self.tile_pos = tuple([(a+b) for a, b in zip(self.tile_pos, delta)])

    def draw(self, screen, pix):
        """Draw moving items (mobs, player) so their feet rest on the top
        portion of the tile (approximately the upper 2/3). This makes
        them appear above the block's top surface.
        """
        try:
            draw_x = int(pix[0])
            top_area_height = (Configuration.TILE_HEIGHT * 2) // 3
            # Place the bottom of the sprite at the top_area_height within the tile
            draw_y = int(pix[1] + top_area_height - self.size[1])
            screen.blit(self.img, (draw_x, draw_y))
        except Exception:
            pass

    def roam(self):
        if random.random() < self.frec_movement:
            move_to = random.choice(list(Configuration.directions))
            self.set_facing(move_to)
            self.move(Configuration.directions[move_to])
