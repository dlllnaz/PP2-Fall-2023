import pygame
from settings import *
from spritesheets import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, platform, game):
        self.groups = game.coins
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = platform

        # Load the coin image
        self.spritesheetsobj = SpriteSheet()
        self.image = self.spritesheetsobj.imageLoad(244, 1981, 61, 61)
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (80 // 3, 80 // 3))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.y = self.plat.rect.top - 5
        print("Coin ADDED!")

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()
