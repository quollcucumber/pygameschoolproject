import pygame
import sys
import random

pygame.init()

dif = 0

WIDTH, HEIGHT = 1000, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# takes font from no file, of size 36
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
easymediumhard = pygame.image.load("easymediumhard.png")
while running:
    screen.fill((255, 255, 255))
    screen.blit(easymediumhard, (0, 0))
    dificultytext = font.render("Choose dificulty", True, (0, 0, 0))
    screen.blit(dificultytext, (330, 10))
    #TODO Hadrien make better easy medium hard images
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):
                pos = pygame.mouse.get_pos()
                # print(pos[0])
                # print(pos[1])
                if 80 <= pos[1] <= 250:
                    running = False
                    if 30 <= pos[0] <= 300:
                        dif = 1
                    elif 330 <= pos[0] <= 600:
                        dif = 2
                    elif 630 <= pos[0] <= 950:
                        dif = 3
                    else:
                        running = True

    pygame.display.flip()
    clock.tick(60)

# pygame.quit()

font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
rows, cols = 10, 10
if dif == 2:
    rows = 15
    cols = 15
elif dif == 3:
    rows = 20
    cols = 20

grid = []
for i in range(rows * cols):
    if random.randint(0, 5) == 0:
        grid.append(10)
    else:
        grid.append(0)


def find(row, col):
    if row >= rows or row < 0 or col >= cols or cols < 0:
        return 0
    return grid[row * rows + col]


def edit(row, col, setval):
    if row >= rows or row < 0 or col >= cols or cols < 0:
        return
    grid[row * rows + col] = setval
    return


# for i in range(rows * colums):
#     print(grid[i])
for row in range(rows):
    a = []
    for col in range(cols):
        if find(row, col) != 10:
            total = 0
            if find(row + 1, col + 1) == 10:
                total += 1
            if find(row + 1, col - 1) == 10:
                total += 1
            if find(row + 1, col) == 10:
                total += 1
            if find(row, col + 1) == 10:
                total += 1
            if find(row, col - 1) == 10:
                total += 1
            if find(row - 1, col + 1) == 10:
                total += 1
            if find(row - 1, col) == 10:
                total += 1
            if find(row - 1, col - 1) == 10:
                total += 1
            edit(row, col, total)
        a.append(find(row, col))
    print(a)                

while running:
    screen.fill((255, 255, 255))
    if (dif == 1):
        dificultytext = font.render("EASY", True, (0, 0, 0))
    elif (dif == 2):
        dificultytext = font.render("MEDIUM", True, (0, 0, 0))
    else:
        dificultytext = font.render("HARD", True, (0, 0, 0))
    screen.blit(dificultytext, (470, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

sys.exit()
