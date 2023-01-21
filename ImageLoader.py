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
    def __init__(self, path, size, delay=1, alpha=False):
        self.path = path
        self.alpha = alpha
        self.size = size
        self.frames = [pygame.transform.scale(image, self.size) for image in split_animated_gif(path)]

        self.animation_delay = delay
        self.animation_current = 0
        self.last_time = datetime(2012, 3, 5, 23, 8, 15)

        self.current_surf = ""

    def load(self, screen, position):

        rect = self.frames[self.animation_current].get_rect().move(position[0], position[1])

        if not self.alpha:
            screen.blit(self.frames[self.animation_current].convert(), rect)

        else:
            screen.blit(self.frames[self.animation_current], rect)
        if (datetime.now() - self.last_time).total_seconds() >= self.animation_delay:

            if self.animation_current == len(self.frames) - 1:
                self.animation_current = 0
            else:
                self.animation_current += 1
            self.last_time = datetime.now()
        # def draw():
        # Thread(target=draw).start()
        #


class StaticImage:
    def __init__(self, path, size, alpha=False):
        self.path = path
        self.size = size
        self.alpha = alpha
        self.surf = pygame.transform.scale(pygame.image.load(path), size)

    def load(self, screen, position):
        rect = self.surf.get_rect().move(position[0], position[1])
        if not self.alpha:

            screen.blit(self.surf.convert(), rect)
        else:
            screen.blit(self.surf, rect)
