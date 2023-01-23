from Scenes import Scene
from config import SCREEN_SIZE, MAIN_FONT
import pygame





class WinScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)
        self.gifts = 0
        self.button = Button(self.scene_loader.screen)

    def update_event(self, event):
        self.scene_loader.screen.fill((120, 219, 226))
        self.button.draw_button()
        text1 = MAIN_FONT.render('Вы победили!', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 120))
        text1 = MAIN_FONT.render(f'Собрано подарков: {self.gifts}', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 100))

    def on_pygame_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.is_clicked(event.pos):
                self.scene_loader.switch_scene('all_levels_scene')


class Button():
    def __init__(self, screen):
        self.y_coord = 300
        self.x_coord = 330
        self.x_2_coord = 0
        self._y_2_coord = 0
        self.screen = screen

    def draw_button(self):
        font = pygame.font.Font(None, 50)
        text = font.render(f"Главное меню", True, (100, 100, 100))
        text_x = self.x_coord
        text_y = self.y_coord
        self.x_2_coord = text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y))
        pygame.draw.rect(self.screen, (100, 100, 100), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
    def is_clicked(self, pos):
        if self.x_coord - 10 < pos[0] and self.x_coord + 180 > pos[0]:
            if self.y_coord < pos[1] and self.y_coord + 60 > pos[1]:
                return True
        return