import pygame
Grid_w = 52
Grid_h = 52

class Menjar:
    def __init__(self):
        self.pos = None

class Serp:
    def __init__(self):
        self.pos_x = 7 * 52
        self.pos_y = 7 * 52
        self.len = 1
    
    def move(self, mov_x, mov_y):
        self.pos_x = self.pos_x + mov_x * 52
        self.pos_y = self.pos_y + mov_y * 52
    