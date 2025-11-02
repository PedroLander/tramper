from .entities import StaticItem
from config import StaticConfig, dynamic_config
import pygame


class Block(StaticItem):
    """Block class"""
    def __init__(self, name, pos, img_name="block"):
        size = (64, 64, 64)
        super().__init__(name, pos, size, img_name)
        self.img = load_img_2faces(self, img_name, pov_angle=45)

class GrassBlock(Block):
    def __init__(self, pos):
        name = "Grass Block"
        img_name = "try"
        super().__init__(name, pos, img_name)


def load_img_2faces(block: Block, img_base_name, pov_angle=45):
    """
    Loads two faces (top and front) and combines them into one Surface.
    Returns a pygame.Surface.
    """
    img_path = StaticConfig.ICONS_PATH
    top_img = pygame.image.load(img_path + img_base_name + "_top.png").convert_alpha()
    front_img = pygame.image.load(img_path + img_base_name + "_front.png").convert_alpha()

    # Scale both to your zoom (assuming both are 32×32)
    top_img = pygame.transform.scale(top_img, (block.size[0] * dynamic_config.zoom, block.size[1] * dynamic_config.zoom * 0.5 * (pov_angle / 45)))
    front_img = pygame.transform.scale(front_img, (block.size[0] * dynamic_config.zoom, block.size[2] * dynamic_config.zoom * (1 - (0.5 * (pov_angle / 45)))))

    # Create combined surface large enough to hold both
    w = top_img.get_width()
    h = top_img.get_height() + front_img.get_height()
    combined = pygame.Surface((w, h), pygame.SRCALPHA)

    # Draw top first, then front shifted down
    combined.blit(top_img, (0, 0))
    combined.blit(front_img, (0, top_img.get_height()))

    return combined