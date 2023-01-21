import pygame

from ImageLoader import Animation, StaticImage

pygame.font.init()
CLOCK = pygame.time.Clock()

LEVELS_FILE = "levels.txt"
SCREEN_SIZE = 900, 800
DISPLAYING_DISTANCE = 7, 7
ITEM_SIZE = int(SCREEN_SIZE[0] / DISPLAYING_DISTANCE[0]), int(
    SCREEN_SIZE[1] / DISPLAYING_DISTANCE[1])
# ENTITY_HITBOX_SIZE = 52, 60
PLAYER_SPEED = 4
MONSTERS_SPEED = 5
MAIN_FONT = pygame.font.Font(None, 36)
# Block Types
AIR = 0
WALL = 1
SPAWN = 3
SANTA = 3.1
INTERACTIVE = 5
MONSTER = 6
FULL_BLOCKS = [WALL]
CODES = {
    " ": {"texture": StaticImage("textures/plate.png", ITEM_SIZE), "type": AIR,
          "second_layer": False},
    "#": {"texture": StaticImage("textures/dirt.png", ITEM_SIZE), "type": AIR,
          "second_layer": False},
    "|": {"texture": StaticImage("textures/block_snowed_all.png", ITEM_SIZE), "type": WALL,
          "second_layer": False},
    "s": {"texture": StaticImage("textures/stone1.png", ITEM_SIZE), "type": WALL,
          "second_layer": False},
    "E": {"texture": StaticImage("textures/tree.png", (ITEM_SIZE[0] + 80, ITEM_SIZE[1] + 200), True),
          "type": WALL, "second_layer": True},
    "C": {"texture": Animation("textures/christmas_tree.gif", (ITEM_SIZE[0] + 80, ITEM_SIZE[1] + 200), 0.1, True),
          "animated": True,
          "type": WALL, "second_layer": True},
    "G": {"texture": Animation("textures/gift.gif", (ITEM_SIZE[0], ITEM_SIZE[1]), 0.1, True), "animated": True,
          "type": INTERACTIVE, "second_layer": True},
    "_": {"texture": StaticImage("textures/block.png", ITEM_SIZE), "type": WALL,
          "second_layer": False}
}

TEXTURES = {

}
ANIMATIONS = {

}
# for d in CODES.values():
#     if d.get("texture"):
#         TEXTURES[d["texture"]] = pygame.transform.scale(pygame.image.load(d["texture"]),
#                                                         (ITEM_SIZE[0], ITEM_SIZE[1]))
# TEXTURES["textures/health.png"] = pygame.transform.scale(pygame.image.load("textures/health.png"),
#                                                          (20, 20))
