import pygame
import random
from Scenes import Scene
from config import SCREEN_SIZE, MAIN_FONT


class AllLevelsScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)
        self.snows = []
        for i in range(350):
            x = random.randrange(0, 900)
            y = random.randrange(0, 900)
            self.snows.append([x, y])

        self.button = Button(self.scene_loader.screen, 1)
        self.button_2 = Button(self.scene_loader.screen, 2)
        self.buttons = [self.button, self.button_2]

    def update_event(self, event):
        self.scene_loader.screen.fill((0, 0, 0))
        draw_snow(self.scene_loader.screen, self.snows)
        self.button.draw_button()
        self.button_2.draw_button()
        text1 = MAIN_FONT.render('Для выбора уровня нажмите на соответствующую клваишу', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (100, 100))

    def on_pygame_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_clicked(event.pos):
                    self.scene_loader.switch_scene(f"level_scene_{button.level - 1}")
            # self.button.is_clicked(event.pos)


def draw_snow(screen, snows):
    screen = screen
    screen.fill((0, 0, 0))
    for i in range(len(snows)):
        pygame.draw.circle(screen, (255, 255, 255), snows[i], 2)
        snows[i][1] += 1
        if snows[i][1] > SCREEN_SIZE[1]:
            y = random.randrange(-350, -15)
            snows[i][1] = y
            x = random.randrange(0, SCREEN_SIZE[0])
            snows[i][0] = x


class Button():
    def __init__(self, screen, level_number):
        self.level = level_number
        self.y_coord = 120 + level_number * 65
        self.x_coord = 100
        self.x_2_coord = 0
        self._y_2_coord = 0
        self.screen = screen

    def draw_button(self):
        font = pygame.font.Font(None, 50)
        text = font.render(f"Уровень {self.level}", True, (100, 100, 100))
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
