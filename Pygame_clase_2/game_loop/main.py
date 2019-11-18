# Por "norma" llamaremos a este archivo main.py
import pygame as pg  # el 'as' sirve para hacer abreviaciones
from configuracion import *
# el * nos sirve para usar otro archivo sin tener que hacer referencia directa


class Juego:
    def __init__(self):  # Se inicializa todo lo necesario para que corra
        pg.init()
        # Las variables que están en MAYÚSCULAS se colocarán en un archivo adicional llamado configuracion.py
        self.ventana = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption(TITULO)
        self.clock = pg.time.Clock()
        self.corriendo = True

    def nuevo(self):  # inicia un nuevo juego
        # Aquí colocaremos todos los elementos del juego
        self.run()

    def run(self):  # loop del juego
        self.jugando = True
        while self.jugando:
            self.clock.tick(FPS)
            self.eventos()
            self.actualizar()
            self.draw()

    def eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Se sale del juego
                if self.jugando:
                    self.jugando = False
                self.corriendo = False

    def actualizar(self):  # Revisará que ha cambiado y tomará decisiones
        pass

    def draw(self):  # Re dibuja la pantalla
        pass

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
