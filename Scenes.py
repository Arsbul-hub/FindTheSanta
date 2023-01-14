import keyboard
import pygame

from Animation import Animation
from Entities.Entity import Player
from SceneLoader import Scene
from config import ITEM_SIZE, DISPLAYING_DISTANCE, SCREEN_SIZE, SANTA, GIFT, MAIN_FONT, CODES
from pygame_animatedgif import AnimatedGifSprite


class LevelsScene(Scene):
    def __init__(self, scene_loader, level):
        super().__init__(scene_loader)
        self.level = level

        self.player = Player(self.level, scene_loader.screen)
        # self.player.map_collision_event = self.coll_event
        self.player.on_win = self.on_player_win

    def on_player_win(self):
        self.scene_loader.scenes["win_scene"].gifts = self.player.gifts
        self.scene_loader.switch_scene("win_scene")

    def on_pygame_event(self, event):
        for entity in self.level.entities:
            entity.on_pygame_event(event)
        self.player.on_pygame_event(event)

    def update_event(self, event):
        self.scene_loader.screen.fill((0, 0, 0))

        for i in range(int(self.player.y / ITEM_SIZE[1] - DISPLAYING_DISTANCE[1] / 2) - 1,
                       int(self.player.y / ITEM_SIZE[1] + DISPLAYING_DISTANCE[1] / 2) + 1):
            for j in range(int(self.player.x / ITEM_SIZE[0] - DISPLAYING_DISTANCE[0] / 2) - 1,
                           int(self.player.x / ITEM_SIZE[0] + DISPLAYING_DISTANCE[0] / 2) + 1):
                try:

                    if i >= 0 and j >= 0:
                        item = self.level.level_map[i][j]
                        x, y = (j * ITEM_SIZE[0] - self.player.x + (DISPLAYING_DISTANCE[0] / 2) * ITEM_SIZE[0],
                                i * ITEM_SIZE[1] - self.player.y + (DISPLAYING_DISTANCE[1] / 2) * ITEM_SIZE[1])
                        h, w = ITEM_SIZE[0], ITEM_SIZE[1]
                        if item["animated"]:

                            item["animation"].load(self.scene_loader.screen, (ITEM_SIZE[0], ITEM_SIZE[1]), (x, y))
                        else:
                            scaled_block = pygame.transform.scale(pygame.image.load(item["texture"]),
                                                                  (ITEM_SIZE[0], ITEM_SIZE[1]))
                            rect = scaled_block.get_rect().move(x, y)
                            self.scene_loader.screen.blit(scaled_block, rect)

                except Exception:
                    pass
        text1 = MAIN_FONT.render(f"Собрано подарков: {self.player.gifts}", True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (0, 0))

        for entity in self.level.entities:
            draw_pos = (entity.x - self.player.x + (DISPLAYING_DISTANCE[0] / 2) * ITEM_SIZE[0],
                        entity.y - self.player.y + (DISPLAYING_DISTANCE[1] / 2) * ITEM_SIZE[1])

            entity.draw(draw_pos, size=ITEM_SIZE)
            entity.update(event)
        self.player.draw((DISPLAYING_DISTANCE[0] / 2 * ITEM_SIZE[0],
                          DISPLAYING_DISTANCE[1] / 2 * ITEM_SIZE[1] - ITEM_SIZE[1] / 2),
                         (DISPLAYING_DISTANCE[0] / 2 * ITEM_SIZE[0],
                          DISPLAYING_DISTANCE[1] / 2 * ITEM_SIZE[1]))
        self.player.update(event)

        self.player.check_entity_collision()


class GameOverScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)


class WinScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)
        self.gifts = 0

    def update_event(self, event):
        self.scene_loader.screen.fill((120, 219, 226))
        text1 = MAIN_FONT.render('Вы победили!', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 120))
        text1 = MAIN_FONT.render(f'Собрано подарков: {self.gifts}', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 100))
