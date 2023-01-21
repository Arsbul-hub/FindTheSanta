import pygame

from Scenes import Scene
from config import SCREEN_SIZE, MAIN_FONT


class AllLevelsScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)

    def update_event(self, event):
        self.scene_loader.screen.fill((0, 0, 0))
        text1 = MAIN_FONT.render('Для выбора уровня нажмите на соответствующую клваишу', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 120))
        text1 = MAIN_FONT.render('1', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 80))
        text1 = MAIN_FONT.render('2', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 40))
        text1 = MAIN_FONT.render('3', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2))

    def on_pygame_event(self, event):

        if event.type == pygame.KEYDOWN:

            self.scene_loader.switch_scene(f"level_scene_{int(event.unicode) - 1}")
