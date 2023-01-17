import sys
from pprint import pprint

from pygame import *

from Scenes.WinScene import WinScene
from Scenes import SceneLoader
from Scenes.LevelScene import LevelsScene
from Scenes.MainScreenScene import MainScreenScene
from Scenes.AllLevelsScene import AllLevelsScene
from config import SCREEN_SIZE
from LevelLoader import LevelLoader
import pygame


pygame.font.init()
if __name__ == "__main__":

    sc = display.set_mode(SCREEN_SIZE, vsync=1)

    scene_loader = SceneLoader(sc)
    levels = LevelLoader(sc)
    ev = None
    for i in range(len(levels.get_levels())):
        level = levels.levels[i]
        scene_loader.add(LevelsScene(scene_loader, level), f"level_scene_{i}")

    scene_loader.add(WinScene(scene_loader), "win_scene")
    scene_loader.add(MainScreenScene(scene_loader), "main_screen_scene")
    scene_loader.add(AllLevelsScene(scene_loader), "all_levels_scene")
    scene_loader.current_scene = "main_screen_scene"
    while True:

        for ev in event.get():  # Обрабатываем события
            if ev.type == QUIT:
                sys.exit(0)
            # self.draw(

            scene_loader.get_current().on_pygame_event(ev)

        scene_loader.get_current().update_event(ev)

        display.update()
