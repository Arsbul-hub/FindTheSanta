import random

import keyboard
import pygame.time
from config import PLAYER_SPEED, ITEM_SIZE, DISPLAYING_DISTANCE, FULL_BLOCKS, CLOCK, SANTA, CODES, \
    GIFT, MONSTER, WALL
from datetime import datetime


class Entity:
    STOP = 0
    FORWARD = 0
    DOWN = 0
    LEFT = 0
    RIGHT = 0
    NAME = "Entity"

    def __init__(self, screen, level):
        self.x, self.y = (0, 0)
        self.level = level

        self.draw_x, self.draw_y = 0, 0
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
        self.lives = 3

    def __eq__(self, other):
        if self.NAME == other.NAME:
            return True

        return False

    def update(self, event, tick):
        pass

    def on_pygame_event(self, event):
        pass

    def draw(self, texture_position, hitbox_position=None, size=None):
        if self.surf:
            if size:

                surf = pygame.transform.scale(pygame.image.load(self.surf), size)
            else:
                surf = pygame.image.load(self.surf)
            rect = surf.get_rect()
            rect.x, rect.y = texture_position
            self.screen.blit(surf, rect)
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
        for cords in d.keys():
            cx, cy = cords
            item = self.level[int(cy / ITEM_SIZE[1])][int(cx / ITEM_SIZE[0])]

            d[cords] = item["type"]
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
                x, y = entity.x, entity.y
                w, h = entity.HITBOX_SIZE
                cx, cy = cords

                if x < cx < x + w and y < cy < y + h:
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


class Player(Entity):
    NAME = "Player"

    def __init__(self, screen, level):
        super().__init__(screen, level)

        self.show_collider = False
        self.set_position(level.player_spawn[0] * ITEM_SIZE[0], level.player_spawn[1] * ITEM_SIZE[1])
        self.direction = self.STOP
        self.gifts = 0
        self.HITBOX_SIZE = 52, 60

    def on_pygame_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.FORWARD = 1
            if event.key == pygame.K_s:
                self.DOWN = 1
            if event.key == pygame.K_a:
                self.LEFT = 1
            if event.key == pygame.K_d:
                self.RIGHT = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.FORWARD = 0
            if event.key == pygame.K_s:
                self.DOWN = 0
            if event.key == pygame.K_a:
                self.LEFT = 0
            if event.key == pygame.K_d:
                self.RIGHT = 0

    def update(self, event, tick):
        self.surf = f"sprites/player_{self.animation}_{self.sprite_animations_current}.png"

        if (datetime.now() - self.sprite_old_time).total_seconds() >= 0.1 and self.animate:

            if self.sprite_animations_current == 5:
                self.sprite_animations_current = 0
            else:
                self.sprite_animations_current += 1
            self.sprite_old_time = datetime.now()

        self.speed_in_tick = ITEM_SIZE[0] * PLAYER_SPEED * tick / 1000
        self.animate = False

        if self.FORWARD:
            self.move_up()
            self.animate = True
            self.animation = "forward"
        if self.DOWN:
            self.move_down()
            self.animation = "down"
            self.animate = True
        if self.LEFT:
            self.move_left()
            self.animate = True
            self.animation = "left"
        if self.RIGHT:
            self.move_right()
            self.animation = "right"
            self.animate = True
        # self.map_collision_event(self.check_map_collision())
        for cords, block_type in self.check_map_collision().items():

            if block_type == GIFT:
                self.gifts += 1
                self.level.level_map[int(cords[1] / ITEM_SIZE[1])][int(cords[0] / ITEM_SIZE[0])] = CODES[" "]
                break
        for cords, entities in self.check_entity_collision().items():

            for entity in entities:
                # if entity == Mon:
                #     self.lives -= 1
                #     break

                if entity == Santa:
                    self.on_win()
                    break

    def on_win(self):
        pass

    def on_loose(self):
        pass


class Santa(Entity):
    NAME = "Santa"

    def __init__(self, screen, level):
        super().__init__(screen, level)
        self.show_collider = False

        self.direction = self.STOP
        self.gifts = 0

    def update(self, event, tick):
        self.surf = f"textures/santa.png"


class Monster(Entity):
    NAME = "Monster"

    def __init__(self, screen, level):
        super().__init__(screen, level)
        self.show_collider = True
        self.HITBOX_SIZE = 52, 60
        self.cooldown = 0
        self.gifts = 0
        self.up = 1
        self.down = 2
        self.left = 3
        self.right = 4
        self.old_time_switch = datetime(2012, 3, 5, 23, 8, 15)
        self.direction = 2
        self.old_time_rand = datetime.now()

    def update(self, event, tick):
        self.surf = f"textures/santa.png"
        self.speed_in_tick = ITEM_SIZE[0] * 4 * tick / 1000

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
