import pygame

from Animation import Animation

pygame.font.init()
CLOCK = pygame.time.Clock()
LEVELS_FILE = "levels.txt"
SCREEN_SIZE = 900, 800
DISPLAYING_DISTANCE = 10, 10
ITEM_SIZE = int(SCREEN_SIZE[0] / DISPLAYING_DISTANCE[0]), int(
    SCREEN_SIZE[1] / DISPLAYING_DISTANCE[1])
# ENTITY_HITBOX_SIZE = 52, 60
PLAYER_SPEED = 3
MAIN_FONT = pygame.font.Font(None, 36)
# Block Types
AIR = 0
WALL = 1
SPAWN = 3
SANTA = 4
GIFT = 5
MONSTER = 6
FULL_BLOCKS = [WALL]
CODES = {
            " ": {"texture": "textures/plate.png", "animated": False, "type": AIR},
            "|": {"texture": "textures/block_snowed_all.png", "animated": False, "type": WALL},
            # "S": {"texture": "textures/santa.png", "animated": False, "type": SANTA},
            "s": {"texture": "textures/stone1.png", "animated": False, "type": WALL},
            # "P": {"texture": "textures/plate.png", "animated": False, "type": SPAWN},
            "g": {"animation": Animation("textures/gift.gif"), "animated": True, "type": GIFT},
            "_": {"texture": "textures/block.png", "animated": False, "type": WALL}
        }
