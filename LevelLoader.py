from pprint import pprint

from Entities.Entity import Player
from config import AIR, WALL, GIFT, SPAWN, SANTA, CODES


class Level:
    level_map = []
    entities = []
    santa_spawn = (0, 0)
    gifts = []
    player_spawn = (0, 0)

    def __getitem__(self, index):
        return self.level_map[index]


def get_player_cords(level):
    for i in range(len(level)):
        line = level[i]

        if CODES["P"] in line:
            return line.index(CODES["P"]), i


def get_santa_cords(level):
    for i in range(len(level)):
        line = level[i]
        if CODES["S"] in line:
            return line.index(CODES["S"]), i


class LevelLoader:
    def __init__(self, screen):
        self.screen = screen
        self.levels = []

        with open("levels.txt", "r") as f:
            levels = f.read().split("#level\n")[1:]
        for level in levels:
            out_level_map = []
            for line in level.split("\n"):

                list_items = []
                for i in line:

                    if CODES.get(i):
                        list_items.append(CODES[i])
                    else:
                        print(i)
                        list_items.append(i)

                out_level_map.append(list_items)

            out_level = Level()
            out_level.level_map = out_level_map
            out_level.player_spawn = get_player_cords(out_level_map)
            # out_level.entities.append(Player(out_level, self.screen, self.get_player_cords(out_level_map)))
            out_level.player_spawn = get_player_cords(out_level_map)
            self.levels.append(out_level)

    def __call__(self, *args, **kwargs):
        return self.levels

    def __iter__(self):
        return self.levels
