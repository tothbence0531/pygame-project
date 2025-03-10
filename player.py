import math

import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        super().__init__(game.all_sprites)

        self.x = TILESIZE * x
        self.y = TILESIZE * y
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.speed = 15
        self.move_y, self.move_x = 0, 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_y -= 1
        if keys[pygame.K_s]:
            self.move_y += 1
        if keys[pygame.K_a]:
            self.move_x -= 1
        if keys[pygame.K_d]:
            self.move_x += 1

        # Normalizing the movement placement
            
        if self.move_x != 0 and self.move_y != 0:
            magnitude = math.sqrt(self.move_x ** 2 + self.move_y ** 2)
            self.move_x /= magnitude
            self.move_y /= magnitude

    def update(self):
        self.move()
        # Updating the player's position
        if 0 < self.rect.x + self.move_x * self.speed:
            self.rect.x += self.move_x * self.speed

            self.collide_with_objects('x')
            self.collide_with_enemies('x')

        if 0 < self.rect.y + self.move_y * self.speed:
            self.rect.y += self.move_y * self.speed

            self.collide_with_objects('y')
            self.collide_with_enemies('y')

        self.move_x, self.move_y = 0, 0

    def collide_with_objects(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.terrain, False)
        if hits:
            if direction == 'x':
                if self.move_x > 0: self.rect.x = hits[0].rect.left - self.rect.width
                elif self.move_x < 0: self.rect.x = hits[0].rect.right

            elif direction == 'y':
                if self.move_y > 0: self.rect.y = hits[0].rect.top - self.rect.height
                elif self.move_y < 0: self.rect.y = hits[0].rect.bottom

    def collide_with_enemies(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            print(hits)
            #self.game.screen.fill(BLACK)
            self.game.stateManager.set_state("fight")