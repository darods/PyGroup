import pygame as pg
from configuracion import *
from sprites import *


class Juego:
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode((Ancho, Alto))
        pg.display.set_caption(Titulo)
        self.clock = pg.time.Clock()
        self.corriendo = True

    def nuevo(self):
        # inicia un nuevo juego
        self.all_sprites = pg.sprite.Group()
        self.platafaformas = pg.sprite.Group()
        self.jugador = Jugador()
        self.all_sprites.add(self.jugador)
        p1 = Plataforma(0, Alto - 40, Ancho, 40)
        self.all_sprites.add(p1)
        self.platafaformas.add(p1)
        p2 = Plataforma(Ancho / 2 - 50, Alto * 3 / 4, 100, 20)
        self.all_sprites.add(p2)
        self.platafaformas.add(p2)
        self.run()

    def run(self):
        # loop del juego
        self.jugando = True
        while self.jugando:
            self.clock.tick(FPS)
            self.eventos()
            self.actualizar()
            self.draw()

    def actualizar(self):
        self.all_sprites.update()
        colision = pg.sprite.spritecollide(
            self.jugador, self.platafaformas, False)
        if colision:
            self.jugador.pos.y = colision[0].rect.top
            self.jugador.vel.y = 0
            self.jugador.rect.midbottom = self.jugador.pos  # corrige los micro saltos

    def eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Se sale del juego
                if self.jugando:
                    self.jugando = False
                self.corriendo = False

    def draw(self):
        self.ventana.fill(Blanco)
        self.all_sprites.draw(self.ventana)
        pg.display.flip()

    def pantalla_inicio(self):
        pass

    def pantalla_fin(self):
        pass


juego = Juego()
juego.pantalla_inicio()
while juego.corriendo:
    juego.nuevo()
    juego.pantalla_fin()

pg.quit()
