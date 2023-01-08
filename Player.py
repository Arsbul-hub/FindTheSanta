import time

import keyboard
import pygame.time
from config import PLAYER_SPEED, ENTITY_HITBOX_SIZE, ITEM_SIZE, DISPLAYING_DISTANCE, FULL_BLOCKS, CLOCK
from datetime import datetime


class Player:
    def __init__(self, level, screen_size, screen):
        self.screen_size = screen_size
        self.level = level
        self.screen = screen
        print(level.player_spawn)
        self.x, self.y = level.player_spawn[0] * ITEM_SIZE[0], level.player_spawn[1] * ITEM_SIZE[1]
        self.speed_in_tick = 0
        self.colliders = []
        self.sprite_animations_forward = [pygame.image.load(f"sprites/player_forward_{i}.png") for i in range(3)]
        self.sprite_animations_current = 0
        self.sprite_old_time = datetime(2012, 3, 5, 23, 8, 15)
        self.animate = False
        self.animation = "forward"
        self.show_collider = False

    def update(self):
        self.speed_in_tick = ITEM_SIZE[0] * PLAYER_SPEED * CLOCK.tick() / 1000
        self.animate = False
        if keyboard.is_pressed("w"):
            self.move_up()
            self.animate = True
            self.animation = "forward"
        if keyboard.is_pressed("s"):
            self.move_down()
            self.animation = "down"
            self.animate = True
        if keyboard.is_pressed("a"):
            self.move_left()
            self.animate = True
            self.animation = "left"
        if keyboard.is_pressed("d"):
            self.move_right()
            self.animation = "right"
            self.animate = True

    def draw_player(self):
        surf = pygame.image.load(f"sprites/player_{self.animation}_{self.sprite_animations_current}.png")
        rect = surf.get_rect()
        rect.x, rect.y = DISPLAYING_DISTANCE[0] / 2 * ITEM_SIZE[0], DISPLAYING_DISTANCE[1] / 2 * ITEM_SIZE[1] - \
                         ITEM_SIZE[1] / 2
        self.screen.blit(surf, rect)

        if (datetime.now() - self.sprite_old_time).total_seconds() >= 0.1 and self.animate:

            if self.sprite_animations_current == 5 - 1:
                self.sprite_animations_current = 0
            else:
                self.sprite_animations_current += 1
            self.sprite_old_time = datetime.now()
        if self.show_collider:
            pygame.draw.rect(self.screen, (0, 255, 0),
                             (DISPLAYING_DISTANCE[0] / 2 * ITEM_SIZE[0],
                              DISPLAYING_DISTANCE[1] / 2 * ITEM_SIZE[1],
                              ENTITY_HITBOX_SIZE[0], ENTITY_HITBOX_SIZE[1]), 1)

    def move_up(self):
        try:

            if self.can_move(self.x, self.y - self.speed_in_tick) and \
                    self.can_move(self.x + ENTITY_HITBOX_SIZE[0], self.y - self.speed_in_tick):
                self.y -= self.speed_in_tick
        except IndexError:
            pass

    def move_down(self):
        try:
            if self.can_move(self.x, self.y + ENTITY_HITBOX_SIZE[1] + self.speed_in_tick) and \
                    self.can_move(self.x + ENTITY_HITBOX_SIZE[0],
                                  self.y + ENTITY_HITBOX_SIZE[1] + self.speed_in_tick):
                self.y += self.speed_in_tick
        except IndexError:
            pass

    def move_right(self):
        try:
            if self.can_move(self.x + ENTITY_HITBOX_SIZE[0] + self.speed_in_tick, self.y) and \
                    self.can_move(self.x + ENTITY_HITBOX_SIZE[0] + self.speed_in_tick,
                                  self.y + ENTITY_HITBOX_SIZE[1]):
                self.x += self.speed_in_tick
        except IndexError:
            pass

    def move_left(self):
        try:
            if self.can_move(self.x - self.speed_in_tick, self.y) and \
                    self.can_move(self.x - self.speed_in_tick,
                                  self.y + ENTITY_HITBOX_SIZE[1]):
                self.x -= self.speed_in_tick
        except IndexError:
            pass

    def get_spawn(self):
        spawn_cords = (0, 0)

        for i in self.level:
            if "s" in i:
                spawn_cords = i.index("s"), self.level.index(i)
        return spawn_cords

    def can_move(self, go_x, go_y):

        if self.level[int(go_y / ITEM_SIZE[1])][int(go_x / ITEM_SIZE[0])]["type"] not in FULL_BLOCKS:
            return True
        return False
