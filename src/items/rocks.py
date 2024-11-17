from ..items.entities import StaticItem

class Rock(StaticItem):
    """Rock class"""
    def __init__(self, name, pos, img_name="rock"):
        size = (64,64)
        super().__init__(name, pos, size, img_name)

class Quartz(Rock):
    def __init__(self, pos):
        name = "Rock"
        super().__init__(name, pos)