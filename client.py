import pygame
from network import Network
from Player import player
import time
import math
import nntplib

Width = 700
Height = 300
background_x = -900
pygame.init() # now use display and fonts
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Szable")
bg = pygame.image.load('data/background.jpg')


def redrawWindow(window, player1, player2):
    font = pygame.font.SysFont('comicsans', 30, True, True)
    window.blit(bg, (player1.background, 0))
    if player1.player_number==0:
        score1 = font.render('Score: ' + str(player1.score), 1, (0, 0, 255))
        score2 = font.render('Score: ' + str(player2.score), 1, (255, 0,0))
       # back = font.render('Background  ' + str(player1.player_number) + ' is ' + str(player1.background), 1,
        #                   (0, 0, 255))

        #window.blit(back,(30,50))
        window.blit(score1, (30, 30))
        window.blit(score2,(580,30))

    else:
        score2 = font.render('Score: ' + str(player1.score), 1, (255, 0, 0))
        score1 = font.render('Score: ' + str(player2.score), 1, (0, 0, 255))
        #back = font.render('Background  ' + str(player1.player_number) + ' is ' + str(player1.background), 1,
         #                 (255, 0, 0))
        #window.blit(back, (350, 50))
        window.blit(score1, (30, 30))
        window.blit(score2, (580, 30))

    if player1.background <= -1250 and (player1.alive == False or player2.alive == False):
        pygame.draw.rect(window, (0, 255, 0), (1950 + player1.background, 200, 1, 150), 5)
    elif player1.background <=-1250:
        pygame.draw.rect(window, (255, 0, 0), (1950 + player1.background, 200, 1, 150), 5)

    if player1.background >= -550 and (player1.alive == False or player2.alive == False):
        pygame.draw.rect(window, (0, 255, 0), (550 +player1.background, 200, 1, 150), 5)
    elif player1.background >=-550:
        pygame.draw.rect(window, (255, 0, 0), (550+player1.background, 200, 1, 150), 5)

    if player1.alive and player2.alive:
        player1.draw(window)
        player2.draw(window)
    elif player1.alive:
        player1.draw(window)
    else:
        player2.draw(window)

    pygame.display.update()


def main():
    run = True
    n = Network()
    player1 = n.getP()
    clock = pygame.time.Clock()
    player2 = n.send(player1)

    while run:
        player2 = n.send(player1)
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if player1.winning:
            player1.win(window)
        elif player2.winning:
            player1.loss(window)

        if player1.respawn:
            redrawWindow(window, player1, player2)
            player1.respawn_dead(window)

        elif  player2.respawn:
            player1.background = player2.background
            redrawWindow(window, player1, player2)
            player1.respawn_kill(window)





        if player1.kill_time !=0 and player1.kill_f ==1 :
            player1.kill_f = 2
        elif player1.kill_time != 0 and player2.kill_time==0 and player1.kill_f==2:
            player1.hit(window)
        elif player1.kill_time != 0 and player2.kill_time!=0:
            if float(player1.kill_time) > float(player2.kill_time):
                player1.kill_f = 0
                player1.kill_time = 0
                player2 = n.send(player1)


            elif float(player1.kill_time) < float(player2.kill_time):
                player1.kill_f = 0
                player1.kill_time = 0
                player2 = n.send(player1)
                player1.hit(window)
            else:
                player1.kill_f = 0
                player1.kill_time = 0
                player2 = n.send(player1)
                player1.hit(window)

        elif player2.kill_time != 0  and player1.kill_time ==0 and player2.kill_f ==2 and player1.kill_f ==0:
            player1.killed(window)





        #OBYDOWJE GRACZE ZYJA
        if player2.alive and player1.alive:


            if player1.new_attack > 0:
                player1.new_attack -= 1

            if player1.attack_cooldown > 0:
                player1.attack_cooldown -= 1

            if player1.change_cooldown > 0:
                player1.change_cooldown -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if player1.attack_cooldown == 0:
                player1.move(window)

            # JESLI  JESTES Z LEWEJ
            if player1.player_number == 0:
                if player1.sword >= player2.sword and player1.position == player2.position and player1.x > 15:
                    player1.x -= 15

                else:
                    if player1.sword >= player2.hitbox[0]:
                        if player1.kill_f == 0:
                            end = time.time()
                            t = (end - player1.time)
                            player1.kill_time = t
                            player1.kill_f = 1



            # JESLI JESTES Z PRAWEJ
            elif player1.player_number == 1:
                if player1.sword <= player2.sword and player1.position == player2.position and player1.x  < 500:
                    player1.x += 15

                else:
                    if player1.sword <= player2.hitbox[0]:
                        if player1.kill_f == 0:
                            end = time.time()
                            t = (end - player1.time)
                            player1.kill_time = t
                            player1.kill_f = 1





        #TY ZYJESZ
        elif player1.alive:

            if player1.player_number == 1 and player1.background >= 0:
                player1.winning = True
            if player1.player_number == 0 and player1.background <= -1800:
                player1.winning = True


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:

                player1.background += 1
                player1.left = True
                player1.right = False

            if keys[pygame.K_RIGHT]:
                player1.background -= 1
                player1.left = False
                player1.right = True



        # NIE ZYJESZ
        elif not player1.alive:
            keys = pygame.key.get_pressed()

            if player1.death_time > 0:
                player1.death_time -= 1
            else:
                player1.respawn = True
                player1.alive=True

            player1.background = player2.background
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        elif not player1.alive and not player2.alive:
            player1.death_time=0
            player1.respawn = True
            player1.alive = True




        redrawWindow(window, player1, player2)


main()
pygame.quit()
exit()