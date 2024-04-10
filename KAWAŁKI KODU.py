# PORUSZANIE SIĘ STRZAŁKAMI

x = 70
y = 50
player = pygame.rect.Rect(x, y, 40, 150) # TWORZY PROSTOKAT


keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: # czy strzałka w prawo jest naciskana
        x += 1
    if keys[pygame.K_LEFT]: # STRZAłKA W LEWO
        x -= 1
    if keys[pygame.K_UP]: # STRZAŁKA W GÓRĘ
        y -= 1
    if keys[pygame.K_DOWN]: # STRZAŁKA W DÓŁ
        y += 1

    player = pygame.rect.Rect(x, y, 40, 150)

pygame.draw.rect(window, (50, 205, 50), player)  # RYSOWANIE RAKIETKI

Każde odbicie piłki od rakiety to jeden punkt.

PLAY_MOUSE_POS = pygame.mouse.get_pos()

SCREEN.fill((0, 100, 0))

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

