from ..items.entities import StaticItem

class Plant(StaticItem):
    """Plant class"""
    def __init__(self, name, pos, img_name="plant"):
        size = (64,64)
        super().__init__(name, pos, size, img_name)

class Grass(Plant):
    def __init__(self, pos):
        name = "Grass"
        super().__init__(name, pos)

class AchilleaMillefolium(Plant):
    def __init__(self, pos):
        name = "Yarrow"
        img_name = "achillea_millefolium"
        super().__init__(name, pos, img_name)
