from pygame.sprite import Sprite
import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    def __init__(self):
         self.image = SPACESHIP
         self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
         self.rect = self.image.get_rect()
         self.rect.x = self.X_POS
         self.rect.y = self.Y_POS

    def update (self, user_input):
          if user_input[pygame.K_LEFT]:
              self.move_left()
          elif user_input[pygame.K_RIGHT]:
               self.move_right()
          elif user_input[pygame.K_UP]:
               self.move_up()
          elif user_input[pygame.K_DOWN]:
               self.move_down()
    
    def draw(self, screen):
         screen.blit(self.image,(self.rect.x, self.rect.y))
         

    def move_left(self):
        if self.rect.left <= 0:
            self.rect.right = SCREEN_WIDTH
        else:
            self.rect.x -= self.SHIP_SPEED

    def move_right(self):
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.left = 0
        else:
            self.rect.x += self.SHIP_SPEED

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.SHIP_SPEED