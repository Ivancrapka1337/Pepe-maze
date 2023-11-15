from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, size_x, size_y, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 60:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 60:
            self.rect.y += self.speed

class Eminem(GameSprite):
    side = "up"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, y1, y2):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)
        self.y1 = y1
        self.y2 = y2
    def update(self):
        if self.rect.y <= self.y1: 
            self.side = "down"
        if self.rect.y >= self.y2:
            self.side = " up"
        if self.side == " up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Pepe maze")
background = transform.scale(image.load("scho.jpg"), (win_width, win_height))

player = Player('pepe s.png', 60, 60, win_width - 80, 20, 4)
monster = Eminem('pepe.png', 50, 60, win_width - 80, 220, 2, 220, 410)
final = GameSprite('dor.png', 60, 60, win_width - 260, win_height - 60, 0)

w1 = Wall(234, 207, 76, 75,425, 25,75)
w2 = Wall(234, 207, 76, 75,425, 75,25)
w3 = Wall(234, 207, 76, 75,300, 525,25)
w4 = Wall(234, 207, 76, 75,0, 25,200)
w5 = Wall(234, 207, 76, 275,325, 25,75)
w6 = Wall(234, 207, 76, 400,425, 25,75)
w7 = Wall(234, 207, 76, 400,400, 200,25)
w8 = Wall(234, 207, 76, 200,200, 525,25)
w9 = Wall(234, 207, 76, 200,100, 25,125)
w10 = Wall(234, 207, 76, 325,0, 25,100)
w11 = Wall(234, 207, 76, 450,150, 25,50)
w12 = Wall(234, 207, 76, 0,0, 700,1)
w13 = Wall(234, 207, 76, -1,0, 1,500)
w14 = Wall(234, 207, 76, 0,501, 700,1)
w15 = Wall(234, 207, 76, 701,0, 1,500)

walls = sprite.Group()
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)
walls.add(w7)
walls.add(w8)
walls.add(w9)
walls.add(w10)
walls.add(w11)
walls.add(w12)
walls.add(w13)
walls.add(w14)
walls.add(w15)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('neon-gaming-128925.mp3')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()
        walls.draw(window)

        if sprite.collide_rect(player, monster) or sprite.spritecollide(player, walls, False):
            finish = True
            window.blit(lose, (230, 240))
            kick.play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (230, 240))
            money.play()

    display.update()
    clock.tick(FPS)

