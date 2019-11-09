import pygame as pg
from configuracion import *


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

    def eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Se sale del juego
                self.jugando = False
                self.corriendo = False

        key = pg.key.get_pressed()

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
