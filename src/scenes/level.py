import pygame
from ..items.player import Player
from ..items.plants import Quartz

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player((100, 100))
        self.env = [Quartz((300,100)),Quartz((-200,50))]
        width = self.screen.get_width()
        height = self.screen.get_height()
        self.bbox = [-width//2, width//2, height//2, -height//2]

    def update(self):
        #Updates all item's state
        #self.player.move("right") # Example
        for en in self.env:
            continue

    def draw(self):
        # Draw the items in the screen
        self.screen.fill((255,255,255)) # Clean screen
        pygame.display.flip()
        self.player.draw(self.screen)

    def collision_mngr(self):
        self.player.rect.collidelist(self.env)

    def event_mngr(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.player.set_facing("front")

                self.player.move((0,-self.player.speed))
                if self.player.pos[1]<self.bbox[3]:
                    self.load_tile("down")

            if event.key == pygame.K_UP:
                self.player.set_facing("back")

                self.player.move((0,self.player.speed))
                if self.player.pos[1]>self.bbox[2]:
                    self.load_tile("up")

            if event.key == pygame.K_LEFT:
                self.player.set_facing("left")
                
                self.player.move((-self.player.speed,0))
                if self.player.pos[0]<self.bbox[0]:
                    self.load_tile("left")

            if event.key == pygame.K_RIGHT:
                self.player.set_facing("right")

                self.player.move((self.player.speed,0))
                if self.player.pos[0]>self.bbox[1]:
                    self.load_tile("right")
                    