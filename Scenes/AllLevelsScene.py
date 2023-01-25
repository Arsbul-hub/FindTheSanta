import pygame
import random
from Scenes import Scene
from Widgets.Buttton import Button
from config import SCREEN_SIZE, MAIN_FONT


# with open("levels.txt", "r") as f:
#     n = len(f.read().split("#level\n")[1:])


class AllLevelsScene(Scene):
    def __init__(self, scene_loader, levels):
        super().__init__(scene_loader)
        self.snows = []
        for i in range(350):
            x = random.randrange(0, 900)
            y = random.randrange(0, 900)
            self.snows.append([x, y])
        self.buttons = []
        for i in range(len(levels)):
            b = Button(self.scene_loader.screen, (50, i * 70 + 200), (160, 60), f"Уровень: {i + 1}")
            b.level = i
            self.buttons.append(b)

    def update_event(self, event):
        self.scene_loader.screen.fill((0, 0, 0))
        draw_snow(self.scene_loader.screen, self.snows)
        for button in self.buttons:
            button.draw_button()

        text1 = MAIN_FONT.render('Для выбора уровня нажмите на соответствующую кнопку', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (100, 100))

    def on_pygame_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_clicked(event.pos):
                    self.scene_loader.switch_scene(f"level_scene_{button.level}")
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
