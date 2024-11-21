"""Main module to execute for running the game"""
import pygame
from src.engine.loop import MainLoop
from config import Configuration

def main():
    """Main function. Executes the screen and the main loop of the game"""
    config = Configuration()
    pygame.init()
    screen = pygame.display.set_mode(
        (config.display_width, config.display_height))
    loop = MainLoop(config, screen)
    loop.run(config)

if __name__=="__main__":
    main()
