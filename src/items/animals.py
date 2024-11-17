from ..items.entities import MovingItem

class Animal(MovingItem):
    """Animal class"""
    def __init__(self, name, pos, size=(64,64), init_facing="down", speed=1, img_name="redfox", frec_movement=0.1):
        super().__init__(name, pos, size, init_facing, speed, img_name, frec_movement)

class RedFox(Animal):
    """Fox class"""
    def __init__(self, pos):
        name = "Red Fox"
        size = (64,64)
        init_facing = "left"
        speed = 1
        img_name = "redfox"
        frec_movement = 0.4
        

        super().__init__(name, pos, size, init_facing, speed, img_name, frec_movement)
    