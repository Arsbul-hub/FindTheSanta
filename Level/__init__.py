from Entities.Santa import Santa
from Entities.Monster import Monster
from Exceptions import MapException
from config import CODES, ITEM_SIZE
from datetime import timedelta


class Level:
    def __init__(self):
        self.level_map = []
        self.entities = []
        self.santa_spawn = (0, 0)
        self.gifts = 0
        self.player_spawn = (0, 0)
        self.loose_time = timedelta(minutes=0, seconds=0)

    def __getitem__(self, index):
        return self.level_map[index]

    def copy(self):
        new_level = Level()
        new_level.level_map = self.level_map
        new_level.entities = self.entities
        new_level.santa_spawn = self.santa_spawn
        new_level.gifts = self.gifts
        new_level.player_spawn = self.player_spawn
        new_level.player_spawn = self.loose_time
        return new_level


def get_player_cords(level):
    for i in range(len(level)):
        line = level[i]

        if "P" in line:
            return line.index("P"), i
    raise MapException("На карте не задана позиция игрока!")


def get_santa_cords(level):
    for i in range(len(level)):
        line = level[i]
        if "S" in line:
            return line.index("S"), i
    raise MapException("На карте не задана позиция санты!")


def get_monsters_cords(level):
    d = []
    for i in range(len(level)):
        line = level[i]
        for j in range(len(line)):
            block = line[j]
            if "M" == block:
                d.append((j, i))
    return d


def get_loose_time(str_level):
    d = []
    time_line = str_level.split("\n")[0]

    minutes, seconds = time_line.split(":")

    minutes, seconds = int(minutes), int(seconds)

    return timedelta(minutes=minutes, seconds=seconds)


def get_gifts_count(level):
    d = 0
    for i in range(len(level)):
        line = level[i]
        for j in range(len(line)):
            block = line[j]
            if block == CODES["G"]:
                d += 1
    return d



