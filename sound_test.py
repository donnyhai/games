import pygame, os
pygame.init() 


hive_paths = {"ant": os.path.join("sounds", "ant.wav"), "hopper": os.path.join("sounds", "hopper.wav"),
              "spider": os.path.join("sounds", "spider.wav"), "bee": os.path.join("sounds", "bee.wav"),
              "bug": os.path.join("sounds", "bug.wav"), "mosquito": os.path.join("sounds", "mosquito.wav"),
              "ladybug": os.path.join("sounds", "ladybug.wav")}


class sound_maker():
    def __init__(self, insect_type):
        self.insect_sound = pygame.mixer.Sound(hive_paths[insect_type])
    
    def make_sound(self):
       return self.insect_sound.play()      