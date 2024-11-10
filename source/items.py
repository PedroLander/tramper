import pygame

class Item():
    def __init__(self, pos, size):
        self.pos = pos
        #size is a tuple of (width, height) pixels
        self.size = size

    def load_img(self, file):
        img = pygame.image.load(file).convert_alpha()

        #img_width, img_height = img.get_size()
        #new_size = (int(img_width*self.scale),
        #            int(img_height*self.scale))
        img = pygame.transform.scale(img, self.size)
        return img

class StaticItem(Item):
    def __init__(self, pos, scale, img):
        super().__init__(pos, scale)
        self.img = super().load_img(img)

class MovingItem(Item):
    def __init__(self, pos, scale, f_img, b_img, l_img, r_img):
        super().__init__(pos, scale)

        self.f_img = super().load_img(f_img)
        self.b_img = super().load_img(b_img)
        self.l_img = super().load_img(l_img)
        self.r_img = super().load_img(r_img)

        self.set_facing("front")

    def set_facing(self, facing):
        if facing == "front":
            self.img = self.f_img
        if facing == "back":
            self.img = self.b_img
        if facing == "left":
            self.img = self.l_img
        if facing == "right":
            self.img = self.r_img

    def move(self, delta):
        self.pos = [a-b for a, b in zip(self.pos, delta)]

class Human(MovingItem):
    def __init__(self, pos):
        front = "images/icons/sheriff_front.png"
        back = "images/icons/sheriff_back.png"
        left = "images/icons/sheriff_left.png"
        right = "images/icons/sheriff_right.png"
        size = (128,128)
        super().__init__(pos, size, front, back, left, right)

class Rock(StaticItem):
    def __init__(self, pos):
        front = "images/icons/rock1.png"
        size = (48,48)
        super().__init__(pos, size, front)
