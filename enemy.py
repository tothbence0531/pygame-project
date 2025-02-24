import pygame
from config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        super().__init__(game.all_sprites, game.enemies)

        self.x = TILESIZE * x
        self.y = TILESIZE * y
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(PURPLE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y