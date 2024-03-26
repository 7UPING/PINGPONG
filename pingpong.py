from pygame import *
mixer.init()
font.init()
from random import *
import time as timer

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('PINGPONG')
back = (200, 255, 255)

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

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == False:
        player1.update_l()
        player2.update_r()
        window.fill(back)
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
    
    display.update()
    time.delay(60)
