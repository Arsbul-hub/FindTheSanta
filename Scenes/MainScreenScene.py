from Entities.Person import Main_Screen_Person
from Scenes import Scene
from config import ITEM_SIZE, DISPLAYING_DISTANCE, SCREEN_SIZE, MAIN_FONT, CLOCK, TEXTURES
import pygame


class MainScreenScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)
        self.person = Main_Screen_Person(scene_loader.screen)

    def update_event(self, event):
        self.scene_loader.screen.fill((0, 0, 0))
        text1 = MAIN_FONT.render('Правила игры', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 120))
        text1 = MAIN_FONT.render('ддддддддддддд', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 80))
        text1 = MAIN_FONT.render('ддддддддддддд', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 40))
        text1 = MAIN_FONT.render('ддддддддддддд', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2))
        self.person.update(event, CLOCK.tick())
        self.person.draw((self.person.x, self.person.y))

    def on_pygame_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            self.scene_loader.switch_scene("all_levels_scene")
