import keyboard
import pygame

from Player import Player
from SceneLoader import Scene
from config import ITEM_SIZE, DISPLAYING_DISTANCE, SCREEN_SIZE


class LevelsScene(Scene):
    def __init__(self, scene_loader, level):
        super().__init__(scene_loader)
        self.level = level


        self.player = Player(self.level, SCREEN_SIZE, scene_loader.screen)

    def on_pygame_event(self, event):
        pass

    def update_event(self, event):
        self.player.update(event)

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

                        scaled_block = pygame.transform.scale(pygame.image.load(item["base_texture"]),
                                                              (ITEM_SIZE[0], ITEM_SIZE[1]))
                        rect = scaled_block.get_rect().move(x, y)
                        self.scene_loader.screen.blit(scaled_block, rect)



                except:
                    pass

        self.player.draw_player()