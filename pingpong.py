from pygame import *
mixer.init()
font.init()
from random import *
import time as timer
font.init() 

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('PINGPONG')
back = (200, 255, 255)
font1 = font.SysFont('Arial', 35)
lose1 = font1.render('Игрок 1 проиграл', True,(180, 180, 0))
lose2 = font1.render('Игрок 2 проиграл', True,(180, 180, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r (self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_l (self):
        keys1 = key.get_pressed()
        if keys1 [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys1 [K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    
player1 = Player("racket.png", 620, win_height - 300, 60, 150, 15)
player2 = Player("racket.png", 20, win_height - 300, 60, 150, 15)
ball = GameSprite("tenis_ball.png", 290, 60, 30, 30, 50)

speed_x = 10
speed_y =10

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == False:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player1.update_l()
        player2.update_r()
        window.fill(back)
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        if ball.rect.y >= win_height - 20 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1.2
    else:
        finish = False
        speed_x = 10
        ball.rect.x = 290
        ball.rect.y =60
        time.delay(2000)
    display.update()
    time.delay(60)
