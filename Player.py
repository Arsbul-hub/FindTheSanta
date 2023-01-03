import keyboard
import pygame.time


class Player:
    def __init__(self, level, screen_size):
        self.screen_size = screen_size
        self.level = level
        self.displayed_items = (10, 10)

        self.item_size = int(self.screen_size[0] / self.displayed_items[0]), int(
            self.screen_size[1] / self.displayed_items[1])
        self.x, self.y = self.get_spawn()[0] * self.item_size[0], self.get_spawn()[1] * self.item_size[1]

        self.hitbox_size = (30, 30)
        self.speed = 0
        self.colliders = []
        self.s = self.item_size[0]

    def move_up(self):
        try:
            if keyboard.is_pressed("w") and self.level[int((self.y - self.speed) / self.item_size[1])][
                int(self.x / self.item_size[0])] == 0 and \
                    self.level[int((self.y - self.speed) / self.item_size[1])][
                        int((self.x + self.hitbox_size[0]) / self.item_size[0])] == 0:
                self.y -= self.speed
        except IndexError:
            pass

    def move_down(self):
        try:

            if self.level[int((self.y + self.hitbox_size[1] + self.speed) / self.item_size[1])][
                        int(self.x / self.item_size[0])] == 0 and \
                    self.level[int((self.y + self.hitbox_size[1] + self.speed) / self.item_size[1])][
                        int((self.x + self.hitbox_size[0]) / self.item_size[0])] == 0:
                self.y += self.speed
        except IndexError:
            pass

    def move_right(self):
        try:
            if self.level[int((self.y) / self.item_size[1])][
                int((self.x + self.hitbox_size[0] + self.speed) / self.item_size[0])] == 0 and \
                    self.level[int((self.y + self.hitbox_size[1]) / self.item_size[1])][
                        int((self.x + self.hitbox_size[0] + self.speed) / self.item_size[0])] == 0:
                self.x += self.speed
        except IndexError:
            pass

    def move_left(self):
        try:

            if self.level[int((self.y) / self.item_size[1])][
                int((self.x - self.speed) / self.item_size[0])] == 0 and \
                    self.level[int((self.y + self.hitbox_size[1]) / self.item_size[1])][
                        int((self.x - self.speed) / self.item_size[0])] == 0:
                self.x -= self.speed
        except IndexError:
            pass

    def get_spawn(self):
        spawn_cords = (0, 0)

        for i in self.level:
            if "s" in i:
                spawn_cords = i.index("s"), self.level.index(i)
        return spawn_cords
