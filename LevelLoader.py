from pprint import pprint

from config import AIR, WALL, GIFT, SPAWN, SANTA, CODES


class Level:
    level_map = []
    player_spawn = (0, 0)
    santa_spawn = (0, 0)
    gifts = []

    def __getitem__(self, index):
        return self.level_map[index]


class LevelLoader:
    def __init__(self):
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
            out_level.santa_spawn = self.get_santa_cords(out_level_map)
            out_level.player_spawn = self.get_player_cords(out_level_map)
            self.levels.append(out_level)

    def __call__(self, *args, **kwargs):
        return self.levels

    def __iter__(self):
        return self.levels

    @staticmethod
    def get_santa_cords(levels):
        for i in range(len(levels)):
            level = levels[i]
            if CODES["S"] in level:
                return level.index(CODES["S"]), i

    @staticmethod
    def get_player_cords(levels):
        for i in range(len(levels)):
            level = levels[i]

            if CODES["P"] in level:
                return level.index(CODES["P"]), i
