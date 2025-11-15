import pygame
import sys
import random
pygame.init()

dif = 0



WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# takes font from no file, of size 36
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True

while running:
    screen.fill((255, 255, 255))
    dificultytext = font.render("Choose dificulty", True, (0, 0, 0))
    screen.blit(dificultytext, (160, 10))
    #TODO Create images of easy medium hard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                pos = pygame.mouse.get_pos()
                print(pos[0])
                print(pos[1])
                #TODO Check where click, and set dif accordingly
                dif = 1
                running = False

    pygame.display.flip()
    clock.tick(60)

# pygame.quit()

font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

while running:
    screen.fill((255, 255, 255))
    if(dif == 1):
        dificultytext = font.render("EASY", True, (0, 0, 0))
    elif(dif == 2):
        dificultytext = font.render("MEDIUM", True, (0, 0, 0))
    else:
        dificultytext = font.render("HARD", True, (0, 0, 0))
    screen.blit(dificultytext, (200, 10))
    #TODO Create images of easy medium hard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 1):
                #TODO Check where click, and set dif accordingly
                dif = 1
                running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

sys.exit()
