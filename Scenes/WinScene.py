from Scenes import Scene
from Widgets.Buttton import Button
from config import SCREEN_SIZE, MAIN_FONT
import pygame


class WinScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)
        self.gifts = 0
        self.button = Button(self.scene_loader.screen, (SCREEN_SIZE[0] / 2 - 105, SCREEN_SIZE[1] / 2), (100, 100),
                             "На главную")

    def update_event(self, event):
        self.scene_loader.screen.fill((120, 219, 226))
        self.button.draw_button()
        text1 = MAIN_FONT.render('Вы победили!', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 120))
        text1 = MAIN_FONT.render(f'Вы помогли Санте собрать подарки', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 70))

    def on_pygame_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.is_clicked(event.pos):
                self.scene_loader.switch_scene('all_levels_scene')
