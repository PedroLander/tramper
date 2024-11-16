from ..items.entities import StaticItem

class Rock(StaticItem):
    """Rock class"""
    def __init__(self, pos, img_name="rock"):
        size = (64,64)
        super().__init__(pos, size, img_name)

class Quartz(Rock):
    pass