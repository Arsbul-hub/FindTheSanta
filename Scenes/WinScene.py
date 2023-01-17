from Scenes import Scene
from config import SCREEN_SIZE, MAIN_FONT





class WinScene(Scene):
    def __init__(self, scene_loader):
        super().__init__(scene_loader)
        self.gifts = 0

    def update_event(self, event):
        self.scene_loader.screen.fill((120, 219, 226))
        text1 = MAIN_FONT.render('Вы победили!', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 120))
        text1 = MAIN_FONT.render(f'Собрано подарков: {self.gifts}', True, (100, 100, 100))
        self.scene_loader.screen.blit(text1, (SCREEN_SIZE[0] // 2 - text1.get_size()[0] / 2,
                                              SCREEN_SIZE[1] // 2 - text1.get_size()[1] / 2 - 100))
