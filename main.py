import pygame

pygame.init()
screen = pygame.display.set_mode((600, 560))

def checkKeys():
    for event in pygame.event.get:
        if event == pygame.KEYDOWN:
            if pygame.key == key.Q:
                keepGoing = False

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 35)
    def update(self):
        self.text = "Lives left %d, Score %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 440
        self.dx = 5
        self.dy = 5
        playerFault = False
        computerFault = False
        
    def update(self):
        if self.rect.top == 10:
            self.dy *= -1
        elif self.rect.bottom == 545:
            self.dy *= -1
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
    def reset(self):
        print("hi")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("paddle.png")
        self.rect = self.image.get_rect()
        self.center = (20, 280)
    def update(self):
        print("hi")
class Computer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("paddle.png")
        self.rect = self.image.get_rect()
        self.center = (580, 280)
    def update(self):
        print("hi")
def game():
    print("hi")
def menu(score):
    computer = Computer()
    player = Player()
    allSprites = pygame.sprite.Group(computer, player)
    insFont = pygame.font.SysFont(None, 30)

    instructions = (
        "Pong. Last Score: %d" % score,
        "Instructions: Play the classic arcade game pong,",
        "As you play try and score as high as you can.",
        "But be careful and avoid letting it slip past your side",
        "too many times.",
        "",
        "Good luck!",
        "",
        "click to start, escape to quit..."
        )

    insLabels = []
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 255))
        insLabels.append(tempLabel)
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
                elif event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = False
        allSprites.draw(screen)
        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))
        pygame.display.flip()
    pygame.mouse.set_visible(True)
    return donePlaying
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = menu(score)
        if not donePlaying:
            score = game()

if __name__ == "__main__":
    main()
pygame.quit()
