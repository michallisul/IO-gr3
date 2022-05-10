import pygame
import sys
import random
import time

black = (0, 0, 0)
white = (255, 255, 255)
green = (34, 139, 34)
blue = (64, 224, 208)
GREY = (150,150,150)

def read_from_file(board):
    file = open(board, 'r')
    lines = file.readlines()
    file.close

    high_score = 0
    high_name = ""
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)

        if score > high_score:
            high_score = score
            high_name = name

    return high_name, high_score

def write_to_file(board, your_name, score):
    with open(board, 'a') as score_file:
        print(your_name +",",score)
    score_file.close()


def show_top(surface, board):
    bx = 480
    by = 400
    file = open(board, 'r')
    lines = file.readlines()

    all_score = []
    for line in lines:
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep + 1:-1])
        all_score.append((score, name))
    file.close
    all_score.sort(reverse=True)
    best = all_score[:5]

    box = pygame.surface.Surface((bx, by))
    box.fill(GREY)
    pygame.draw.rect(box, white, (50, 12, bx - 100, 35), 0)
    pygame.draw.rect(box, white, (50, by - 60, bx - 100, 42), 0)
    pygame.draw.rect(box, black, (0, 0, bx, by), 1)
    txt_surf = font.render("HIGHSCORE", True, black)
    txt_rect = txt_surf.get_rect(center=(bx // 2, 30))
    box.blit(txt_surf, txt_rect)

    for i, entry in enumerate(best):
        txt_surf = font.render(entry[1] + " " + str(entry[0]), True, black)
        txt_rect = txt_surf.get_rect(center=(bx // 2, 30 * i + 60))
        box.blit((txt_surf, txt_rect))

    box.blit(box, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                return
        pygame.time.wait(20)

def enterbox(surface, txt):
    def blink(surface):
        for color in [GREY, white]:
            pygame.draw.circle(box, color, (bx // 2, int(by * 0.7)), 7, 0)
            surface.blit(box, (0, by // 2))
            pygame.display.flip()
            pygame.time.wait(300)

    def show_name(surface, name):
        pygame.draw.rect(box, white, (50, 60, bx - 100, 20), 0)
        txt_surf = font.render(name, True, black)
        txt_rect = txt_surf.get_rect(center=(bx // 2, int(by * 0.7)))
        box.blit(txt_surf, txt_rect)
        surface.blit(box, (0,by//2))
        pygame.display.flip()

    bx = 480
    by = 100
    font = pygame.font.SysFont("Arial", 16)

    # make box
    box = pygame.surface.Surface((bx, by))
    box.fill(GREY)
    pygame.draw.rect(box, black, (0, 0, bx, by), 1)
    txt_surf = font.render(txt, True, black)
    txt_rect = txt_surf.get_rect(center=(bx // 2, int(by * 0.3)))
    box.blit(txt_surf, txt_rect)

    name = ""
    show_name(surface, name)



def highscore(surface, board, your_points):
    high_name, high_score = read_from_file(board)

    if your_points > high_score:
        your_name = enterbox(surface, "YOU HAVE BEATEN THE HIGHSCORE - What is your name?")
    elif your_points == high_score:
        your_name = enterbox(surface, "YOU HAVE SAME AS HIGHSCORE - What is your name?")
    elif your_points < high_score:
        st1 = "Highscore is "
        st2 = " made by "
        st3 = "   What is your name?"
        txt = st1 + str(high_score) + st2 + high_name + st3
        your_name = enterbox(surface, txt)

    if your_name == None or len(your_name) == 0:
        return
    write_to_file(board, your_name, your_points)
    show_top(score, board)
    return