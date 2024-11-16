"""Module for implementation of the objects"""
import pygame
import random
from config import Configuration

class Item(pygame.sprite.Sprite):
    """Generic item class, for all beings in the game"""
    def __init__(self, tile_pos, size):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.tile_pos = tile_pos
        #size is a tuple of (width, height) pixels
        self.size = []
        self.size.append(size[0]*Configuration.ZOOM_LEVEL)
        self.size.append(size[1]*Configuration.ZOOM_LEVEL)
        self.size = tuple(self.size)

    def load_img(self, img_name):
        """Loads an image and returns the Surface object sized"""
        img_path = Configuration.ICONS_PATH
        img = pygame.image.load(img_path+img_name+".png").convert_alpha()
        img = pygame.transform.scale(img, self.size)
        return img
    
    def draw(self, screen, pix):
        try:
            screen.blit(self.img, pix)
        except:
            # Show something if picture is not loaded
            pass
    
    def update_item(self):
        pass

class StaticItem(Item):
    """Class defining an item that can not move and will show always the same 
    face"""
    def __init__(self, tile_pos, size, img_name):
        super().__init__(tile_pos, size)
        self.img = super().load_img(img_name)
        self.rect = self.img.get_rect()

class MovingItem(Item):
    """Class for an item that will move and can show different faces"""
    def __init__(self, tile_pos, size, facing, speed, img_name, frec_movement=0):
        super().__init__(tile_pos, size)
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

    def roam(self):
        if random.random() < self.frec_movement:
            move_to = random.choice(list(Configuration.directions))
            self.set_facing(move_to)
            self.move(Configuration.directions[move_to])

class Human(MovingItem):
    """Human class"""
    def __init__(self, pos):
        img_name = "sheriff"
        size = (64,64)
        init_facing = "down"
        speed = 1
        super().__init__(pos, size, init_facing, speed, img_name)


