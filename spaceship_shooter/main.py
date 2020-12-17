import pygame
import random
import math
from pygame import mixer

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('spaceback.png')

# Title and Icon
pygame.display.set_caption("Spaceship Shooter")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

# Insert music
pygame.mixer.init()
playerMusic = pygame.mixer.music.load('gamemusic.mp3')
pygame.mixer.music.play(-1)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370  # initial positions
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(4)
    enemyY_change.append(20)

# Bullet
# Ready state means you cant't see the bullet on the screen
# Fire means bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return True if distance < 27 else False


# Game loop
running = True
while running:
    # RGB
    # screen.fill((255, 178, 102))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is pressed, check whether right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
                # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
                # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                # print("Keystroke has been released")

    # boundary conditions
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Enemy movement
    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)  # initial positions
            enemyY[i] = random.randint(50, 200)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()  # since its a game with lot of
    # animations and stuff, so it
    # needs updating every time