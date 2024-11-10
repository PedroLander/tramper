import pygame
from items import Human, Rock

class Game():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 400

        pygame.init()
        screen = pygame.display.set_mode(
                (self.screen_width,self.screen_height))

        h1 = Human([0,0])
        r1 = Rock((100,100))
        items = [h1, r1]

        background = pygame.Surface(
                (self.screen_width,self.screen_height))

        pygame.font.init()
        my_font = pygame.font.SysFont('Arial', 15)
    
        def pos_to_pix(pos):
        #transform possition to pixels
            return (pos[0]+(self.screen_width//2),pos[1]+self.screen_height//2)

        running = True
    
        while running :

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((100,155,100))

            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_DOWN]:
                h1.set_facing("front")
                h1.move((0,0.2))
            if keys[pygame.K_UP]:
                h1.set_facing("back")
                h1.move((0,-0.2))
            if keys[pygame.K_LEFT]:
                h1.set_facing("left")
                h1.move((-0.2,0))
            if keys[pygame.K_RIGHT]:
                h1.set_facing("right")
                h1.move((0.2,0))

            #image_rect = s_views[facing].get_rect()
            #image_rect.center = pos_to_pix(items[0]["pos"])
            screen.blits([(item.img,pos_to_pix(item.pos)) for item in items])

            pygame.display.flip()

