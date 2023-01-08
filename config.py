import pygame
pygame.font.init()
CLOCK = pygame.time.Clock()
LEVELS_FILE = "levels.txt"
SCREEN_SIZE = 900, 800
DISPLAYING_DISTANCE = 10, 10
ITEM_SIZE = int(SCREEN_SIZE[0] / DISPLAYING_DISTANCE[0]), int(
    SCREEN_SIZE[1] / DISPLAYING_DISTANCE[1])
ENTITY_HITBOX_SIZE = 52, 70
PLAYER_SPEED = 3
MAIN_FONT = pygame.font.Font(None, 36)
# Block Types
AIR = 0
WALL = 1
SPAWN = 3
SANTA = 4
GIFT = 5
FULL_BLOCKS = [WALL]
CODES = {
            ".": {"base_texture": "textures/plate.png", "animation_len": 4, "animation_duration": 1,
                  "type": AIR},
            "b": {"base_texture": "textures/block_snowed_all.png", "animation_len": 4, "animation_duration": 1,
                  "type": WALL},
            "S": {"base_texture": "textures/santa.png", "animation_len": 4, "animation_duration": 1,
                  "type": SANTA},
            "s": {"base_texture": "textures/stone1.png", "animation_len": 4, "animation_duration": 1,
                  "type": WALL},
            "P": {"base_texture": "textures/plate.png", "animation_len": 4, "animation_duration": 1,
                  "type": SPAWN},
            "g": {"base_texture": "textures/gift.gif", "animation_len": 4, "animation_duration": 1,
                  "type": GIFT},
            "w": {"base_texture": "textures/block.png", "animation_len": 4, "animation_duration": 1,
                  "type": WALL}
        }
