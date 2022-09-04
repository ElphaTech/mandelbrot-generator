import pygame
from math import floor
import datetime

palette = []

for r in range(256):
    palette.append((r,0,0))
for g in range(256):
    palette.append((255,g,0))
for r in range(256):
    palette.append((255-r,255,0))
for b in range(256):
    palette.append((0,255,b))
for g in range(256):
    palette.append((0,255-g,255))
for r in range(256):
    palette.append((r,0,255))
for g in range(256):
    palette.append((255,g,255))

screenWidth=1700
screenHeight=990
screenCaption="Mandelbrot Generator"

pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption(screenCaption)
screen.fill((255,255,255))
pygame.display.update()

def generate():
    for px in range(screenWidth):
        for py in range(screenHeight):
            x0=(px/screenWidth*2.47)-2
            y0=(py/screenHeight*2.24)-1.12

            x=0
            y=0

            iteration=0
            maxIteration=50

            while (x*x + y*y)<4 and iteration<maxIteration:
                xTemp=x*x-y*y+x0
                y=2*x*y+y0
                x=xTemp
                iteration+=1

            arr=iteration/maxIteration
            arr=arr**0.1
            color=palette[floor(arr*(len(palette)-1))]
            pygame.Surface.set_at(screen,(px,py),color)
        pygame.display.update()
    print("done")

generate()

mPos1=False
mPos2=False

while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type==pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pressed()[0]:
                if mPos1==False:
                    mPos1=pygame.mouse.get_pos()
                    print(mPos1)
                elif mPos2==False:
                    mPos2=pygame.mouse.get_pos()
                    print(mPos2)
        if event.type==pygame.K_EQUALS:
            pygame.image.save(screen, f"picx/{datetime.datetime.now()}.jpg")