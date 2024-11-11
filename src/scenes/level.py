import pygame
from ..items.player import Player
from ..items.plants import Quartz
from ..engine.funcs import load_tile

class Level:
    def __init__(self, screen):

        self.screen = screen
        self.player = Player((100, 100))
        self.env = [Quartz((300,100)),Quartz((-200,50))]
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.bbox = [-self.screen_width//2, self.screen_width//2,
                      self.screen_height//2, -self.screen_height//2]


    def update(self):
        #Updates all item's state
        #self.player.move("right") # Example
        for en in self.env:
            continue

    def draw(self):
        # Clean the screen
        self.screen.fill((0,100,0))
        # Draw the items in the screen
        self.player.draw(self.screen, self.bbox)
        for item in self.env:
            item.draw(self.screen,self.bbox)

    def collision_mngr(self):
        self.player.rect.collidelist(self.env)

    def event_mngr(self, keys):
        if keys[pygame.K_DOWN]:
            self.player.set_facing("front")
            self.player.move((0,-self.player.speed))
            if self.player.pos[1]<self.bbox[3]:
                load_tile("down",self.bbox,self.screen_height,self.screen_width)

        if keys[pygame.K_UP]:
            self.player.set_facing("back")
            self.player.move((0,self.player.speed))
            if self.player.pos[1]>self.bbox[2]:
                load_tile("up",self.bbox,self.screen_height,self.screen_width)

        if keys[pygame.K_LEFT]:
            self.player.set_facing("left")
            self.player.move((-self.player.speed,0))
            if self.player.pos[0]<self.bbox[0]:
                load_tile("left",self.bbox,self.screen_height,self.screen_width)

        if keys[pygame.K_RIGHT]:
            self.player.set_facing("right")
            self.player.move((self.player.speed,0))
            if self.player.pos[0]>self.bbox[1]:
                load_tile("right",self.bbox,self.screen_height,self.screen_width)
                    