import pygame

class Panel(pygame.Surface):
    def __init__(self, config):
        
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        super().__init__((config.TEXT_WIDTH, config.TEXT_HEIGHT))
        
        self.fill((0,0,0))
        
        self.text_surface = self.my_font.render('Some Text', False, (200, 200, 200))
        
        self.blit(self.text_surface, (0,0))

    def show_msg(self, msg):
        self.fill((0,0,0))
        self.text_surface = self.my_font.render(msg, False, (200, 200, 200))
        self.blit(self.text_surface, (0,0))

