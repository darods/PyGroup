import pygame as pg
from configuracion import *
from sprites import *


class Juego:
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption(TITULO)
        self.clock = pg.time.Clock()
        self.corriendo = True

    def nuevo(self):
        # inicia un nuevo juego
        self.puntaje = 0
        self.all_sprites = pg.sprite.Group()
        self.platafaformas = pg.sprite.Group()
        self.jugador = Jugador(self)
        self.all_sprites.add(self.jugador)

        # añadimos cada una de las plataformas
        for plat in LISTA_PLATAFORMAS:
            p = Plataforma(*plat)  # el * sirve para descomponer cada elemento
            self.all_sprites.add(p)
            self.platafaformas.add(p)

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
        if self.jugador.vel.y > 0:
            colision = pg.sprite.spritecollide(
                self.jugador, self.platafaformas, False)
            if colision:
                if self.jugador.pos.y < colision[0].rect.bottom:
                    self.jugador.pos.y = colision[0].rect.top
                    self.jugador.vel.y = 0
                    self.jugador.rect.midbottom = self.jugador.pos  # corrige los micro saltos

    def eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Se sale del juego
                if self.jugando:
                    self.jugando = False
                self.corriendo = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.jugador.jump()

    def draw(self):
        self.ventana.fill(BLANCO)
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
