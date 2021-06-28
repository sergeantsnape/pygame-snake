import random
import time
import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake.exe")
clk = pygame.time.Clock()


def text_msg(n, s, x, y, c):
    base_font = pygame.font.Font('Poppins-Bold.ttf', n)
    text = base_font.render(s, True, c)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    return text, text_rect


def splash_screen():
    screen.fill((255, 255, 255))
    img = pygame.image.load('833674.png')
    screen.blit(img, (50, 50))
    text, text_rect = text_msg(20, 'PRESS |___| TO PLAY', 250, 400, (0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.update()

    play = True
    while play:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                play = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return game_loop()

    pygame.quit()


def game_over():
    text1, text_rect1 = text_msg(60, 'GAME OVER', 250, 125, (255, 0, 0))
    screen.blit(text1, text_rect1)
    text2, text_rect2 = text_msg(20, "PLAY AGAIN", 250, 250, (255, 0, 0))
    screen.blit(text2, text_rect2)
    text3, text_rect3 = text_msg(20, "(Y/N)", 250, 275, (255, 0, 0))
    screen.blit(text3, text_rect3)
    pygame.display.update()

    again = True
    while again:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                again = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_y:
                    return game_loop()
                if e.key == pygame.K_n:
                    again = False

    pygame.quit()


def game_loop():
    # <<- variables ->>
    run = True
    x, y = 250, 250
    c_w = 10
    x_c = -1
    y_c = -1
    v = 10
    s = 5
    s_l = []
    leng = 1
    move = False
    # <<- ---------- ->>

    # grid of 10X10 px
    f_x = round(random.randrange(0, 500 - c_w) / 10) * 10
    f_y = round(random.randrange(0, 500 - c_w) / 10) * 10

    # <<-Main game loop->>
    while run:
        # pygame.time.Clock()
        # closing window (default)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP :
                    if leng == 1:
                        y_c, x_c = -v, 0
                    if leng != 1 and x_c !=0:
                        y_c, x_c = -v, 0
                    move = True
                if event.key == pygame.K_DOWN :
                    if leng == 1:
                        y_c, x_c = v, 0
                    if leng != 1 and x_c != 0:
                        y_c, x_c = v, 0
                    move = True
                if event.key == pygame.K_RIGHT :
                    if leng == 1:
                        x_c, y_c = v, 0
                    if leng != 1 and y_c != 0:
                        x_c, y_c = v, 0
                    move = True
                if event.key == pygame.K_LEFT:
                    if leng == 1:
                        x_c, y_c = -v, 0
                    if leng != 1 and y_c != 0:
                        x_c, y_c = -v, 0
                    move = True

        screen.fill((200, 200, 200))

        # movement initialization
        if move:
            y += y_c
            x += x_c

        # hits block
        if y >= 500 - c_w or y < 0 or x >= 500 - c_w or x < 0:
            time.sleep(0.3)
            game_over()

        # snake body constraints
        s_l.append([x, y])
        if len(s_l) > leng:
            s_l.pop(0)
        for i in s_l[:-1]:
            if i == [x, y]:
                game_over()

        # snake body
        for mov in s_l:
            pygame.draw.rect(screen, (255, 255, 255), (mov[0], mov[1], c_w, c_w))

        # food
        pygame.draw.rect(screen, (255, 0, 0), (f_x, f_y, c_w, c_w))

        # snake eats food
        if x == f_x and y == f_y:
            f_x = round(random.randrange(0, 500 - 2 * c_w) / 10) * 10
            f_y = round(random.randrange(0, 500 - 2 * c_w) / 10) * 10
            leng += 1
            s += 0.8

        # score board
        score = pygame.font.Font('Poppins-Thin.ttf', 20).render('SCORE  ' + str(leng - 1), True, (0, 0, 0))
        screen.blit(score, (0, 0))

        # refreshes the screen (default)
        pygame.display.update()
        clk.tick(s)
    pygame.quit()


def main():
    splash_screen()


if __name__ == '__main__':
    main()
