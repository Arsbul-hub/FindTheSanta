from Entities.Monster import Monster
from Entities.Santa import Santa
from Level import get_monsters_cords, get_gifts_count, get_santa_cords, get_player_cords, get_loose_time, Level
from config import CODES, ITEM_SIZE


class LevelLoader:
    def __init__(self, screen):
        self.screen = screen
        self.levels = []

        with open("./levels.txt", "r") as f:
            levels = f.read().split("#level\n")[1:]
        for level in levels:
            out_level_map = []

            for line in level.split("\n")[1:]:

                list_items = []
                for i in line:

                    if CODES.get(i):
                        list_items.append(CODES[i])
                    else:

                        list_items.append(i)

                out_level_map.append(list_items)

            out_level = Level()

            out_level.loose_time = get_loose_time(level)
            out_level.level_map = out_level_map
            out_level.player_spawn = get_player_cords(out_level_map)
            out_level.level_map[out_level.player_spawn[1]][out_level.player_spawn[0]] = CODES[" "]
            out_level.santa_spawn = get_santa_cords(out_level_map)
            out_level.level_map[out_level.santa_spawn[1]][out_level.santa_spawn[0]] = CODES[" "]
            out_level.gifts = get_gifts_count(out_level_map)
            s = Santa(screen, out_level)

            s.set_position(out_level.santa_spawn[0] * ITEM_SIZE[0], out_level.santa_spawn[1] * ITEM_SIZE[1])
            out_level.entities.append(s)
            for mpos in get_monsters_cords(out_level_map):
                m = Monster(screen, out_level)
                m.set_position(mpos[0] * ITEM_SIZE[0], mpos[1] * ITEM_SIZE[1])
                out_level.level_map[mpos[1]][mpos[0]] = CODES[" "]
                out_level.entities.append(m)
            # out_level.entities.append(Player(out_level, self.screen, self.get_player_cords(out_level_map)))
            # out_level.player_spawn = get_player_cords(out_level_map)
            self.levels.append(out_level)

    def get_levels(self):
        return self.levels

    def __call__(self, *args, **kwargs):
        return self.levels

    def __iter__(self):
        return self.levels