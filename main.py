import pygame

pygame.init()
screen = pygame.display.set_mode((600, 560))


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (320, 440)
        self.dx = -5
        self.dy = 5
        playerFault = False
        computerFault = False
        
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
    def reset(self):
        self.rect.center = (320, 440)
        self.dx *= -1
        self.dy *= -1
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
        self.rect.center = (580, 280)
        self.dy = 0
    def update(self):
        self.dy = 0
        if ball.rect.top >= 565:
            self.dy = 3
        if ball.rect.bottom <= 550:
            self.dy = -3
        self.rect.centery += self.dy
            
class Scoreboard(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.playerScore = 0
        self.computerScore = 0
        self.font = pygame.font.SysFont("None", 50)

    def update(self):
        self.text = "%d   %d" % (self.playerScore, self.computerScore)
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (285, 35)
def game():
    pygame.display.set_caption("Pong!")

    background = pygame.image.load("fieldbg.png")
    screen.blit(background, (0, 0))

    right = screen.get_width()
    player = Player()
    computer = Computer()

    scoreboard  = Scoreboard()

    objectSprites = pygame.sprite.Group(computer, player)
    ballSprite = pygame.sprite.Group(ball)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        hitPaddles = pygame.sprite.spritecollide(ball, objectSprites, False)
        if hitPaddles:
            ball.dy *= -1
            ball.dx *= -1
        if ball.rect.top <= 10:
            ball.dy*= -1
        if ball.rect.bottom >= 580:
            ball.dy *= -1
        if ball.rect.right <= 0:
            scoreboard.computerScore += 1
            ball.reset()
        if ball.rect.left >= screen.get_width():
            scoreboard.playerScore += 1
            ball.reset()

        objectSprites.update()
        ballSprite.update()
        scoreSprite.update()

        objectSprites.clear(screen, background)
        ballSprite.clear(screen, background)
        scoreSprite.clear(screen, background)

        ballSprite.draw(screen)
        objectSprites.draw(screen)
        scoreSprite.draw(screen)

        pygame.display.flip()
    pygame.mouse.set_visible(True)
    return scoreboard.playerScore
def instructions(score):
    player = Player()
    ball = Ball()
    computer = Computer()

    background = pygame.image.load("fieldbg.png")
    screen.blit(background, (0, 0))

    allSprites = pygame.sprite.Group(computer, player, ball)
    insFont = pygame.font.SysFont(None, 30)

    instructions = (
        "Mail Pilot. Last Score: %d" % score,
        "Instructions: You are a mail pilot for neighborig Islands,",
        "You need to get the mail to the islands for the day's shift.",
        "But be careful and avoid the clouds. Doing this will cause",
        "the plane to fall apart if hit by lightening too",
        "many times.",
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
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()

if __name__ == "__main__":
    ball = Ball()
    main()
pygame.quit()
