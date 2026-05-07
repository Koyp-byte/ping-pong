from pygame import *

window = display.set_mode((700, 500))
display.set_caption('labirint')
background = transform.scale(image.load('images (1).jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, width, height, x, y):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x,  self.rect.y))




class Player_2(GameSprite):
    def __init__(self, sprite_image, width, height, x, y, speed):
        super().__init__(sprite_image, width, height, x, y)
        self.speed = speed
    def update(self):
    
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:   
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:   
            self.rect.y += self.speed

class Player_1(GameSprite):
    def __init__(self, sprite_image, width, height, x, y, speed):
        super().__init__(sprite_image, width, height, x, y)
        self.speed = speed

    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:   
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:   
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, sprite_image, width, height, x, y, speed):
        super().__init__(sprite_image, width, height, x, y)
        self.speed_x = speed
        self.speed_y = speed


    def update(self):
        if self.rect.x < 645 and self.rect.x > 5:
            self.rect.x += self.speed_x
        if self.rect.y > 5 and self.rect.y < 445:
            self.rect.y += self.speed_y
        else:
            self.speed_y *= -1
            self.rect.y += self.speed_y


player1 = Player_1('p2026-02-06-08-10-58-576x394.jpg',20, 150, 50, 400, 5)
ball = Enemy('images.jpg',50, 50, 350, 250, 5)
player2 = Player_2('p2026-02-06-08-10-58-576x394.jpg',20, 150, 650, 400, 5)

game = True

clock = time.Clock()

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    window.blit(background, (0, 0))




    clock.tick(60)
    player1.update()
    player2.update()
    ball.update()
    player1.reset()
    player2.reset()
    ball.reset()
    display.update() 

    if (sprite.collide_rect(player1, ball)) or (sprite.collide_rect(player2, ball)):
        ball.speed_x *= -1









game = True
finish = False





















