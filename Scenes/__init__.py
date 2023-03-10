from copy import deepcopy, copy


class Scene:
    def __init__(self, scene_loader):
        self.scene_loader = scene_loader

    def update_event(self, event):
        pass

    def on_pygame_event(self, event):
        pass

    def on_switch(self):
        pass


class SceneLoader:
    def __init__(self, screen):
        self.scenes = {}
        self.current_scene = None
        self.screen = screen

    def add(self, scene, name):
        self.scenes[name] = scene
        if len(self.scenes) == 1:
            self.current_scene = name

    def switch_scene(self, name):
        self.current_scene = name
        self.get_current().on_switch()

    def get_current(self):
        d = self.scenes[self.current_scene]
        return d
