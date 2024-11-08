import pygame

class Game():
    pygame.init()

    screen_width = 500
    screen_height = 400
    screen = pygame.display.set_mode((screen_width,screen_height))

    background = pygame.Surface((screen_width,screen_height))

    pygame.font.init()
    my_font = pygame.font.SysFont('Arial', 15)
    
    #load sheriff views
    s_views = {}
    scale_factor = 6
    rock_scale = 3
    for view in ["front","back","left","right"]:
        image = pygame.image.load("images/icons/sheriff_{}.png".format(view))
        image_width, image_height = image.get_size()
        new_size = (int(image_width*scale_factor),
                int(image_height*scale_factor))  
        image = pygame.transform.scale(image, new_size)
        s_views[view] = image.convert_alpha()
        
        rock = pygame.image.load("images/icons/rock1.png")
        image_width, image_height = rock.get_size()
        new_size = (int(image_width*rock_scale),
                int(image_height*rock_scale))
        rock = pygame.transform.scale(rock, new_size)
        rock_rect = rock.get_rect()
        rock_rect.center = (screen_width // 3, screen_height // 3)


    facing = "front"

    running = True
    
    while running :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((100,155,100))

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_DOWN]:
            facing = "front"
        if keys[pygame.K_UP]:
            facing = "back"
        if keys[pygame.K_LEFT]:
            facing = "left"
        if keys[pygame.K_RIGHT]:
            facing = "right"

        image_rect = s_views[facing].get_rect()
        image_rect.center = (screen_width // 2, screen_height // 2)
        screen.blits(blit_sequence=((s_views[facing], image_rect),(rock,rock_rect)))
        
        

        pygame.display.flip()


        pass
