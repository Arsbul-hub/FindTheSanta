from Entities.Person import Main_Screen_Person
from ImageLoader import StaticImage
from Scenes import Scene
from config import ITEM_SIZE, DISPLAYING_DISTANCE, SCREEN_SIZE, MAIN_FONT, CLOCK, TEXTURES
import pygame, random


class MainScreenScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)
        self.person = Main_Screen_Person(scene_loader.screen)
        self.snows = []
        for i in range(350):
            x = random.randrange(0, 900)
            y = random.randrange(0, 900)
            self.snows.append([x, y])
        self.logo = StaticImage("textures/logo.png", (200, 200), True)
        self.start_text_opacity = 100
        self.hiding_start_text = True
        self.hiding_speed = 20

    def update_event(self, event):
        tick = CLOCK.tick()
        self.scene_loader.screen.fill((0, 0, 0))
        draw_snow(self.scene_loader.screen, self.snows)
        self.logo.draw(self.scene_loader.screen, (SCREEN_SIZE[0] / 2 - self.logo.size[0] / 2, 50))
        text1 = MAIN_FONT.render('Правила игры', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 100))

        text1 = MAIN_FONT.render('Соберите подарки и принесите их Деду Морозу!', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 60))
        text1 = MAIN_FONT.render('Остерегайся монстров, используй левый shift для того, чтобы убежать.', True,
                                 (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 20))
        text1 = MAIN_FONT.render('Для управления используйте клавиши W, S, A или D', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 + 20))
        text1 = MAIN_FONT.render('Старайся пройти лабиринт как можно скорее!', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 + 60))

        text1 = MAIN_FONT.render('Для старта нажмите любую клавишу', True, (self.start_text_opacity, self.start_text_opacity, self.start_text_opacity))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 + 150))
        self.person.on_update(event, tick)
        self.person.draw((self.person.x, self.person.y))

        self.start_text_opacity += self.hiding_speed * tick / 1000
        if self.start_text_opacity >= 100:
            self.hiding_speed = -100
        elif self.start_text_opacity <= 0:

            self.hiding_speed = 100

    def on_pygame_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            self.scene_loader.switch_scene("all_levels_scene")


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
