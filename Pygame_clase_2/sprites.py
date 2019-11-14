import pygame as pg
from configuracion import *
vector = pg.math.Vector2


class Jugador(pg.sprite.Sprite):
    def __init__(self, juego):
        pg.sprite.Sprite.__init__(self)
        self.game = juego
        self.image = pg.Surface((30, 40))
        self.image.fill(Rojo)
        self.rect = self.image.get_rect()
        self.rect.center = (Ancho / 2, Alto / 2)
        self.pos = vector(Ancho / 2, Alto / 2)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

    def jump(self):
        # salta solo si está en una plataforma
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platafaformas, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vector(0, gravedad)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -acc_jugador

        if keys[pg.K_RIGHT]:
            self.acc.x = acc_jugador

        self.acc.x += self.vel.x * friccion_jugador
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # equación de la aceleración

        if self.pos.x > Ancho:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Ancho
        self.rect.midbottom = self.pos


class Plataforma(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(Verde)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
