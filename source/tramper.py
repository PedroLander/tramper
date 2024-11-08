import pygame

class Game():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 400

        pelayo = {"kind":"sheriff", "views":True, "pos":[0,0],"scale":6,
                "view":None, rect:None}
        rock1 = {"kind":"rock","views":False, "pos":[-100,-100],"scale":3,
                "view":None, rect:None}
        rock2 = {"kind":"rock","views":False, "pos":[-150,200],"scale":3,
                "view":None, rect:None}
        items = [pelayo, rock1, rock2]
    
        pygame.init()
        screen = pygame.display.set_mode(
                (self.screen_width,self.screen_height))

        background = pygame.Surface(
                (self.screen_width,self.screen_height))

        pygame.font.init()
        my_font = pygame.font.SysFont('Arial', 15)
    
        def pos_to_pix(pos):
        #transform possition to pixels
            return (pos[0]+(self.screen_width//2),pos[1]+self.screen_height//2)

        for item in items:

            if item["views"]==True:
            #load sheriff views
                s_views = {}
                for view in ["front","back","left","right"]:
                    image = pygame.image.load("images/icons/{0}_{1}.png"
                            .format(item["kind"],view))
                    image_width, image_height = image.get_size()
                    new_size = (int(image_width*item["scale"]),
                        int(image_height*item["scale"]))  
                    image = pygame.transform.scale(image, new_size)
                    s_views[view] = image.convert_alpha()
            elif item["views"]==False:
                image = pygame.image.load("images/icons/{0}1.png"
                        .format(item["kind"]))
                image_width, image_height = image.get_size()
                new_size = (int(image_width*item["scale"]),
                    int(image_height*item["scale"]))
                image = pygame.transform.scale(image, new_size)
                item["rect"] = image.get_rect()



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
                items[0]["pos"][1]+=.2
            if keys[pygame.K_UP]:
                facing = "back"
                items[0]["pos"][1]-=.2
            if keys[pygame.K_LEFT]:
                facing = "left"
                items[0]["pos"][0]-=.2
            if keys[pygame.K_RIGHT]:
                facing = "right"
                items[0]["pos"][0]+=.2

            image_rect = s_views[facing].get_rect()
            image_rect.center = pos_to_pix(items[0]["pos"])
            screen.blits(blit_sequence=(
                (item["rect"] for item in items)))

            pygame.display.flip()

