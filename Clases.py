import pygame
import random
Grid_w = 52
Grid_h = 52

class Menjar:
    def __init__(self):
        self.pos_x = random.randint(1,14) * Grid_w
        self.pos_y = random.randint(1,14) * Grid_h
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 100, 100), pygame.Rect(self.pos_x+5, self.pos_y+5, 40, 40))

class Serp:
    def __init__(self):
        self.pos_x = 7 * 52
        self.pos_y = 7 * 52
        self.len = 1
    
    def move(self, mov_x, mov_y):
        self.pos_x = self.pos_x + mov_x * 52
        self.pos_y = self.pos_y + mov_y * 52
    
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 255), pygame.Rect(self.pos_x+5, self.pos_y+5, 40, 40))