import pygame

from Personajes.Jugador1 import Jugador1

pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("contra")


jugador = Jugador1(None)


run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se sale del juego
            run = False
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        print(jugador.getTeclasMovimiento(0))
        print('\n')

    if (jugador.getTeclasMovimiento(3)):
        print(jugador.getTeclasMovimiento(0))
        print('\n')
