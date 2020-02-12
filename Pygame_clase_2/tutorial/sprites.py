import pygame as pg
from configuracion import *
vector = pg.math.Vector2


class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image


class Jugador(pg.sprite.Sprite):
    def __init__(self, juego):
        pg.sprite.Sprite.__init__(self)
        self.game = juego
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (Ancho / 2, Alto / 2)
        self.pos = vector(Ancho / 2, Alto / 2)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(614, 1063, 120, 191),
                                self.game.spritesheet.get_image(690, 406, 120, 201)]
        for frame in self.standing_frames:
            frame.set_colorkey(Negro)

        self.walk_frames_r = [self.game.spritesheet.get_image(678, 860, 120, 201),
                              self.game.spritesheet.get_image(692, 1458, 120, 207)]
        for frame in self.walk_frames_r:
            frame.set_colorkey(Negro)

        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))
        for frame in self.walk_frames_l:
            frame.set_colorkey(Negro)

        self.jump_frame = self.game.spritesheet.get_image(416, 1660, 150, 181)
        self.jump_frame.set_colorkey(Negro)

    def jump(self):
        # salta solo si está en una plataforma
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platafaformas, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.animate()
        self.acc = vector(0, gravedad)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -acc_jugador

        if keys[pg.K_RIGHT]:
            self.acc.x = acc_jugador

        self.acc.x += self.vel.x * friccion_jugador
        self.vel += self.acc
        if abs(self.vel.x) < 0.5:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc  # equación de la aceleración

        if self.pos.x > Ancho:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Ancho
        self.rect.midbottom = self.pos

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


class Plataforma(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(Verde)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
