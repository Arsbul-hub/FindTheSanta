import pygame


class StaticImage:
    def __init__(self, path, size, alpha=False):
        self.path = path
        self.size = size
        self.alpha = alpha
        self.surf = pygame.transform.scale(pygame.image.load(path), size)

    def draw(self, screen, position):
        rect = self.surf.get_rect().move(position[0], position[1])
        if not self.alpha:

            screen.blit(self.surf.convert(), rect)
        else:
            screen.blit(self.surf.convert_alpha(), rect)

    def draw_flipped(self, screen, position, flip):
        flipped_surf = pygame.transform.flip(self.surf, flip[0], flip[1])
        rect = flipped_surf.get_rect().move(position[0], position[1])
        if not self.alpha:

            screen.blit(flipped_surf.convert(), rect)
        else:
            screen.blit(flipped_surf, rect)
