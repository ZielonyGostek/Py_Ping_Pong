import pygame, sys
from Button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ping Pong By TOMASZ MAN i JAKUB BRYDZIŃSKI")

BG = pygame.image.load("grafika/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("grafika/font.ttf", size)


def G1():
    FPS = pygame.time.Clock()
    GREEN = (0, 100, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    player_score = 0
    game_font = pygame.font.Font('grafika/font.ttf', 40)
    Licznik_życia = 3

    S = 7

    Ball_x = 7
    Ball_y = 7

    Player = pygame.Rect(550, 640, 200, 50)
    Ball = pygame.Rect(385, 385, 30, 30)

    Bottom_wall = pygame.Rect(0, 720, 1280, 30)

    def BG_finish():
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(BLACK)
        font = pygame.font.Font(None, 100)
        text = font.render('Koniec gry Twój wynik to {}'.format(player_score), False, WHITE)
        SCREEN.blit(text, (200, 250))
        pygame.display.update()
        pygame.time.delay(5000)
        main_menu()


    def draw():
        FPS.tick(60)
        SCREEN.fill(GREEN)
        pygame.draw.rect(SCREEN, RED, Player)
        pygame.draw.ellipse(SCREEN, WHITE, Ball)
        pygame.draw.rect(SCREEN, BLACK, Bottom_wall)

    def Move():
        if keys[pygame.K_RIGHT]:
            Player.x += S
        if keys[pygame.K_LEFT]:
            Player.x -= S

    def Player_Border():
        if Player.x <= 5:
            S = 0
            Player.x = 6
        if Player.x >= 1080:
            S = 0
            Player.x = 1078

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Ball.x += Ball_x
        Ball.y += Ball_y

        if Ball.top <= 0 or Ball.bottom >= 720:
            Ball_y *= -1
        if Ball.left <= 0 or Ball.right > 1280:
            Ball_x *= -1

        if Ball.colliderect(Player):
            Ball_y *= -1
            S += 0.8
            player_score += 1

        if Ball.colliderect((Bottom_wall)):
            player_score += -1
            Licznik_życia += -1

        if Licznik_życia == 0:
            BG_finish()



        keys = pygame.key.get_pressed()

        draw()
        Move()
        Player_Border()

        player_text = game_font.render(f"{player_score}", False, BLACK)
        SCREEN.blit(player_text, (598, 150))
        pygame.display.update()

def G2():
    pygame.init()
    width = 1280
    height = 720
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption('First Game')

    value = 2
    ball_x = width / 2
    ball_y = height / 2
    ball_radius = 20
    ball_value_x = value
    ball_value_y = value

    paletka_width = 50
    paletka_height = 200
    paletka_1x = 10
    paletka_1y = 200
    paletka_2x = 1220
    paletka_2y = 200

    k = True
    player_1 = 0
    player_1s = 0
    player_2 = 0
    player_2s = 0

    def punkty(player_1s, player_2s, player_1, player_2):
        font = pygame.font.Font(None, 36)
        sety = font.render(f'{player_1s}-{player_2s}', True, (255, 255, 255))
        win.blit(sety, (630, 100))

        font = pygame.font.Font(None, 70)
        punkty = font.render(f'{player_1}-{player_2}', True, (255, 255, 255))
        win.blit(punkty, (width / 2 - 30, 30))

    def left_touch():
        return touch(paletka_1y, ball_y) and ball_x <= paletka_1x + paletka_width + ball_radius

    def right_touch():
        return touch(paletka_2y, ball_y) and ball_x >= paletka_2x - ball_radius

    def touch(paletka_y, ball_y):
        return paletka_y + paletka_height >= ball_y >= paletka_y

    def winner():
        nonlocal player_1s, player_2s, player_1, player_2
        if ball_x <= ball_radius:
            player_2, player_2s = kk(player_2, player_1, player_2s)
            # c.x += 2
        if ball_x >= width - ball_radius:
            player_1, player_1s = kk(player_1, player_2, player_1s)
            # c.x -= 2
        if player_1s == 3:
            print_winner(1)
        if player_2s == 3:
            print_winner(2)
        return player_1s, player_2s, player_1, player_2

    def kk(player_a, player_b, player_s):
        nonlocal ball_x, ball_y, player_1, player_2, k
        player_a += 1
        ball_x = 640
        ball_y = 360
        if player_a >= 11 and player_a - player_b >= 2:
            player_a = 0
            player_1 = 0
            player_2 = 0
            player_s += 1
        k = True
        return player_a, player_s

    def print_winner(player):
        font = pygame.font.Font(None, 150)
        wynik = font.render(f'Wygrał gracz: {player}', True, (255, 255, 255))
        win.blit(wynik, (200, 360))
        pygame.display.update()
        pygame.time.delay(5000)
        main_menu()



    run = True
    while run:
        pygame.time.delay(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paletka_1y != 0:
            paletka_1y -= value
        if keys[pygame.K_s] and paletka_1y != 520:
            paletka_1y += value
        if keys[pygame.K_UP] and paletka_2y != 0:
            paletka_2y -= value
        if keys[pygame.K_DOWN] and paletka_2y != 520:
            paletka_2y += value
        if keys[pygame.K_o]:
            player_1 += 1
        if keys[pygame.K_p]:
            player_2 += 1
        ball_x += ball_value_x
        ball_y += ball_value_y
        if left_touch() or right_touch():
            ball_value_x = -ball_value_x
        if (ball_y == 20 or ball_y >= 700 or
            ((paletka_1y == ball_y - ball_radius or paletka_1y - paletka_height == ball_y + ball_radius) and paletka_1x <= ball_x <= paletka_1x + paletka_width) or ((paletka_2y == ball_y - ball_radius or paletka_2y - paletka_height == ball_y + ball_radius) and paletka_2x <= ball_x <= paletka_2x + paletka_width)):
            ball_value_y = -ball_value_y
        winner()

        win.fill((0, 100, 0))
        punkty(player_1s, player_2s, player_1, player_2)
        pygame.draw.rect(win, (255, 0, 0),
                         (paletka_1x, paletka_1y, paletka_width, paletka_height))
        pygame.draw.rect(win, (0, 0, 0),
                         (paletka_2x, paletka_2y, paletka_width, paletka_height))
        pygame.draw.circle(win, (255, 255, 255), (ball_x, ball_y), ball_radius)
        pygame.display.update()
        if k:
            pygame.time.delay(3000)
            k = False
    pygame.quit()





def ZASADY():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        G1_TEXT = get_font(45).render("1 GRACZ", True, "White")
        G1_RECT = G1_TEXT.get_rect(center=(200, 90))
        SCREEN.blit(G1_TEXT, G1_RECT)

        G1_ZASADY_TEXT = get_font(15).render("Gracz porusza się strzałkami lewo, prawo.",  True, "White")
        G1_ZASADY_RECT = G1_ZASADY_TEXT.get_rect(center=(340, 140))

        G1_ZASADY2_TEXT = get_font(15).render("Każde odbicie piłki od rakiety to jeden punkt.", True, "White")
        G1_ZASADY2_RECT = G1_ZASADY2_TEXT.get_rect(center=(380, 160))

        G1_ZASADY3_TEXT = get_font(15).render("Gracz ma trzy szanse, aby grać dalej. każde piłka, która spadnie daje -1 punkt.", True, "White")
        G1_ZASADY3_RECT = G1_ZASADY3_TEXT.get_rect(center=(625, 180))

        SCREEN.blit(G1_ZASADY_TEXT, G1_ZASADY_RECT)
        SCREEN.blit( G1_ZASADY2_TEXT, G1_ZASADY2_RECT)
        SCREEN.blit( G1_ZASADY3_TEXT, G1_ZASADY3_RECT)


        G2_TEXT = get_font(45).render("2 GRACZ", True, "White")
        G2_RECT = G2_TEXT.get_rect(center=(200, 350))
        SCREEN.blit(G2_TEXT, G2_RECT)

        G2_ZASADY4_TEXT = get_font(15).render("Gracz czewony porusza się 'W' 'S' a gracz czarny porusza się strzałkami góra dół.", True, "White")
        G2_ZASADY4_RECT = G2_ZASADY4_TEXT.get_rect(center=(615, 400))
        SCREEN.blit(G2_ZASADY4_TEXT, G2_ZASADY4_RECT)

        G2_ZASADY5_TEXT = get_font(15).render("Każdy set gra się do 11 punktów.", True, "White")
        G2_ZASADY5_RECT = G2_ZASADY5_TEXT.get_rect(center=(250, 425))
        SCREEN.blit(G2_ZASADY5_TEXT, G2_ZASADY5_RECT)

        G2_ZASADY6_TEXT = get_font(15).render("Wygrywa zawodnik, który uzyska te 3 sety jako pierwszy.", True, "White")
        G2_ZASADY6_RECT = G2_ZASADY6_TEXT.get_rect(center=(450, 445))
        SCREEN.blit(G2_ZASADY6_TEXT, G2_ZASADY6_RECT)

        OPTIONS_BACK = Button(image=None, pos=(1205, 650),
                              text_input="BACK", font=get_font(30), base_color="Grey", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Ping Pong", True, "#32cd32")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        G1_BUTTON = Button(image=pygame.image.load("grafika/1g.png"), pos=(640, 250),
                             text_input="1 GRACZ", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        G2_BUTTON = Button(image=pygame.image.load("grafika/2g.png"), pos=(640, 400),
                                text_input="2 GRACZY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ZASADY_BUTTON = Button(image=pygame.image.load("grafika/ZASADY.png"), pos=(640, 550),
                             text_input="ZASADY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [G1_BUTTON, G2_BUTTON, ZASADY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if G1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    G1()
                if G2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    G2()
                if ZASADY_BUTTON.checkForInput(MENU_MOUSE_POS):
                   ZASADY()

        pygame.display.update()


main_menu()