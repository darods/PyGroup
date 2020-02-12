import pygame as pg
from configuracion import *
vector = pg.math.Vector2  # sirve para manejar el movimiento en 2D


class Spritesheet:
    def __init__(self, nombre_archivo):
        self.spritesheet = pg.image.load(nombre_archivo).convert()

    def get_image(self, x, y, ancho, alto):
        imagen = pg.Surface((ancho, alto))
        imagen.blit(self.spritesheet, (0, 0), (x, y, ancho, alto))
        # el metodo de re escalar solo funciona con enteros, y el // es div entera
        imagen = pg.transform.scale(imagen, (ancho // 2, alto // 2))
        return imagen


class Jugador(pg.sprite.Sprite):
    def __init__(self, juego):
        pg.sprite.Sprite.__init__(self)
        self.juego = juego  # Hacemos una referencia al juego
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.cargar_imagenes()
        self.image = self.standing_frames[0]

        self.image = pg.Surface((ANCHO_JUGADOR, ALTO_JUGADOR))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO / 2, ALTO / 2)
        self.pos = vector(ANCHO / 2, ALTO / 2)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

    def cargar_imagenes(self):
        self.standing_frames = [self.juego.spritesheet.get_image(614, 1063, 120, 191),
                                self.juego.spritesheet.get_image(690, 406, 120, 201)]
        for frame in self.standing_frames:
            frame.set_colorkey(NEGRO)

        self.walk_frames_r = [self.juego.spritesheet.get_image(678, 860, 120, 201),
                              self.juego.spritesheet.get_image(692, 1458, 120, 207)]
        for frame in self.walk_frames_r:
            frame.set_colorkey(NEGRO)

        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))
        for frame in self.walk_frames_l:
            frame.set_colorkey(NEGRO)

        self.jump_frame = self.juego.spritesheet.get_image(416, 1660, 150, 181)
        self.jump_frame.set_colorkey(NEGRO)

    def animate(self):
        now = pg.time.get_ticks()

        if not self.jumping and not self.walking:
            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom

                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # walk animation
        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (
                    self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

    def jump(self):
        # salta solo si está en una plataforma
        self.rect.y += 1  # corre en 1 pixel a ver si colisiona
        colision = pg.sprite.spritecollide(
            self, self.juego.platafaformas, False)
        self.rect.y -= 1
        if colision:
            self.vel.y = -20

    def update(self):  # importante que se llame update, no valen traducciones
        self.animate()
        self.acc = vector(0, GRAVEDAD)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -ACC_JUGADOR

        if keys[pg.K_RIGHT]:
            self.acc.x = ACC_JUGADOR

        self.acc.x += self.vel.x * FRICCCION
        self.vel += self.acc  # equación de la velocidad
        if abs(self.vel.x) < 0.5:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc  # equación de la posición

        # vuelve a aparecer en el otro lado de la pantalla
        if self.pos.x > ANCHO:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = ANCHO
        self.rect.midbottom = self.pos  # actualizamos su posición


class Plataforma(pg.sprite.Sprite):
    # w y h hacen referencia a ancho y alto (en ingles)
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
