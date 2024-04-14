import pygame, sys
from Button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ping Pong By TOMASZ MAN i JAKUB BRYDZIŃSKI")

BG = pygame.image.load("grafika/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("grafika/font.ttf", size)


def G1():
    x = 550
    y = 640
    rakietka = pygame.rect.Rect(x, y, 200, 50) # tworzy prostokąt


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

        rakietka = pygame.rect.Rect(x, y, 200, 50)  # tworzy prostokąt

# WYKRYWANIE KRAWĘDZI OD 38 do 41 (POMOCY)
        if x <= 0:
            x += 1
        if x >= 1280:
            x -= -1

        player = pygame.rect.Rect(x, y, 40, 150)
        pygame.draw.rect(SCREEN,(255,51, 51),rakietka)
        pygame.display.update()


def G2():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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