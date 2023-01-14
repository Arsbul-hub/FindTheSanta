from datetime import datetime
from threading import Thread

import pygame
from PIL import Image


def split_animated_gif(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
        )
        ret.append(pygame_image)
    return ret


class Animation:
    def __init__(self, path):
        self.frames = split_animated_gif(path)

        self.animation_delay = 0.1
        self.animation_current = 0
        self.last_time = datetime(2012, 3, 5, 23, 8, 15)

        self.current_surf = ""

    def load(self, screen, size, position):
        t = pygame.transform.scale(self.frames[self.animation_current], size)
        rect = t.get_rect().move(position[0], position[1])
        screen.blit(t, rect)

        if (datetime.now() - self.last_time).total_seconds() >= 0.1:

            if self.animation_current == len(self.frames) - 1:
                self.animation_current = 0
            else:
                self.animation_current += 1
            self.last_time = datetime.now()
        # def draw():
        # Thread(target=draw).start()
        #
