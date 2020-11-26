import pygame
import os
import Clases

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

#Definicio Serp
Serp = Clases.Serp()

#Definicio poma
Menjar = Clases.Menjar()

#MAIN LOOP
speed_param = 0
clock = pygame.time.Clock()
running = True
score = 0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direccio_y != 1:
                direccio_x = 0 
                direccio_y = -1
            elif event.key == pygame.K_DOWN and direccio_y != -1:
                direccio_x = 0
                direccio_y = 1
            elif event.key == pygame.K_LEFT and direccio_x != 1:
                direccio_x = -1
                direccio_y = 0
            elif event.key == pygame.K_RIGHT and direccio_x != -1:
                direccio_x = 1
                direccio_y = 0
            
    if speed_param == 8:   
        Serp.move(direccio_x, direccio_y)
        speed_param = 0
        if Serp.pos_x_list[0] in [15*52, 0] or Serp.pos_y_list[0] in [15*52, 0] or Serp.colisio == True:
            Serp = Clases.Serp()
            Menjar = Clases.Menjar()
            score = 0
            direccio_x = 1
            direccio_y = 0

    elif Menjar.pos_x == Serp.pos_x_list[0] and Menjar.pos_y == Serp.pos_y_list[0]:
        Menjar = Clases.Menjar()
        score += 1
        Serp.len += 1
        Serp.pos_x_list.append(0)
        Serp.pos_y_list.append(0)
    
    
    #Coses del final
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
