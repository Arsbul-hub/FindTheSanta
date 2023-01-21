import pygame

from Entities import Entity
from config import SCREEN_SIZE, ITEM_SIZE


class Main_Screen_Person(Entity):
    NAME = "Player"

    def __init__(self, screen):

        super().__init__(screen)

        self.show_collider = False
        self.x = 110
        self.direction = "right"
        self.surf = f"textures/santa.png"
        self.HITBOX_SIZE = 100, 120
        self.y = SCREEN_SIZE[1] - self.HITBOX_SIZE[1] - 30

    def on_pygame_event(self, event):
        pass

    def update(self, event, tick):

        self.speed_in_tick = ITEM_SIZE[0] * 3 * tick / 1000
        if self.direction == "right":
            self.x += self.speed_in_tick

        else:
            self.x -= self.speed_in_tick

        if self.x >= SCREEN_SIZE[0] - self.HITBOX_SIZE[0]:
            self.direction = "left"

        elif self.x <= 0:
            self.direction = "right"

    def draw(self, texture_position, hitbox_position=None, size=None):
        if self.surf:
            if size:

                if self.direction == "left":
                    surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.surf), size), False, False)

                else:
                    surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.surf), size), True, False)
            else:
                if self.direction == "left":
                    surf = pygame.transform.rotate(pygame.image.load(self.surf), 90)

                else:
                    surf = pygame.image.load(self.surf)

            rect = surf.get_rect()
            rect.x, rect.y = texture_position
            self.screen.blit(surf, rect)