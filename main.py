import sys
from pprint import pprint

from pygame import *
from SceneLoader import SceneLoader
from Scenes import *
from config import SCREEN_SIZE
from LevelLoader import LevelLoader

pygame.font.init()
if __name__ == "__main__":

    sc = display.set_mode(SCREEN_SIZE)

    scene_loader = SceneLoader(sc)
    levels = LevelLoader(sc)
    ev = None
    for i in range(len(levels.levels)):
        level = levels.levels[i]
        scene_loader.add(LevelsScene(scene_loader, level), f"levels_scene_{i}")
    scene_loader.add(WinScene(scene_loader), "win_scene")
    while True:

        for ev in event.get():  # Обрабатываем события
            if ev.type == QUIT:
                sys.exit(0)
            # self.draw(

            scene_loader.get_current().on_pygame_event(ev)

        scene_loader.get_current().update_event(ev)

        display.update()
