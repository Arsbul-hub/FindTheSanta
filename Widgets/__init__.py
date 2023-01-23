import pygame

pygame.font.init()


class Button():
    def __init__(self, screen, position, size, text):
        self.text = text
        self.x, self.y = position
        self.w, self.h = size
        self.screen = screen

    def draw_button(self):
        font = pygame.font.Font(None, 50)
        text = font.render(self.text, True, (100, 100, 100))
        rect = text.get_rect()
        rect = rect.move(self.x + 10, self.y + 10)

        self.screen.blit(text, rect)
        pygame.draw.rect(self.screen, (100, 100, 100), (self.x, self.y, text.get_width() + 20, text.get_height() + 20), 1)

    def is_clicked(self, pos):
        if self.x < pos[0] < self.x + self.w:
            if self.y < pos[1] < self.y + self.h:
                return True
        return
