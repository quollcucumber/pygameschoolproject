import pygame
import sys
import random

pygame.init()

pygame.display.set_caption("Minesweeper")
dif = 0

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# takes font from no file, of size 36
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()


def resize_image(img, new_height):
    """
    This function makes an image taller or shorter while keeping its shape.

    Steps:
    1. Get the original width and height of the image.
    2. Work out the aspect ratio (how wide vs how tall it is).
    3. Use the new height to calculate the new width, so the image is not squashed.
    4. Use pygame.transform.scale to resize the image.
    5. Return (give back) the resized image.
    """

    # Get the original height and width of the image
    original_height = img.get_height()
    original_width = img.get_width()

    # Work out how wide the image is compared to its height
    aspect_ratio = original_width / original_height

    # Calculate the new width so the image keeps the same proportions
    new_width = int(new_height * aspect_ratio)

    # Scale (resize) the image to the new width and height
    img = pygame.transform.scale(img, (new_width, new_height))

    # Give back the resized image so the rest of the program can use it
    return img


running = True
background = pygame.image.load("Minesweeper Mine.jpg")
background = resize_image(background, 650)
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    text = font.render("EASY                              MEDIUM                           HARD", True, (255, 255, 255))
    screen.blit(text, (100, 150))
    dificultytext = font.render("Choose dificulty", True, (255, 255, 255))
    screen.blit(dificultytext, (330, 10))
    # TODO Hadrien make better easy medium hard images
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
for i in range(rows):
    a = []
    for j in range(cols):
        if random.randint(0, 7) == 0:
            a.append(10)
        else:
            a.append(0)
    grid.append(a)


def find(row, col):
    if row >= rows or row < 0 or col >= cols or cols < 0:
        return 0
    return grid[row][col]


def edit(row, col, setval):
    if row >= rows or row < 0 or col >= cols or cols < 0:
        return
    grid[row][col] = setval
    return


# for i in range(rows * colums):
#     print(grid[i])
for row in range(rows):
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


tile = pygame.image.load("Minesweeper Tile.jpg")
tile_height = 400 / rows + 1
tile = resize_image(tile, tile_height)
flagtile = pygame.image.load("Minesweeper Flag.png")
flagtile = resize_image(flagtile, tile_height)
neighbor0 = pygame.image.load("Minesweeper 0.jpg")
neighbor0 = resize_image(neighbor0, tile_height)
neighbor1 = pygame.image.load("Minesweeper 1.png")
neighbor1 = resize_image(neighbor1, tile_height)
neighbor2 = pygame.image.load("Minesweeper 2.png")
neighbor2 = resize_image(neighbor2, tile_height)
neighbor3 = pygame.image.load("Minesweeper 3.png")
neighbor3 = resize_image(neighbor3, tile_height)
neighbor4 = pygame.image.load("Minesweeper 4.png")
neighbor4 = resize_image(neighbor4, tile_height)
neighbor5 = pygame.image.load("Minesweeper 5.png")
neighbor5 = resize_image(neighbor5, tile_height)
neighbor6 = pygame.image.load("Minesweeper 6.png")
neighbor6 = resize_image(neighbor6, tile_height)
neighbor7 = pygame.image.load("Minesweeper 7.png")
neighbor7 = resize_image(neighbor7, tile_height)
neighbor8 = pygame.image.load("Minesweeper 8.png")
neighbor8 = resize_image(neighbor8, tile_height)
flags = []
q = []
opened = []
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(0)
    opened.append(a)
for i in range(rows):
    a = []
    for j in range(cols):
        a.append(0)
    flags.append(a)

def bfs():
    while len(q) != 0:
        row, col = q[len(q) - 1]
        q.pop()
        if 0 <= row < rows and 0 <= col < cols:
            if opened[row][col] != 1:
                opened[row][col] = 1
                if find(row, col) == 0:
                    q.append((row + 1, col))
                    q.append((row + 1, col - 1))
                    q.append((row + 1, col + 1))
                    q.append((row, col + 1))
                    q.append((row, col - 1))
                    q.append((row - 1, col + 1))
                    q.append((row - 1, col))
                    q.append((row - 1, col - 1))

def youwin():
    for i in range(rows):
        for j in range(cols):
            if not (opened[i][j] == 1 or (flags[i][j] == 1 and find(i, j) == 10)):
                return 0
    return 1


while running:
    if youwin() == 1:
        print("YOU WIN!")
        running = False
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for i in range(rows):
        prints = []
        for j in range(cols):
            a = find(i, j)
            prints.append(a)
            pos = (300 + j * 400 / cols, 100 + i * 400 / rows)
            if flags[i][j] == 0:
                # if opened[i][j] == 0:
                if opened[i][j] == 0:
                    screen.blit(tile, pos)
                else:
                    if find(i, j) == 0:
                        screen.blit(neighbor0, pos)
                    elif find(i, j) == 1:
                        screen.blit(neighbor1, pos)
                    elif find(i, j) == 2:
                        screen.blit(neighbor2, pos)
                    elif find(i, j) == 3:
                        screen.blit(neighbor3, pos)
                    elif find(i, j) == 4:
                        screen.blit(neighbor4, pos)
                    elif find(i, j) == 5:
                        screen.blit(neighbor5, pos)
                    elif find(i, j) == 6:
                        screen.blit(neighbor6, pos)
                    elif find(i, j) == 7:
                        screen.blit(neighbor7, pos)
                    elif find(i, j) == 8:
                        screen.blit(neighbor8, pos)
            else:
                screen.blit(flagtile, pos)
        # print(prints)
    if dif == 1:
        dificultytext = font.render("EASY", True, (255, 255, 255))
    elif dif == 2:
        dificultytext = font.render("MEDIUM", True, (255, 255, 255))
    else:
        dificultytext = font.render("HARD", True, (255, 255, 255))
    screen.blit(dificultytext, (470, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                row = int((pos[1] - 100) / int(400 / cols))
                col = int((pos[0] - 300) / int(400 / rows))
                if 0 <= row < rows and 0 <= col < cols:
                    q.append((row, col))
                    bfs()
                    if find(row, col) == 10:
                        print("YOU DIED")
                        running = False

            elif event.button == 3:
                #right click, add/remove a flag
                pos = pygame.mouse.get_pos()
                row = int((pos[1] - 100) / int(400 / cols))
                col = int((pos[0] - 300) / int(400 / rows))
                if 0 <= row < rows and 0 <= col < cols:
                    flags[row][col] = 1 - flags[row][col]
    pygame.display.flip()
    clock.tick(60)
    # running = False

pygame.quit()

sys.exit()
