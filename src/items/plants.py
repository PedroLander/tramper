from ..items.entities import StaticItem

class Plant(StaticItem):
    """Plant class"""
    def __init__(self, pos, img_name="plant"):
        size = (64,64)
        super().__init__(pos, size, img_name)

class Grass(Plant):
    pass