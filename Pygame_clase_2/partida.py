import pygame
from configuracion import *
from Personajes.Jugador1 import Jugador1

pygame.init()

ventana = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption(Titulo)
clock = pygame.time.Clock()

jugador = Jugador1()
caminando_der = [pygame.image.load("Imagenes/Sprites/dogge_der_1.png"),
                 pygame.image.load("Imagenes/Sprites/dogge_der_2.png")]

derecha = False
walkCount = 0

run = True


def redibujarVentana():
    global walkCount
    ventana.fill(Blanco)
    # ventana.blit(imagen1,(jugador.Pos_x, jugador.Pos_y))
    pygame.display.update()


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se sale del juego
            run = False
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        print("hola")

    if key[pygame.K_a]:
        jugador.mover_izq()

    if key[pygame.K_d]:
        jugador.mover_der()

    redibujarVentana()

pygame.quit()  # Se cierra pygame
