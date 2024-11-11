"""Module for implementation of the objects"""

import pygame

class Item():
    """Generic item class, for all beings in the game"""
    def __init__(self, pos, size):
        self.pos = pos
        #size is a tuple of (width, height) pixels
        self.size = size
        self.rect = pygame.Rect(pos[0]-(size[0]//2),
                                pos[1]+(size[1]//2),
                                size[0],
                                size[1])

    def load_img(self, file):
        """Loads an image and returns the Surface object sized"""
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img, self.size)
        return img
    
    def draw(self, screen):
        print (self.pos)
        screen.blit(self.img, pos_to_pix(self.pos))

class StaticItem(Item):
    """Class defining an item that can not move and will show always the same 
    face"""
    def __init__(self, pos, scale, img):
        super().__init__(pos, scale)
        self.img = super().load_img(img)

class MovingItem(Item):
    """Class for an item that will move and can show different faces"""
    def __init__(self, pos, scale, speed, f_img, b_img, l_img, r_img):
        super().__init__(pos, scale)
        self.pos = pos
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
        """Method for updating the possition of the item"""
        self.pos = [a+b for a, b in zip(self.pos, delta)]
        self.rect = self.rect.move(delta[0],delta[1])

class Human(MovingItem):
    """Human class"""
    def __init__(self, pos):
        front = "assets/images/icons/sheriff_front.png"
        back = "assets/images/icons/sheriff_back.png"
        left = "assets/images/icons/sheriff_left.png"
        right = "assets/images/icons/sheriff_right.png"
        size = (128,128)
        speed = 10
        super().__init__(pos, size, speed, front, back, left, right)

class Rock(StaticItem):
    """Rock class"""
    def __init__(self, pos):
        front = "assets/images/icons/rock1.png"
        size = (48,48)
        super().__init__(pos, size, front)
