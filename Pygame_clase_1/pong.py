from Bloques import cajita_xd, pelota
import pygame
pygame.init()
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my pirate pong")

# Fuente para el texto de la puntuacion
myfont = pygame.font.SysFont("consolas", 80)


# Declaramos los elementos que vamos a usar en nuestro pong
jugador_1 = cajita_xd(0, 0)
jugador_2 = cajita_xd(450, 0)
pelota = pelota()


run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se sale del juego
            run = False

    key = pygame.key.get_pressed()
    # Definimos los controles del jugador_1
    if key[pygame.K_w] and jugador_1.pos_y > 0:
        jugador_1.mover_arriba()
    if key[pygame.K_s] and jugador_1.pos_y < 400:
        jugador_1.mover_abajo()

    # Definimos los controles del jugador_2
    if key[pygame.K_UP] and jugador_2.pos_y > 0:
        jugador_2.mover_arriba()
    if key[pygame.K_DOWN] and jugador_2.pos_y < 400:
        jugador_2.mover_abajo()

    # llenamos la pantalla con un color para que no se vea el rectangulo regado
    ventana.fill((0, 0, 0))
    # linea que separa la mitad
    pygame.draw.line(ventana, (255, 255, 255), (255, 0), (255, 500), 4)
    # Dibujamos los elementos que hay en nuestro juego
    jugador_1.dibujar(ventana)
    jugador_2.dibujar(ventana)
    pelota.dibujar(ventana)

    # Textos de puntuacion
    puntuacion_1 = myfont.render(str(jugador_1.puntaje), 1, (255, 255, 255))
    puntuacion_2 = myfont.render(str(jugador_2.puntaje), 1, (255, 255, 255))
    ventana.blit(puntuacion_1, (210, 10))
    ventana.blit(puntuacion_2, (270, 10))

    # ponemos a correr la pelota
    pelota.pos_x += pelota.velocidad[0]
    pelota.pos_y += pelota.velocidad[1]

    if(jugador_1.get_rect().colliderect(pelota.get_rect()) or
            jugador_2.get_rect().colliderect(pelota.get_rect())):
        pelota.velocidad[0] = -pelota.velocidad[0]

    if(pelota.pos_y < 0 or pelota.pos_y > 490):
        pelota.velocidad[1] = -pelota.velocidad[1]

    if(pelota.pos_x < 40):
        jugador_2.puntaje += 1
        pelota.reiniciar()

    if(pelota.pos_x > 480):
        jugador_1.puntaje += 1
        pelota.reiniciar()

    pygame.display.update()
pygame.quit()  # Se cierra pygame
