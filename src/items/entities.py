"""Module for implementation of the objects"""

import pygame

class Item(pygame.sprite.Sprite):
    """Generic item class, for all beings in the game"""
    def __init__(self, tile_pos, size):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.tile_pos = tile_pos
        #size is a tuple of (width, height) pixels
        self.size = size

    def load_img(self, file):
        """Loads an image and returns the Surface object sized"""
        img = pygame.image.load(file).convert_alpha()
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
    def __init__(self, tile_pos, size, img):
        super().__init__(tile_pos, size)
        self.img = super().load_img(img)
        self.rect = self.img.get_rect()

class MovingItem(Item):
    """Class for an item that will move and can show different faces"""
    def __init__(self, tile_pos, size, speed, f_img, b_img, l_img, r_img):
        super().__init__(tile_pos, size)
        self.speed = speed

        self.f_img = super().load_img(f_img)
        self.b_img = super().load_img(b_img)
        self.l_img = super().load_img(l_img)
        self.r_img = super().load_img(r_img)

        self.set_facing("front")

    def set_facing(self, facing):
        """Method for selecting the image that will be shown"""
        if facing == "front":
            self.img = self.f_img
        if facing == "back":
            self.img = self.b_img
        if facing == "left":
            self.img = self.l_img
        if facing == "right":
            self.img = self.r_img
        
    def move(self, delta):
        ######## Mirar esto
        """Method for updating the possition of the item"""
        self.tile_pos = tuple([(a+b) for a, b in zip(self.tile_pos, delta)])

class Human(MovingItem):
    """Human class"""
    def __init__(self, pos):
        front = "assets/images/icons/sheriff_front.png"
        back = "assets/images/icons/sheriff_back.png"
        left = "assets/images/icons/sheriff_left.png"
        right = "assets/images/icons/sheriff_right.png"
        size = (64,64)
        speed = 1
        super().__init__(pos, size, speed, front, back, left, right)

class Rock(StaticItem):
    """Rock class"""
    def __init__(self, pos):
        front = "assets/images/icons/rock1.png"
        size = (64,64)
        super().__init__(pos, size, front)
