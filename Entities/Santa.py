from Entities import Entity


class Santa(Entity):
    NAME = "Santa"

    def __init__(self, screen, level):
        super().__init__(screen, level)
        self.show_collider = False

        self.size = self.HITBOX_SIZE
        self.direction = self.STOP
        self.gifts = 0

        self.set_surf(f"textures/santa.png", self.HITBOX_SIZE, True)