import sys

from pygame import *
from SceneLoader import SceneLoader
from Scenes import *

if __name__ == "__main__":
    screen_size = 900, 800
    sc = display.set_mode(screen_size)
    clock = pygame.time.Clock()
    scene_loader = SceneLoader(sc)
    scene_loader.add(LevelsScene(scene_loader, screen_size), "levels_scene")

    while True:
        sc.fill((0, 0, 0))

        for e in event.get():  # Обрабатываем события
            if e.type == QUIT:
                sys.exit(0)
            # self.draw()
            scene_loader.get_current().on_pygame_event(event)
        scene_loader.get_current().update_event(event)

        display.update()
