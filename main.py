import pygame
from player import *
from terrain import *
from config import *
from camera import *
from enemy import *

pygame.init()

class Game:
    def __init__(self):
        self.player = None
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_sprites = Camera()
        self.terrain = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.running = True
        self.clock = pygame.time.Clock()
        self.create_tilemap()

    def create_tilemap(self):

        for i, row in enumerate(SAFEHOUSE):
            for j, column in enumerate(row):
                if column == "T":
                    Terrain(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)

    def loop(self):

        while self.running:

            self.clock.tick(60)
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.custom_draw(self.player)
            self.all_sprites.update()

            pygame.display.flip()

        pygame.quit()

game = Game()
game.loop()