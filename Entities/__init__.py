from datetime import datetime

import pygame

from ImageLoader import StaticImage
from config import ITEM_SIZE, FULL_BLOCKS


class Entity:
    STOP = 0
    FORWARD = 0
    DOWN = 0
    LEFT = 0
    RIGHT = 0
    NAME = "Entity"

    def __init__(self, screen, level=None):
        self.x, self.y = (0, 0)
        self.level = level

        self.draw_x, self.draw_y = 0, 0
        self.spawn_position = None
        self.speed_in_tick = 0
        self.screen = screen
        self.sprite_animations = []
        self.animation_delay = 0.1
        self.sprite_animations_current = 0
        self.sprite_old_time = datetime(2012, 3, 5, 23, 8, 15)
        self.animate = False
        self.animation = "forward"
        self.show_collider = False
        self.surf = None
        self.HITBOX_SIZE = ITEM_SIZE
        self.size = (0, 0)
        self.lives = 2

        self.spawned = False

    def __eq__(self, other):
        if self.NAME == other.NAME:
            return True

        return False

    def on_update(self, event, tick):
        pass

    def update(self, event, tick):
        if self.spawned:
            self.on_update(event, tick)

    def on_pygame_event(self, event):
        pass

    def set_surf(self, path, size, alpha=False):
        self.surf = StaticImage(path, size, alpha)

    def draw(self, texture_position, hitbox_position=None):
        if self.surf:
            self.surf.draw(self.screen, texture_position)
        if self.show_collider:
            if hitbox_position:
                pygame.draw.rect(self.screen, (0, 255, 0),
                                 (hitbox_position[0],
                                  hitbox_position[1],
                                  self.HITBOX_SIZE[0], self.HITBOX_SIZE[1]), 1)
            else:
                pygame.draw.rect(self.screen, (0, 255, 0),
                                 (texture_position[0],
                                  texture_position[1],
                                  self.HITBOX_SIZE[0], self.HITBOX_SIZE[1]), 1)

    def set_position(self, x, y):
        self.x, self.y = x, y
        if not self.spawn_position:
            self.spawn_position = x, y

    def stop(self):
        self.FORWARD = 0
        self.DOWN = 0
        self.LEFT = 0
        self.RIGHT = 0

    def map_collision_event(self, map_collisions):
        pass

    def entity_collision_event(self, entity_collisions):
        pass

    def check_map_collision(self):
        d = {
            (self.x, self.y - self.speed_in_tick): None,
            (self.x + self.HITBOX_SIZE[0], self.y - self.speed_in_tick): None,

            (self.x, self.y + self.HITBOX_SIZE[1] + self.speed_in_tick): None,
            (self.x + self.HITBOX_SIZE[0], self.y + self.HITBOX_SIZE[1] + self.speed_in_tick): None,

            (self.x - self.speed_in_tick, self.y): None,
            (self.x - self.speed_in_tick, self.y + self.HITBOX_SIZE[1]): None,

            (self.x + self.HITBOX_SIZE[0] + self.speed_in_tick, self.y): None,
            (self.x + self.HITBOX_SIZE[0] + self.speed_in_tick, self.y + self.HITBOX_SIZE[1]): None,

        }
        try:
            for cords in d.keys():
                item = self.level[int(cords[1] / ITEM_SIZE[1])][int(cords[0] / ITEM_SIZE[0])]

                d[cords] = item["type"]

        except IndexError:
            pass

        return d

    def check_entity_collision(self):
        d = {
            (self.x, self.y - self.speed_in_tick): [],
            (self.x + self.HITBOX_SIZE[0], self.y - self.speed_in_tick): [],

            (self.x, self.y + self.HITBOX_SIZE[1] + self.speed_in_tick): [],
            (self.x + self.HITBOX_SIZE[0], self.y + self.HITBOX_SIZE[1] + self.speed_in_tick): [],

            (self.x - self.speed_in_tick, self.y): [],
            (self.x - self.speed_in_tick, self.y + self.HITBOX_SIZE[1]): [],

            (self.x + self.HITBOX_SIZE[0] + self.speed_in_tick, self.y): [],
            (self.x + self.HITBOX_SIZE[0] + self.speed_in_tick, self.y + self.HITBOX_SIZE[1]): [],

        }
        for cords in d.keys():
            for entity in self.level.entities:
                ex, ey = entity.x, entity.y
                w, h = entity.HITBOX_SIZE
                cx, cy = cords

                if ex < cx < ex + w and ey < cy < ey + h:
                    d[cords].append(entity)
        return d

    def can_move(self, go_x, go_y):

        if self.level[int(go_y / ITEM_SIZE[1])][int(go_x / ITEM_SIZE[0])]["type"] not in FULL_BLOCKS:
            return True
        return False

    def move_up(self):
        try:

            if self.can_move(self.x, self.y - self.speed_in_tick) and \
                    self.can_move(self.x + self.HITBOX_SIZE[0], self.y - self.speed_in_tick):
                self.y -= self.speed_in_tick
        except IndexError:
            pass

    def move_down(self):
        try:
            if self.can_move(self.x, self.y + self.HITBOX_SIZE[1] + self.speed_in_tick) and \
                    self.can_move(self.x + self.HITBOX_SIZE[0],
                                  self.y + self.HITBOX_SIZE[1] + self.speed_in_tick):
                self.y += self.speed_in_tick
        except IndexError:
            pass

    def move_right(self):
        try:
            if self.can_move(self.x + self.HITBOX_SIZE[0] + self.speed_in_tick, self.y) and \
                    self.can_move(self.x + self.HITBOX_SIZE[0] + self.speed_in_tick,
                                  self.y + self.HITBOX_SIZE[1]):
                self.x += self.speed_in_tick
        except IndexError:
            pass

    def move_left(self):
        try:
            if self.can_move(self.x - self.speed_in_tick, self.y) and \
                    self.can_move(self.x - self.speed_in_tick,
                                  self.y + self.HITBOX_SIZE[1]):
                self.x -= self.speed_in_tick
        except IndexError:
            pass

    def on_spawned(self):
        self.x, self.y = self.spawn_position

    def on_killed(self):
        pass

    def spawn(self):
        self.spawned = True
        self.on_spawned()

    def kill(self):
        self.spawned = False
        self.on_killed()
