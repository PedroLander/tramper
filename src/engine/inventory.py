import pygame

class Inventory(pygame.Surface):
    def __init__(self, mainloop):

        pos_x = int(mainloop.screen.get_width() * 1/10)
        pos_y = int(mainloop.screen.get_height() * 1/10)
        super().__init__(pos_x,pos_y)
        inventory_font = pygame.font.SysFont("Comic Sans MS", 20, (220,180,180))
        inventory_text = inventory_font.render("Inventory---", Truem, (200,200,200))
        self.blit(inventory_text, (0,0))
        mainloop.running = False
        
        keys = pygame.key.get()
        if keys == pygame.K_ESCAPE:
            mainloop.running=True