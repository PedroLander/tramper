import pygame

class Layout(pygame.Surface):
    def __init__(self, config):
        
        super().__init__((config.display_width, config.display_height))
        
        self.surface1 = pygame.Surface((config.surface1_width,config.surface1_height))
        self.surface2 = pygame.Surface((config.surface2_width,config.surface2_height))
        self.surface3 = pygame.Surface((config.surface3_width,config.surface3_height))

        self.font = 'Comic Sans MS'
        self.font_size = 20
        self.font_colour = (200,200,200)

        self.my_font = pygame.font.SysFont(self.font, self.font_size)

        self.options_surface = pygame.Surface((self.surface3.get_width(),
                                              self.surface3.get_height()))
        self.message_surface = pygame.Surface((self.surface2.get_width(),
                                               self.surface2.get_height()))
        self.inventory_surface = pygame.Surface((self.surface1.get_width(),
                                                self.surface1.get_height()))

        init_msg = ["Welcome to Tramper!"]
        init_options = ["<Arrows>: move",
                        "<e>: grab things"]

        self.show_msg(init_msg, config)
        self.show_options(init_options, config)

    def blit_pans(self,config):
        self.blit(self.surface1,(config.surface1_x_pos,config.surface1_y_pos))
        self.blit(self.surface2,(config.surface2_x_pos,config.surface2_y_pos))
        self.blit(self.surface3,(config.surface3_x_pos,config.surface3_y_pos))

    def show_msg(self, msg:list, config) -> None:
        self.message_surface.fill((0,0,50))
        self.multiline_blit(self.message_surface, msg)
        self.surface2.blit(self.message_surface,(0,0))
        self.blit_pans(config)

    def show_options(self, options:list, config) -> None:
        self.options_surface.fill((50,0,0))
        self.multiline_blit(self.options_surface, options)
        self.surface3.blit(self.options_surface,(0,0))
        self.blit_pans(config)

    def show_inventory(self, inv:list, config) -> None:
        self.inventory_surface.fill((0,50,0))
        self.multiline_blit(self.inventory_surface, inv)
        self.surface1.blit(self.inventory_surface,(0,0))
        self.blit_pans(config)


    def multiline_blit(self, surface, text):
        """Method for rendering a multiple line text in a pygame Surface 
        object"""
        pos_x = (surface.get_width() * 1/10)
        pos_y = (surface.get_height() * 1/10)
        position = pos_x, pos_y

        label = []
        for line in text: 
            label.append(self.my_font.render(str(line), True, self.font_colour))

        for line in enumerate(label):
            surface.blit(line[1],(position[0],position[1]+(line[0]*self.font_size)+(5*line[0])))
