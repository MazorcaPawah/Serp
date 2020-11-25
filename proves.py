import pygame
import os
import Clases
import sys

#Defineix el directori base
base_dir = os.path.abspath(os.path.dirname(__file__))

#Inicialitza el joc
pygame.init()

#Crea una pantalla i el pla de joc
amplada = 827
altura = 947
screen = pygame.display.set_mode((amplada, altura))
pla = pygame.Surface((780, 780), pygame.SRCALPHA)

#Defineix el títol, l'icono de la ventana, l'imatge del fondo de pantalla, i dibuixa el pla
pygame.display.set_caption("Snake goes brrrrrr")
icono_nom = os.path.join(base_dir, "imatges", "Icono.png")
icono = pygame.image.load(icono_nom)
pygame.display.set_icon(icono)
fondo = pygame.image.load(os.path.join(base_dir, "imatges", "Fondo_v2.png"))
screen.blit(fondo, (0, 0))

#Dibuixa la graella ()
Grid_w = 52
Grid_h = 52

#Definicio serp
serp = Clases.Serp()

#MAIN LOOP
speed_param = 0
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if speed_param == 15:
        serp.move(1, 0)
        speed_param =0
    
    #Coses del final
    screen.blit(pla, (24, 144))
    pla.blit(pygame.image.load(os.path.join(base_dir, "imatges", "tablero.png")),(0, 0))
    serp_draw = pygame.draw.rect(pla, (100, 100, 255), pygame.Rect(serp.pos_x+5, serp.pos_y+5, 40, 40))
    speed_param += 1
    pygame.display.update()