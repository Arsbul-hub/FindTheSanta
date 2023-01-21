from Scenes import Scene
from config import MAIN_FONT, SCREEN_SIZE


class GameOverScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)

    def update_event(self, event):
        self.scene_loader.screen.fill((120, 219, 226))
        text1 = MAIN_FONT.render('Вы проиграли!', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 120))
