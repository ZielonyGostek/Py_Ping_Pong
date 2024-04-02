import pygame, sys
from Button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("grafika/Background.png")

def get_font(size):
    return pygame.font.Font("grafika/font.ttf", size)

def GRACZ():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
def GRACZE():
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
    print("ZASADY")

def main_menu():
    pygame.display.set_caption('Menu')

    while True:
        SCREEN.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("PING PONG", True, "#32CD32")
        MENU_RECT = MENU_TEXT.get_rect(center=(800, 250))

        GRACZ1_BUTTON = Button(image=pygame.image.load("grafika/1g.png"), pos=(640,250),text_input="1 GRACZ", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        GRACZ2_BUTTON = Button(image=pygame.image.load("grafika/2g.png"), pos=(640,400),text_input="2 GRACZ", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        ZASADY_BUTTON = Button(image=pygame.image.load("grafika/ZASADY.png"), pos=(640, 550),text_input="ZASADY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [GRACZ1_BUTTON, GRACZ2_BUTTON, ZASADY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if GRACZ1_BUTTON.checkForInput(MENU_MOUSE_POS):
                GRACZ()
            if GRACZ2_BUTTON.checkForInput(MENU_MOUSE_POS):
                GRACZE()
            if ZASADY_BUTTON.checkForInput(MENU_MOUSE_POS):
                ZASADY()
    pygame.display.update()

main_menu()



