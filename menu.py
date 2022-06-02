import pygame
import sys
import tkinter
from tkinter import *
pygame.init()
res = (1500, 800)
screen = pygame.display.set_mode(res)
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
img2 = pygame.image.load('logo.png')

text = smallfont.render('Wyjście', True, color)
text1 = smallfont.render('Start', True, color)
text2 = smallfont.render('Instrukcja', True, color)


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width / 2 + 240 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()
            if width / 2 <= mouse[0] <= width / 2 + 240 and (height / 2)-200 <= mouse[1] <= (height / 2)-200 + 40:
                import main
            if width / 2 <= mouse[0] <= width / 2 + 240 and (height / 2)-100 <= mouse[1] <= (height / 2)-100 + 40:
                okno = Tk()
                def Close():
                    okno.destroy()
                okno.geometry("600x200")
                okno.title('Instrukcja')
                okno.komunikat = tkinter.Label(text="Aby podskoczyć żółwiem wciśnij SZTAŁKĘ W GÓRĘ\n\nZa każdą pokonaną przeszkodę otrzymasz punkty!\n\nPowodzenia! ", font= 30)
                okno.komunikat.pack(pady=35)
                cl_but = Button(okno,text='Wszystko jasne!', font= 30, fg='green', command=Close)
                cl_but.pack()
                okno.mainloop()
    screen.fill((60, 115, 60))
    screen.blit(img2, (150,220))

    mouse = pygame.mouse.get_pos()

    if width / 2 <= mouse[0] <= width / 2 + 240 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 240, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 240, 40])
    screen.blit(text, (width / 2 + 50, height / 2))
    if width / 2 <= mouse[0] <= width / 2 + 240 and (height / 2)-200 <= mouse[1] <= (height / 2)-200 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, (height / 2)-200, 240, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, (height / 2)-200, 240, 40])
    screen.blit(text1, (width / 2 + 50, (height / 2)-200))
    if width / 2 <= mouse[0] <= width / 2 + 240 and (height / 2)-100 <= mouse[1] <= (height / 2)-100 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, (height / 2)-100, 240, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, (height / 2)-100, 240, 40])
    screen.blit(text2, (width / 2 + 50, (height / 2)-100))


    pygame.display.update()
