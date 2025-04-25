from pygame import *
mixer.init()
font.init()
mixer.music.load('121.mp3')
font1 = font.Font(None,70)
win = font1.render(')))))))))))))))))',True,(246,15,154))
lose = font1.render('((((((((((((((((',True,(86,15,21))
mixer.music.play(-1)
window =display.set_mode((700,500))
game = True
finish = False
clock =time.Clock()
background =transform.scale(
    image.load('background.jpg'),
    (700,500)
)
class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename),(w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


#клас персонажа
class Player(GameSprite):
    def update(self):
        keys_pressed =key.get_pressed()
        if keys_pressed[K_a] and self.rect.x >5:
            self.rect.x-= 5

        if keys_pressed[K_d] and self.rect.x <595:
            self.rect.x += 5

        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -= 5

        if keys_pressed[K_s] and self.rect.y <395:
            self.rect.y += 5

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 475:
            self.direction = 'right'
        if self.rect.x >= 625:
            self.direction = 'left'


        if self.direction =='left':
            self.rect.x -=5
        else:
            self.rect.x += 5



class Wall(sprite.Sprite):
    def __init__(self,width,height,x,y):
        super().__init__()
        self.image = Surface((width,height))
        self.image.fill((152,47,94))
        self.rect =self.image.get_rect()
        self.rect.y =y
        self.rect.x =x
    def draw_well(self):
        window.blit(self.image,(self.rect.x,self.rect.y))








wall1 = Wall(100,20,150,0)
wall2 = Wall(100,20,250,50)
wall3 = Wall(100,20,350,50)
wall4 = Wall(100,20,450,50)
wall4 = Wall(20,340,150,0)
walls = sprite.Group()
walls.add(wall1,wall2,wall3,wall4)

player =Player('hero.png',65,65,10,20,20)
cyborget =Enemy('cyborg.png',65,65,10,475,250)
treasure1 =GameSprite('treasure.png',65,65,10,600,400)
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')






while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
     
    
    if finish != True:



        window.blit(background,(0,0))
    
        wall2.draw_well()
        wall1.draw_well()
        wall3.draw_well()
        wall4.draw_well()
        cyborget.update()
        player.update()
        player.reset()
        cyborget.reset()
        treasure1.reset()
        if sprite.collide_rect(player,treasure1):
            window.blit(win ,(200,300))
            finish =True
            money.play()
        if sprite.collide_rect(player,cyborget):
            finish =True
            window.blit(lose ,(200,300))
            kick.play()
        if len(sprite.spritecollide(player,walls,False)) >0:
            player.rect.x =20
            player.rect.y =20
    display.update()
    clock.tick(40)


















