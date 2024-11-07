import pygame

class Game():
    pygame.init()
    
    screen_width = 500
    screen_height = 400
    screen = pygame.display.set_mode((screen_width,screen_height))
    
    background = pygame.Surface((screen_width,screen_height))

    pygame.font.init()
    my_font = pygame.fond.SysFont('Arial', 15)

    clock = pygame.time.Clock()


    running = True

    while running :

        for event in pygame.event.get():
            if event.type == pygame.QUIT
            running = False

        keys = pygame.key.get_pressed()

        pass
