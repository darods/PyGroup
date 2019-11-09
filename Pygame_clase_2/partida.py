import pygame

from Personajes.Jugador1 import Jugador1

pygame.init()

ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("contra")


jugador = Jugador1()
imagen1 = pygame.image.load("Imagenes/Sprites/LanceUP.png")

run = True

while run:
    pygame.time.delay(30)

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

    ventana.fill((200, 0, 0))
    ventana.blit(imagen1,
                 (jugador.Pos_x, jugador.Pos_y))
    pygame.display.update()

pygame.quit()  # Se cierra pygame
