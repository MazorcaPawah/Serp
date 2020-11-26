import pygame
import random
Grid_w = 52
Grid_h = 52

class Menjar:
    def __init__(self):
        self.pos_x = random.randint(1,14) * Grid_w
        self.pos_y = random.randint(1,14) * Grid_h
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 100, 100), pygame.Rect(self.pos_x+5, self.pos_y+5, 40, 40)) #dibuixem el menjar
        

class Serp:
    def __init__(self):
        self.len = 3
        self.pos_x_list = [7*52, 6*52, 5*52]
        self.pos_y_list = [7*52, 7*52, 7*52]
    

    def move(self, mov_x, mov_y):
        aux_x = [e for e in self.pos_x_list]
        aux_y = [e for e in self.pos_y_list]

        for i in range(1, self.len):
            self.pos_x_list[i] = aux_x[i-1]
            self.pos_y_list[i] = aux_y[i-1]

        self.pos_x_list[0] = self.pos_x_list[0] + mov_x * 52
        self.pos_y_list[0] = self.pos_y_list[0] + mov_y * 52
    

    def draw(self, surface):
        for i in range(self.len-1):
            pygame.draw.rect(surface, (100, 100, 255), pygame.Rect(self.pos_x_list[i]+5, self.pos_y_list[i]+5, 40, 40))
    

    def colisio(self):
        for i in range(1, self.len):
            if self.pos_x_list[i] == self.pos_x_list[0] and self.pos_y_list[i] == self.pos_y_list[0]:
                return True
            else:
                return False