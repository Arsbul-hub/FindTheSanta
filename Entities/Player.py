from datetime import datetime

import pygame

from Entities import Entity
from Entities.Santa import Santa
from config import ITEM_SIZE, PLAYER_SPEED, INTERACTIVE, CODES, PLAYER_SPEED_BOOST


class Player(Entity):
    NAME = "Player"
    SPEED_BOOST = 0

    def __init__(self, screen, level):
        super().__init__(screen, level)

        self.show_collider = False
        self.set_position(level.player_spawn[0] * ITEM_SIZE[0], level.player_spawn[1] * ITEM_SIZE[1])
        self.direction = self.STOP
        self.gifts = 0
        self.HITBOX_SIZE = 60, 100
        self.lives_cooldown = 1
        self.old_hit_time = datetime(2012, 3, 5, 23, 8, 15)
        # self.can_rift = True
        # self.rift_target_pos = None
        # self.rift_direction = None
        self.speed = PLAYER_SPEED
        self.speed_boost = 10
        self.old_speed_boost = datetime(2012, 3, 5, 23, 8, 15)  # время старого отнимание шкалы

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
            if event.key == pygame.K_LSHIFT:
                self.SPEED_BOOST = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.FORWARD = 0
            if event.key == pygame.K_s:
                self.DOWN = 0
            if event.key == pygame.K_a:
                self.LEFT = 0
            if event.key == pygame.K_d:
                self.RIGHT = 0
            if event.key == pygame.K_LSHIFT:
                self.SPEED_BOOST = 0

    def update(self, event, tick):
        self.set_surf(f"sprites/player_{self.animation}_{self.sprite_animations_current}.png", self.HITBOX_SIZE, True)

        if (datetime.now() - self.sprite_old_time).total_seconds() >= 0.1 and self.animate:

            if self.sprite_animations_current == 5:
                self.sprite_animations_current = 0
            else:
                self.sprite_animations_current += 1

            self.sprite_old_time = datetime.now()

        self.speed_in_tick = ITEM_SIZE[0] * self.speed * tick / 1000
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
        if self.SPEED_BOOST and 1 in [self.FORWARD, self.DOWN, self.RIGHT, self.LEFT]:
            if self.speed_boost > 0:
                self.speed = PLAYER_SPEED_BOOST

                self.speed_boost -= 3 * tick / 1000

            else:
                self.speed = PLAYER_SPEED
        elif not self.SPEED_BOOST:
            self.speed = PLAYER_SPEED
            if self.speed_boost < 10:
                self.speed_boost += 1 * tick / 1000

        for cords, block_type in self.check_map_collision().items():

            if block_type == INTERACTIVE:
                self.gifts += 1
                self.level.level_map[int(cords[1] / ITEM_SIZE[1])][int(cords[0] / ITEM_SIZE[0])] = CODES[" "]
                break
        for cords, entities in self.check_entity_collision().items():

            for entity in entities:
                if entity.NAME == "Monster" and (
                        datetime.now() - self.old_hit_time).total_seconds() > 1 and self.lives > 0:

                    self.lives -= 1
                    self.old_hit_time = datetime.now()

                    break
                elif self.lives <= 0:
                    self.on_loose()
                    break
                if entity.NAME == "Santa":
                    self.on_win()
                    break

    # def do_rift(self, tick):
    #     if self.can_rift:
    #         if self.FORWARD:
    #             self.rift_target_pos = (self.x, self.y - 20)
    #             self.rift_direction = "forward"
    #         elif self.DOWN:
    #             self.rift_target_pos = (self.x, self.y + 20)
    #             self.rift_direction = "down"
    #
    #         elif self.RIGHT:
    #             self.rift_target_pos = (self.x + 20, self.y)
    #             self.rift_direction = "right"
    #         elif self.LEFT:
    #             self.rift_target_pos = (self.x - 20, self.y)
    #             self.rift_direction = "left"
    #         else:
    #             self.rift_target_pos = (self.x, self.y - 20)
    #             self.rift_direction = "forward"
    #         self.can_rift = False
    #     else:
    #         if self.rift_direction == "forward" and self.y > self.rift_target_pos[1]:
    #             self.y -= ITEM_SIZE[0] * PLAYER_SPEED * tick / 1000
    #         elif self.rift_direction == "down" and self.y < self.rift_target_pos[1]:
    #             self.y += ITEM_SIZE[0] * PLAYER_SPEED * tick / 1000
    #         elif self.rift_direction == "left" and self.x > self.rift_target_pos[0]:
    #             self.x -= ITEM_SIZE[0] * PLAYER_SPEED * tick / 1000
    #         elif self.rift_direction == "right" and self.x > self.rift_target_pos[0]:
    #             self.x += ITEM_SIZE[0] * PLAYER_SPEED * tick / 1000
    #         else:
    #             self.can_rift = True

    def on_win(self):
        pass

    def on_loose(self):
        pass
