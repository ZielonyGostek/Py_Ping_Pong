import pygame

pygame.init()
window = pygame.display.set_mode((1200, 800)) # WYMIARY TŁA W PX




run = True
while run:
    pygame.time.Clock().tick(60) # 60 OZNACZA ŻE PĘTLA WYKONUJE SIĘ 60 RAZY NA SEKUNDĘ
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # ZAMKNIĘCIE PRZEZ UŻYTKOWNIKA X
            run = False
    TYTUŁ= pygame.font.Font.render(pygame.font.SysFont("Sonic Cut", 345), "Ping Pong", True, (31, 112, 31))


    window.fill((65, 66, 65)) # RYSOWANIE TŁA
    window.blit(TYTUŁ, (0,0))
    pygame.display.update()

