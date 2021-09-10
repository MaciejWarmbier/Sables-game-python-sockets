import pygame
import time

left_b=[pygame.image.load('data/left-upper-blue-short.png'),pygame.image.load('data/left-middle-blue-short.png'),pygame.image.load('data/left-bottom-blue-short.png'),
        pygame.image.load('data/left-upper-blue-long.png'),pygame.image.load('data/left-middle-blue-long.png'),pygame.image.load('data/left-bottom-blue-long.png')]

right_r=[pygame.image.load('data/right-upper-red-short.png'),pygame.image.load('data/right-middle-red-short.png'),pygame.image.load('data/right-bottom-red-short.png'),
        pygame.image.load('data/right-upper-red-long.png'),pygame.image.load('data/right-middle-red-long.png'),pygame.image.load('data/right-bottom-red-long.png')]





class player(object):

    def __init__(self,x,y,width,height,position,player_number):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.hitbox = (self.x , self.y, 29, 52)
        self.sword = self.x
        self.position = position
        self.change_cooldown=0
        self.attack_cooldown=0
        self.new_attack = 0
        self.alive = True
        self.death_time = 0
        self.player_number = player_number
        self.background = -900
        self.score = 0
        self.color = (0,0,255)
        self.respawn = False
        self.winning= False
        self.kill_time=0
        self.time=time.time()
        self.time_kill=0
        self.kill_f=0


    def draw(self,window):
        if self.player_number ==0:
            self.color = (0,0,255)
        else:
            self.color=(255,0,0)

        if self.player_number == 1:
            self.hitbox = (self.x + 97, self.y + 80, 1, 70)
            if self.attack_cooldown == 0:

                    self.sword = self.x + 37
                    self.hitbox = (self.x+97, self.y+80, 1, 70)
                    if self.position == 0:
                        window.blit(right_r[0], (self.x, self.y))
                    elif self.position == 1:
                        window.blit(right_r[1], (self.x, self.y))
                    else:
                        window.blit(right_r[2], (self.x, self.y))


            else:

                self.sword = self.x + 17
                if self.position == 0:
                    window.blit(right_r[3], (self.x, self.y))
                elif self.position == 1:
                    window.blit(right_r[4], (self.x, self.y))
                else:
                    window.blit(right_r[5], (self.x, self.y))

        else:
            self.hitbox = (self.x + 81, self.y + 80, 1, 70)
            if self.attack_cooldown == 0:

                    self.sword = self.x + 143
                    self.hitbox = (self.x + 81, self.y +80, 1, 70)
                    if self.position == 0:
                        window.blit(left_b[0], (self.x, self.y))
                    elif self.position == 1:
                        window.blit(left_b[1], (self.x, self.y))
                    else:
                        window.blit(left_b[2], (self.x, self.y))


            else:
                self.sword = self.x + 163

                if self.position == 0:
                    window.blit(left_b[3], (self.x, self.y))
                elif self.position == 1:
                    window.blit(left_b[4], (self.x, self.y))
                else:
                    window.blit(left_b[5], (self.x, self.y))

        #pygame.draw.rect(window, (0, 0, 255), (self.sword,self.y, 1, 100), 1)
        #pygame.draw.rect(window, (255,255,255), self.hitbox,1)

    def killed(self,window):
        self.kill_f = 0
        self.kill_time = 0
        self.alive = False
        self.x=self.start_x
        self.y=self.start_y
        self.attack_cooldown = 0
        self.change_cooldown = 0
        if self.player_number==1:
            self.sword = self.x + 37
            self.hitbox = (self.x + 97, self.y + 80, 1, 70)
        else:
            self.sword = self.x + 143
            self.hitbox = (self.x + 81, self.y + 80, 1, 70)
        self.death_time = 300
        font1 = pygame.font.SysFont('comissans',70)
        text=font1.render('You just DIED!',1,self.color)
        window.blit(text, (700 / 2 - (text.get_width() / 2), 20))
        pygame.display.update()
        i=0
        while i <300:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()
                    exit()

    def hit(self,window):
        self.kill_f=0
        self.kill_time=0
        self.score+=1
        self.x = self.start_x
        self.y = self.start_y
        if self.player_number==1:
            self.sword = self.x + 37
            self.hitbox = (self.x + 97, self.y + 80, 1, 70)
        else:
            self.sword = self.x + 143
            self.hitbox = (self.x + 81, self.y + 80, 1, 70)

        self.attack_cooldown = 0
        self.change_cooldown=0

        font1 = pygame.font.SysFont('comissans', 70)
        text = font1.render('You just KILL!', 1, self.color)
        window.blit(text, (700 / 2 - (text.get_width() / 2), 20))
        pygame.display.update()
        i=0
        while i <300:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()
                    exit()

    def respawn_dead(self,window):
        #self.alive = True
        self.respawn = False
        font1 = pygame.font.SysFont('comissans', 60)
        text = font1.render('Fight once again!', 1, self.color)
        window.blit(text, (700 / 2 - (text.get_width() / 2), 20))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
                    exit()

    def respawn_kill(self,window):
        font1 = pygame.font.SysFont('comissans', 60)
        text = font1.render('Enemy approaches!', 1, self.color)
        window.blit(text, (700 / 2 - (text.get_width() / 2), 20))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
                    exit()

    def attack(self,window):
        self.attack_cooldown = 60
        self.new_attack = 90
        #window.blit(sableRight[3], (self.x, self.y))

    def win(self,window):
        self.winning = False
        self.background = -900
        self.score += 10
        self.x = self.start_x
        self.y = self.start_y
        if self.player_number == 1:
            self.sword = self.x + 37
            self.hitbox = (self.x + 97, self.y + 80, 1, 70)
        else:
            self.sword = self.x + 143
            self.hitbox = (self.x + 81, self.y + 80, 1, 70)

        self.attack_cooldown = 0
        self.change_cooldown = 0

        font1 = pygame.font.SysFont('comissans', 70)
        text = font1.render('You just WON(+10)!', 1, self.color)
        window.blit(text, (700 / 2 - (text.get_width() / 2), 20))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
                    exit()

    def loss(self,window):
        self.respawn =False
        self.alive = True
        self.background = -900
        self.x = self.start_x
        self.y = self.start_y
        self.death_time = 0
        self.attack_cooldown = 0
        self.change_cooldown = 0
        if self.player_number == 1:
            self.sword = self.x + 37
            self.hitbox = (self.x + 97, self.y + 80, 1, 70)
        else:
            self.sword = self.x + 143
            self.hitbox = (self.x + 81, self.y + 80, 1, 70)
        self.death_time = 300
        font1 = pygame.font.SysFont('comissans', 70)
        text = font1.render('You just LOSS!', 1, self.color)
        window.blit(text, (700 / 2 - (text.get_width() / 2), 20))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
                    exit()

    def move(self,window):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 15:
            self.x -= self.vel


        if keys[pygame.K_RIGHT] and self.x < 500:
            self.x += self.vel


        if keys[pygame.K_UP] and self.change_cooldown == 0:
            if self.position > 0:
                self.position -= 1
                self.change_cooldown = 30

        if keys[pygame.K_DOWN] and self.change_cooldown == 0:
            if self.position < 2:
                self.position += 1
                self.change_cooldown = 30

        if keys[pygame.K_SPACE] and self.new_attack == 0:
            self.attack(window)