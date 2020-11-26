import pygame
import random

Grid_w = 52
Grid_h = 52
        

class Serp:
    def __init__(self):
        self.len = 3
        self.pos = [(7*52, 7*52), (6*52, 7*52), (5*52, 7*52)]
        self.direccio = (1, 0)
    

    def move(self):
        aux = [e for e in self.pos]
        cap = self.pos[0]

        for i in range(1, self.len):
            self.pos[i] = aux[i-1]

        cap = (cap[0] + self.direccio[0] * 52, cap[1] + self.direccio[1] * 52)
        self.pos[0] = cap
    

    def draw(self, surface):
        for i in range(self.len-1):
            pos_cub = self.pos[i]
            pygame.draw.rect(surface, (100, 100, 255), pygame.Rect(pos_cub[0]+5, pos_cub[1]+5, 40, 40))

class Menjar:
    def __init__(self, posicio):
        if posicio == "-":
            pos = (random.randint(1,14) * Grid_w, random.randint(1,14) * Grid_h)
            self.pos = pos
        else:
            self.pos = posicio
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 100, 100), pygame.Rect(self.pos[0]+5, self.pos[1]+5, 40, 40)) #dibuixem el menjar