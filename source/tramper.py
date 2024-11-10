"""Module that contains the main game class"""

import pygame
from items import Human, Rock
from funcs import pos_to_pix

class Game():
    """The main game class"""
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 400
        self.clock = pygame.time.Clock()

        self.bbox = [-self.screen_width//2, self.screen_width//2,
                     self.screen_height//2, -self.screen_height//2]
        getattr(pygame, "init")()
        screen = pygame.display.set_mode(
                (self.screen_width,self.screen_height))

        h1 = Human([0,0])
        r1 = Rock((100,100))
        items = [h1, r1]

        background = pygame.Surface(
                (self.screen_width,self.screen_height))

        pygame.font.init()
        my_font = pygame.font.SysFont('Arial', 15)

        running = True
        while running :
            #The optional argument limits the fps (not very accurate).
            self.clock.tick(40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((100,155,100))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                h1.set_facing("front")
                h1.move((0,-h1.speed))
                if h1.pos[1]<self.bbox[3]:
                    self.load_tile("down")
            if keys[pygame.K_UP]:
                h1.set_facing("back")
                h1.move((0,h1.speed))
                if h1.pos[1]>self.bbox[2]:
                    self.load_tile("up")
            if keys[pygame.K_LEFT]:
                h1.set_facing("left")
                h1.move((-h1.speed,0))
                if h1.pos[0]<self.bbox[0]:
                    self.load_tile("left")
            if keys[pygame.K_RIGHT]:
                h1.set_facing("right")
                h1.move((h1.speed,0))
                if h1.pos[0]>self.bbox[1]:
                    self.load_tile("right")
            screen.blits([(item.img,pos_to_pix(
                self.bbox,item.pos,item.size)) for item in items])

            pygame.display.flip()

    def load_tile(self, side):
        """Updates the object bounding box after pressing a key"""
        match side:
            case "down":
                self.bbox[2]=self.bbox[3]
                self.bbox[3]=self.bbox[3]-self.screen_height
            case "up":
                self.bbox[3]=self.bbox[2]
                self.bbox[2]=self.bbox[2]+self.screen_height
            case "left":
                self.bbox[1]=self.bbox[0]
                self.bbox[0]=self.bbox[0]-self.screen_width
            case "right":
                self.bbox[0]=self.bbox[1]
                self.bbox[1]=self.bbox[1]+self.screen_width
