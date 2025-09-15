from .entities import StaticItem

class Block(StaticItem):
    """Block class"""
    def __init__(self, name, pos, img_name="block"):
        size = (64,64)
        super().__init__(name, pos, size, img_name)

class GrassBlock(Block):
    def __init__(self, pos):
        name = "Grass Block"
        img_name = "ground_grass"
        super().__init__(name, pos, img_name)

class StoneBlock(Block):
    def __init__(self, pos):
        name = "Stone Block"
        img_name = "ground_stone"
        super().__init__(name, pos, img_name)

class DirtBlock(Block):
    def __init__(self, pos):
        name = "Dirt Block"
        img_name = "ground_dirt"
        super().__init__(name, pos, img_name)
