import pygame, os
from time import sleep
pygame.init() 


hive_paths = {"ant": os.path.join("sounds", "ant.wav"), "hopper": os.path.join("sounds", "hopper.wav"),
              "spider": os.path.join("sounds", "spider.wav"), "bee": os.path.join("sounds", "bee.wav"),
              "bug": os.path.join("sounds", "bug.wav"), "mosquito": os.path.join("sounds", "mosquito.wav"),
              "ladybug": os.path.join("sounds", "ladybug.wav"), "music": os.path.join("sounds", "music.wav")}
pygame.mixer.music.load(hive_paths["bug"])

class sound_maker():
    def __init__(self, music = False, sound = True):
        self.sound = sound
        self.music = music
    
    def make_sound(self, insect_type):
        if self.sound:
            pygame.mixer.music.stop()
            sleep(0.2)
            return pygame.mixer.Sound(hive_paths[insect_type]).play() 
    
    def play_music(self):
        if self.music:
            return pygame.mixer.music.play(-1)