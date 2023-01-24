import pygame

pygame.font.init()


class Button():
    def __init__(self, screen, position, size, text):

        self.x, self.y = position
        self.w, self.h = size
        self.text_x, self.text_y = self.x + 10, self.y + 10
        self.text = pygame.font.Font(None, 50).render(text, True, (100, 100, 100))
        self.screen = screen

    def draw_button(self):

        rect = self.text.get_rect()
        rect = rect.move(self.text_x, self.text_y)

        self.screen.blit(self.text, rect)
        pygame.draw.rect(self.screen, (100, 100, 100), (
            self.x, self.y, self.text.get_width() + 20, self.text.get_height() + 20), 1)

    def is_clicked(self, pos):
        if self.x < pos[0] < self.x + self.text.get_width() + 20:
            if self.y < pos[1] < self.y + self.text.get_width() + 20:
                return True
        return
