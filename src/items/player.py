from src.items.entities import Human

class Player(Human):
    def interact(self, item):
        """Interaction of the player with the item"""
        print (type(item))
        pass