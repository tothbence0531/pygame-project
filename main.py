import pygame
from player import *
from terrain import *
from config import *
from camera import *

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.terrain = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.running = True
        self.clock = pygame.time.Clock()
        self.create_tilemap()
        self.player = Player(self, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def create_tilemap(self):

        for i, row in enumerate(SAFEHOUSE):
            for j, column in enumerate(row):
                if column == "T":
                    Terrain(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)

    def loop(self):

        while self.running:

            self.clock.tick(60)
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

game = Game()
game.loop()