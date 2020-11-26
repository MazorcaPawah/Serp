import pygame
import os
import Clases
import random

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

#Dibuixa la graella
Grid = 52

#Definicio Serp
Serp = Clases.Serp()

#Definicio menjar
Menjar = Clases.Menjar("-")

#MAIN LOOP
speed_param = 0
clock = pygame.time.Clock()
running = True
score = 0
while running:
    #Eventos
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and Serp.direccio[1] != 1:
                Serp.direccio = (0, -1)
            elif event.key == pygame.K_DOWN and Serp.direccio[1] != -1:
                Serp.direccio = (0, 1)
            elif event.key == pygame.K_LEFT and Serp.direccio[0] != 1:
                Serp.direccio = (-1, 0)
            elif event.key == pygame.K_RIGHT and Serp.direccio[0] != -1:
                Serp.direccio = (1, 0)
    
    #Moviment        
    if speed_param == 5:   
        Serp.move()
        speed_param = 0
        cap = Serp.pos[0]

        #Mort
        aux = [e for e in Serp.pos]
        aux[0] = 0
        if cap[0] > 14*Grid or cap[0] < 0*Grid or cap[1] > 14*Grid or cap[1] < 0*Grid or cap in aux:
            Serp = Clases.Serp()
            Menjar = Clases.Menjar("-")
            score = 0

        #Colisio amb el menjar
        elif Menjar.pos in Serp.pos:
            pos_menjar_new = (random.randint(1,14)*Grid, random.randint(0,14)*Grid) #Verifica que la posició no estigui dins la serp
            while pos_menjar_new in Serp.pos:
                pos_menjar_new = (random.randint(0,14)*Grid, random.randint(0,14)*Grid)

            Menjar = Clases.Menjar(pos_menjar_new)
            score += 1
            Serp.len += 1
            Serp.pos.append(0)
    
    #Actualització pantalla
    scoreText = pygame.font.SysFont('freesansbold.ttf', 50)
    scoreF = scoreText.render(str(score), True, (255, 255, 255))
    screen.blit(fondo, (0, 0))
    screen.blit(scoreF, (85, 50))
    screen.blit(pla, (24, 144))
    pla.blit(pygame.image.load(os.path.join(base_dir, "imatges", "tablero.png")),(0, 0))
    Serp.draw(pla)
    Menjar.draw(pla)
    speed_param += 1
    pygame.display.update()
