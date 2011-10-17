import pygame
playerFault = False
computerFault = False
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("paddle.png")
        self.rect = self.image.get_rect()
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (20, mousey)
class Computer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("paddle.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 560
        self.rect.centery = 235
        self.dx = 5
        self.dy = 5
    def update(self):
        self.rect.centerx += 0
        self.rect.centery += 0
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.centery = 235
        self.dx = 5
        self.dy = 5
        
    def update(self):
        screen = pygame.display.get_surface()
        self.rect.centerx -= self.dx
        self.rect.centery += self.dy
        if self.rect.left > screen.get_width():
            computerFault = True
            self.reset()
        if self.rect.right < 0:
            if score.lives > 0:
                score.lives -= 1
            else:
                gameOver = True

    def reset(self):
        self.rect.centerx = 300
        self.rect.centery = 235
