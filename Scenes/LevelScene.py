import time
from datetime import datetime, time, timedelta

import pygame.draw

from Entities.Player import Player
from ImageLoader import StaticImage
from Scenes import Scene
from Widgets import Button
from config import ITEM_SIZE, DISPLAYING_DISTANCE, SCREEN_SIZE, MAIN_FONT, CLOCK, TEXTURES, CODES


class LevelsScene(Scene):
    def __init__(self, scene_loader, level):
        super().__init__(scene_loader)
        self.level = level

        self.player = Player(scene_loader.screen, self.level)
        # self.player.map_collision_event = self.coll_event

        self.player_health_icon = StaticImage("textures/health.png", (20, 20), True)

        self.player.on_win = self.on_player_win
        self.player.on_loose = self.on_player_loose
        self.gifts_icon_num = StaticImage("textures/gift.png", (70, 70), True)
        self.quit_btn = Button(self.scene_loader.screen, (0, 0), (100, 100), "Выйти")
        self.notification_text = ""
        self.player.on_end_game_failed = self.on_end_game_failed
        self.notification_opacity = 0

    def on_end_game_failed(self):
        self.notify(f"Ох, ты собрал не все подарки... ({self.player.gifts} из {self.level.gifts})")

    def on_switch(self):
        for entity in self.level.entities:
            entity.spawn()
        self.player.spawn()

    def on_player_win(self):
        self.scene_loader.scenes["win_scene"].gifts = self.player.gifts
        self.scene_loader.switch_scene("win_scene")

    def on_player_loose(self):
        # self.scene_loader.scenes["loose_scene"].gifts = self.player.gifts
        self.scene_loader.switch_scene("game_over_scene")

    def on_pygame_event(self, event):
        for entity in self.level.entities:
            entity.on_pygame_event(event)
        self.player.on_pygame_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.quit_btn.is_clicked(event.pos):
                for entity in self.level.entities:
                    entity.kill()
                self.player.kill()
                self.scene_loader.switch_scene("all_levels_scene")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3:
                self.player.god_mode = True
                self.notify("Режим Артёма активен! (Вы неуязвимы!)")

    def update_event(self, event):

        self.scene_loader.screen.fill((242, 237, 241))
        tick = CLOCK.tick()
        # Отрисовка 1 слоя карты
        self.draw_first_layer()
        player_draw_cords = self.player.x - self.player.x + (DISPLAYING_DISTANCE[0] / 2) * ITEM_SIZE[
            0], self.player.y - self.player.y + (DISPLAYING_DISTANCE[1] / 2) * ITEM_SIZE[1]
        for entity in self.level.entities:
            draw_pos = (entity.x - self.player.x + (DISPLAYING_DISTANCE[0] / 2) * ITEM_SIZE[0],
                        entity.y - self.player.y + (DISPLAYING_DISTANCE[1] / 2) * ITEM_SIZE[1])

            entity.draw(draw_pos)
            entity.on_update(event, tick)
        self.player.draw(player_draw_cords)
        # Отрисовка 2 слоя карты
        self.draw_second_layer()
        # Обновление игрока
        self.player.on_update(event, tick)
        # Отрисовка остальных объектов

        fps_text = MAIN_FONT.render(f"fps: {round(CLOCK.get_fps(), 1)}", True, (200, 0, 0))

        self.scene_loader.screen.blit(fps_text, (SCREEN_SIZE[0] - fps_text.get_rect().width - 10, 0))

        for lives in range(self.player.lives):  # Количество сердец
            self.player_health_icon.draw(self.scene_loader.screen,
                                         (self.player_health_icon.size[0] * lives + player_draw_cords[0] +
                                          self.player.HITBOX_SIZE[0] / 2 - (
                                                  self.player_health_icon.size[1] * self.player.lives) / 2,
                                          player_draw_cords[1] - 30))

        bar_height = 20

        pygame.draw.rect(self.scene_loader.screen, (255, 0, 0), (
            SCREEN_SIZE[0] / 2 - self.player.speed_boost * 30 / 2, SCREEN_SIZE[1] - bar_height,
            self.player.speed_boost * 30, bar_height))
        self.gifts_icon_num.draw(self.scene_loader.screen, (0, SCREEN_SIZE[1] - self.gifts_icon_num.size[1]))
        text1 = MAIN_FONT.render(f"""{self.player.gifts} из {self.level.gifts}""", True, (0, 0, 0))
        self.scene_loader.screen.blit(text1, (
            self.gifts_icon_num.size[0], SCREEN_SIZE[1] - self.gifts_icon_num.size[1] - text1.get_height()))
        minutes, seconds = self.player.get_loose_time()

        if int(minutes) == 0 and int(seconds) <= 30:

            text1 = MAIN_FONT.render(f"""Осталось времени: {minutes}:{seconds}""", True, (255, 0, 0))
            self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] / 2 - text1.get_width() / 2, 0))
        else:
            text1 = MAIN_FONT.render(f"""Осталось времени: {minutes}:{seconds}""", True, (0, 0, 0))
            self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] / 2 - text1.get_width() / 2, 0))
        text1 = MAIN_FONT.render(self.notification_text,
                                 True, (0, 0, 0))
        text1.set_alpha(self.notification_opacity)
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] / 2 - text1.get_width() / 2,
                                              SCREEN_SIZE[1] - 100))

        if self.notification_opacity > 0:
            self.notification_opacity -= 70 * tick / 1000
        self.quit_btn.draw_button()

    def draw_first_layer(self):
        for i in range(int(self.player.y / ITEM_SIZE[1] - DISPLAYING_DISTANCE[1] / 2) - 5,
                       int(self.player.y / ITEM_SIZE[1] + DISPLAYING_DISTANCE[1] / 2) + 5):
            for j in range(int(self.player.x / ITEM_SIZE[0] - DISPLAYING_DISTANCE[0] / 2) - 5,
                           int(self.player.x / ITEM_SIZE[0] + DISPLAYING_DISTANCE[0] / 2) + 5):
                try:

                    if i >= 0 and j >= 0:
                        item = self.level.level_map[i][j]
                        x, y = (j * ITEM_SIZE[0] - self.player.x + (DISPLAYING_DISTANCE[0] / 2) * ITEM_SIZE[0],
                                i * ITEM_SIZE[1] - self.player.y + (DISPLAYING_DISTANCE[1] / 2) * ITEM_SIZE[1])
                        h, w = ITEM_SIZE[0], ITEM_SIZE[1]

                        if not item["second_layer"]:

                            CODES[" "]["texture"].draw(self.scene_loader.screen, (x, y))
                            item["texture"].draw(self.scene_loader.screen,
                                                 (x - item["texture"].size[0] / 2 + ITEM_SIZE[0] / 2,
                                                  y - item["texture"].size[1] + ITEM_SIZE[1]))

                        else:

                            CODES[" "]["texture"].draw(self.scene_loader.screen, (x, y))

                except IndexError:
                    pass

    def draw_second_layer(self):
        for i in range(int(self.player.y / ITEM_SIZE[1] - DISPLAYING_DISTANCE[1] / 2) - 5,
                       int(self.player.y / ITEM_SIZE[1] + DISPLAYING_DISTANCE[1] / 2) + 5):
            for j in range(int(self.player.x / ITEM_SIZE[0] - DISPLAYING_DISTANCE[0] / 2) - 5,
                           int(self.player.x / ITEM_SIZE[0] + DISPLAYING_DISTANCE[0] / 2) + 5):
                try:

                    if i >= 0 and j >= 0:
                        item = self.level.level_map[i][j]
                        x, y = (j * ITEM_SIZE[0] - self.player.x + (DISPLAYING_DISTANCE[0] / 2) * ITEM_SIZE[0],
                                i * ITEM_SIZE[1] - self.player.y + (DISPLAYING_DISTANCE[1] / 2) * ITEM_SIZE[1])
                        h, w = ITEM_SIZE[0], ITEM_SIZE[1]
                        if item["second_layer"]:
                            item["texture"].draw(self.scene_loader.screen,
                                                 (x - item["texture"].size[0] / 2 + ITEM_SIZE[0] / 2,
                                                  y - item["texture"].size[1] + ITEM_SIZE[1]))

                except IndexError:
                    pass
    def notify(self, text):
        self.notification_text = text
        self.notification_opacity = 255