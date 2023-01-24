import random
from datetime import datetime

from Entities import Entity
from config import ITEM_SIZE, MONSTERS_SPEED


class Monster(Entity):
    NAME = "Monster"

    def __init__(self, screen, level):
        super().__init__(screen, level)
        self.show_collider = True
        self.HITBOX_SIZE = 70, 70
        self.cooldown = 0
        self.gifts = 0
        self.up = 1
        self.down = 2
        self.left = 3
        self.right = 4
        self.old_time_switch = datetime(2012, 3, 5, 23, 8, 15)
        self.direction = 2
        self.old_time_rand = datetime.now()
        self.size = self.HITBOX_SIZE
        self.set_surf("textures/monster.png", self.HITBOX_SIZE, True)

    # def on_spawned(self):
    #
    #     self.set_position(level.player_spawn[0] * ITEM_SIZE[0], level.player_spawn[1] * ITEM_SIZE[1])
    def on_update(self, event, tick):

        self.speed_in_tick = ITEM_SIZE[0] * MONSTERS_SPEED * tick / 1000

        if self.direction == self.up:
            self.move_up()

        if self.direction == self.down:
            self.move_down()

        if self.direction == self.left:
            self.move_left()

        if self.direction == self.right:
            self.move_right()
        # self.move_up()

    def move_up(self):
        try:

            if self.can_move(self.x, self.y - self.speed_in_tick) and \
                    self.can_move(self.x + self.HITBOX_SIZE[0], self.y - self.speed_in_tick):
                self.y -= self.speed_in_tick
                if (datetime.now() - self.old_time_rand).total_seconds() > 3 and random.choice([True, False]):
                    self.direction = random.choice([self.down, self.left, self.right])
                    self.old_time_rand = datetime.now()
            elif (datetime.now() - self.old_time_switch).total_seconds() > self.cooldown:
                self.direction = random.choice([self.down, self.left, self.right])

                self.old_time_switch = datetime.now()

        except IndexError:
            pass

    def move_down(self):
        try:
            if self.can_move(self.x, self.y + self.HITBOX_SIZE[1] + self.speed_in_tick) and \
                    self.can_move(self.x + self.HITBOX_SIZE[0],
                                  self.y + self.HITBOX_SIZE[1] + self.speed_in_tick):
                self.y += self.speed_in_tick
                if (datetime.now() - self.old_time_rand).total_seconds() > 3 and random.choice([True, False]):
                    self.direction = random.choice([self.up, self.left, self.right])
                    self.old_time_rand = datetime.now()
            elif (datetime.now() - self.old_time_switch).total_seconds() > self.cooldown:
                self.direction = random.choice([self.up, self.left, self.right])

                self.old_time_switch = datetime.now()
        except IndexError:
            pass

    def move_right(self):
        try:

            if self.can_move(self.x + self.HITBOX_SIZE[0] + self.speed_in_tick, self.y) and \
                    self.can_move(self.x + self.HITBOX_SIZE[0] + self.speed_in_tick,
                                  self.y + self.HITBOX_SIZE[1]):
                self.x += self.speed_in_tick
                if (datetime.now() - self.old_time_rand).total_seconds() > 3 and random.choice([True, False]):
                    self.direction = random.choice([self.up, self.down, self.left])
                    self.old_time_rand = datetime.now()
            elif (datetime.now() - self.old_time_switch).total_seconds() > self.cooldown:
                self.direction = random.choice([self.up, self.down, self.left])

                self.old_time_switch = datetime.now()
        except IndexError:
            pass

    def move_left(self):
        try:
            if self.can_move(self.x - self.speed_in_tick, self.y) and \
                    self.can_move(self.x - self.speed_in_tick,
                                  self.y + self.HITBOX_SIZE[1]):
                self.x -= self.speed_in_tick
                if (datetime.now() - self.old_time_rand).total_seconds() > 3 and random.choice([True, False]):
                    self.direction = random.choice([self.up, self.down, self.right])
                    self.old_time_rand = datetime.now()
            elif (datetime.now() - self.old_time_switch).total_seconds() > self.cooldown:
                self.direction = random.choice([self.up, self.down, self.right])

                self.old_time_switch = datetime.now()

        except IndexError:
            pass
