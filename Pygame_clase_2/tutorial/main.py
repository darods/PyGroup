import pygame as pg
from configuracion import *
from sprites import *
from os import path


class Juego:
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode((Ancho, Alto))
        pg.display.set_caption(Titulo)
        self.clock = pg.time.Clock()
        self.corriendo = True
        self.fuente = pg.font.match_font(Fuente)
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'Imagenes/Spritesheets')

        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))

    def nuevo(self):
        # inicia un nuevo juego
        self.puntaje = 0
        self.all_sprites = pg.sprite.Group()
        self.platafaformas = pg.sprite.Group()
        self.jugador = Jugador(self)
        self.all_sprites.add(self.jugador)

        for plat in Lista_plataformas:
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

        # si el jugador llega a el lado der
        if self.jugador.rect.right >= Ancho / 6:
            self.jugador.pos.x -= abs(self.jugador.vel.x)
            for plat in self.platafaformas:
                plat.rect.x -= abs(self.jugador.vel.x)

                if plat.rect.right > Ancho:
                    plat.kill()
                    self.puntaje += 10

        # muere
        if self.jugador.rect.bottom > Alto:
            self.jugando = False

    def eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Se sale del juego
                if self.jugando:
                    self.jugando = False
                self.corriendo = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.jugador.jump()

    def draw(self):
        self.ventana.fill(Blanco)
        self.all_sprites.draw(self.ventana)
        self.dibujar_texto(str(self.puntaje), 22, Verde, Ancho / 2, 15)
        pg.display.flip()

    def pantalla_inicio(self):
        self.ventana.fill(Blanco)
        self.dibujar_texto(Titulo, 48, Negro, Ancho / 2, Alto / 4)
        self.dibujar_texto("muevete con las flechas", 22,
                           Negro, Ancho / 2, Alto / 2)
        self.dibujar_texto("oprime una tecla para empezar",
                           22, Negro, Ancho / 2, Alto * 3 / 4)

        pg.display.flip()
        self.espera_tecla()

    def pantalla_fin(self):
        if not self.corriendo:
            return
        self.ventana.fill(Blanco)
        self.dibujar_texto("Perdistes", 48, Negro, Ancho / 2, Alto / 4)
        self.dibujar_texto("oprime una tecla para  volver a empezar",
                           22, Negro, Ancho / 2, Alto / 2)
        self.dibujar_texto("oprime x para salir",
                           22, Negro, Ancho / 2, Alto * 3 / 4)
        pg.display.flip()
        self.espera_tecla()

    def dibujar_texto(self, texto, tam, color, x, y):
        fuente = pg.font.Font(self.fuente, tam)
        superficie_texto = fuente.render(texto, True, color)
        text_rect = superficie_texto.get_rect()
        text_rect.midtop = (x, y)
        self.ventana.blit(superficie_texto, text_rect)

    def espera_tecla(self):
        esperando = True
        while esperando:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    esperando = False
                    self.corriendo = False
                if event.type == pg.KEYUP:
                    esperando = False


juego = Juego()
juego.pantalla_inicio()
while juego.corriendo:
    juego.nuevo()
    juego.pantalla_fin()

pg.quit()
