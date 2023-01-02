import sys

import keyboard
from pygame import *
import time


class App():
    def __init__(self):

        self.l = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        #
        self.screen_size = 700, 700
        self.sc = display.set_mode(self.screen_size)
        self.displayed_items = (15, 15)
        self.item_size = int(self.screen_size[0] / self.displayed_items[0]), int(
            self.screen_size[1] / self.displayed_items[1])
        self.y = 15 * self.item_size[0]
        self.x = 15 * self.item_size[1]
        self.hitbox_size = (25, 25)
        self.colliders = []
        self.s = self.item_size[0]
        while True:
            self.update()

    def update(self):

        self.sc.fill((0, 0, 0))
        for e in event.get():  # Обрабатываем события
            if e.type == QUIT:
                sys.exit(0)

        # for i in range(int(self.y // self.item_size[1] - self.displayed_items[0] // 2) - 1,
        #                int(self.y // self.item_size[1] + self.displayed_items[0] // 2) + 2):
        #     for j in range(int(self.x // self.item_size[0] - self.displayed_items[0] // 2) + 2,
        #                    int(self.x // self.item_size[0] + self.displayed_items[0] // 2) + 2):
        for i in range(30):
            for j in range(30):
                try:

                    if i >= 0 and j >= 0 and self.l[i][j] == 1:
                        draw.rect(self.sc, (255, 255, 255), (
                            j * self.item_size[0] - self.x + (self.displayed_items[0] / 2) * self.item_size[0],
                            i * self.item_size[1] - self.y + (self.displayed_items[1] / 2) * self.item_size[1],
                            self.item_size[0], self.item_size[1]))
                except:
                    pass
        # print(int(self.x/50)+6*50)

        try:

            draw.rect(self.sc, (0, 255, 0), (self.displayed_items[0] / 2 * self.item_size[0],
                                             self.displayed_items[1] / 2 * self.item_size[1] ,
                                             self.hitbox_size[0], self.hitbox_size[1]))
            # draw.rect(self.sc, (0, 255, 0), (int(self.y/50)*50+7*50, int(self.x/50)*50+7*50 , 50, 50))
            # print(self.l[int(self.y // self.item_size[1])][int(self.x // self.item_size[0])])
            # self.l[int((self.y) / 50) + 6][int(self.x / 50) + 6] = 9

            # for i in self.l:
            #    print(i,"\n")aaaaaaaaa
        except:
            print("error")
        # print(int((self.y)/50)+7,int((self.x)/50)+7)

        if keyboard.is_pressed("s") and self.l[int((self.y + self.hitbox_size[1] + 2) / self.item_size[1])][int((self.x) / self.item_size[0])] == 0 and self.l[int((self.y + self.hitbox_size[1] + 2) / self.item_size[1])][int((self.x + self.hitbox_size[0]) / self.item_size[0])] == 0:
            self.y += 0.5
        if keyboard.is_pressed("w") and self.l[int((self.y - 1) / self.item_size[1])][int((self.x) / self.item_size[0])] == 0 and self.l[int((self.y - 1) / self.item_size[1])][int((self.x + self.hitbox_size[0]) / self.item_size[0])] == 0:
            self.y -= 0.5
        if keyboard.is_pressed("d") and self.l[int((self.y) / self.item_size[1])][int((self.x + self.hitbox_size[0] + 2) / self.item_size[0])] == 0 and self.l[int((self.y + self.hitbox_size[1]) / self.item_size[1])][int((self.x + self.hitbox_size[0] + 2) / self.item_size[0])] == 0:
            self.x += 0.5
        if keyboard.is_pressed("a") and self.l[int((self.y) / self.item_size[1])][int((self.x - 1) / self.item_size[0])] == 0 and self.l[int((self.y + self.hitbox_size[1]) / self.item_size[1])][int((self.x - 1) / self.item_size[0])] == 0:
            self.x -= 0.5
        display.update()


App()
