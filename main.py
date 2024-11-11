"""Main module to execute for running the game"""
import pygame
from src.engine.loop import MainLoop
from config import Configuration

def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (Configuration.WIDTH, Configuration.HEIGHT))
    loop = MainLoop(screen)
    loop.run()

if __name__=="__main__":
    main()
