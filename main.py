import pygame, sys
from Button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ping Pong By TOMASZ MAN i JAKUB BRYDZIŃSKI")

BG = pygame.image.load("grafika/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("grafika/font.ttf", size)


def G1():
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
   #położenie początkowe rakietki
    x = 550
    y = 640
    rakietka = pygame.rect.Rect(x, y, 200, 50) # tworzy prostokąt

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #położenie początkowe piłki
    '''bx = 600
    by = 350

    radius = 20
    width = 1280
    height = 720
    szerokosc_p = 50
    wysokosc_p = 200
    def raketka_touch(rakietka,x,y, bx, by):
        return rakietka + wysokosc_p'''


    object_size = 30
    object_x = SCREEN_WIDTH // 2
    object_y = SCREEN_HEIGHT // 2
    object_speed_x = 5
    object_speed_y = 5

    rakietka_speed_x = 5


    while True:
        SCREEN.fill((0, 100, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # czy strzałka w prawo jest naciskana
            x += 1
        if keys[pygame.K_LEFT]:  # STRZAłKA W LEWO
            x -= 1



        rakietka_speed_x += object_speed_x
        object_x += object_speed_x
        object_y += object_speed_y

        # Odbijanie od krawędzi ekranu
        if object_x <= 0 or object_x + object_size >= SCREEN_WIDTH:
            object_speed_x *= -1
        if object_y <= 0 or object_y + object_size >= SCREEN_HEIGHT:
            object_speed_y *= -1
        rakietka = pygame.rect.Rect(x, y, 200, 50)  # tworzy prostokąt


        # Opóźnienie, aby nie przekraczać zadanej prędkości klatek na sekundę
        pygame.time.Clock().tick(60)

        # WYKRYWANIE KRAWĘDZI
        if x <= 0:
            x += 1
        if x >= 1080:
            x -= 1


        pygame.draw.rect(SCREEN, BLACK, (object_x, object_y, object_size, object_size))
        player = pygame.rect.Rect(x, y, 40, 150)
        pygame.draw.rect(SCREEN,(255,51, 51),rakietka)
       # ball = pygame.draw.circle(SCREEN, (255, 255, 255), (bx, by), 20)
        pygame.display.update()


def G2():
    radius = 20
    width = 1280
    height = 720
    szerokosc_p = 50
    wysokosc_p = 200

    def left_touch(paletka_1y, paletka_1x, wysokosc_p, ball_x, ball_y):
        return paletka_1y + wysokosc_p >= ball_y >= paletka_1y and ball_x <= paletka_1x + szerokosc_p + radius

    # x + szerokość_p  >= piłka_y >= x and y == piłka _y - radius

    def right_touch(paletka_2y, paletka_2x, wysokosc_p, ball_x, ball_y):
        return paletka_2y + wysokosc_p >= ball_y >= paletka_2y and ball_x >= paletka_2x - radius

    def winner(ball_x):
        if ball_x <= 0:
            print_winner(1)
        if ball_x >= width:
            print_winner(2)

    def print_winner(player):
        print(f'Paletka {player} wygrała')
        pygame.time.delay(1000)
        exit()

    pygame.init()

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption('First Game')

    paletka_1y = 200
    paletka_2y = 200
    paletka_1x = 10
    paletka_2x = 1220
    k = True
    value = 1
    ball_x = 340
    ball_y = 620
    value_ballx = value
    value_bally = value
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
        ball_x += value_ballx
        ball_y += value_bally
        if left_touch(paletka_1y, paletka_1x, wysokosc_p, ball_x, ball_y) or \
                right_touch(paletka_2y, paletka_2x, wysokosc_p, ball_x, ball_y):
            value_ballx = -value_ballx
        if (
                ball_y == 20 or ball_y >= 700 or
                (paletka_1y == ball_y - 20 and 10 <= ball_x <= 60) or
                (paletka_1y == ball_y - wysokosc_p - 20 and 10 <= ball_x <= 60) or
                (1220 <= ball_x <= 1270 and (paletka_2y ==
                                             ball_y - wysokosc_p - 20 or paletka_2y == ball_y))
        ):
            value_bally = -value_bally
        winner(ball_x)
        print(paletka_1y, paletka_2y)
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0),
                         (paletka_1x, paletka_1y, szerokosc_p, wysokosc_p))
        pygame.draw.rect(win, (255, 0, 0),
                         (paletka_2x, paletka_2y, szerokosc_p, wysokosc_p))
        pygame.draw.circle(win, (255, 255, 255), (ball_x, ball_y), radius)
        pygame.display.update()
        if k:
            pygame.time.delay(2000)
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

        G2_ZASADY_TEXT = get_font(20).render("Gracz porusza się strzałkami lewo, prawo", True, "White")
        G2_ZASADY_RECT = G2_ZASADY_TEXT.get_rect(center=(480, 400))
        SCREEN.blit(G2_ZASADY_TEXT, G2_ZASADY_RECT)

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