"""Main module to execute for running the game"""
import pygame

from config import dynamic_config
from src.engine.loop import MainLoop

def main():
    """Main function. Executes the screen and the main loop of the game"""
    pygame.init()

    screen = pygame.display.set_mode(
        (dynamic_config.display_width, dynamic_config.display_height))
    
    loop = MainLoop(screen)

    loop.run()

if __name__=="__main__":
    main()
