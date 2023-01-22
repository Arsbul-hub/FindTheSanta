from Entities import Entity
from config import ITEM_SIZE


class Santa(Entity):
    NAME = "Santa"

    def __init__(self, screen, level):
        super().__init__(screen, level)
        self.show_collider = False

        self.HITBOX_SIZE = ITEM_SIZE[0], ITEM_SIZE[1] + 20
        self.direction = self.STOP
        self.gifts = 0

        self.set_surf(f"textures/santa.png", self.HITBOX_SIZE, True)