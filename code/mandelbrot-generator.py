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

screenWidth=900
screenHeight=630
screenCaption="Mandelbrot Generator"

pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption(screenCaption)
screen.fill((255,255,255))
pygame.display.update()

def generate(x0,y0,x1,y1):
    for px in range(screenWidth):
        for py in range(screenHeight):
            xm=(px/screenWidth*(x1-x0))+x0
            ym=(py/screenHeight*(y1-y0))+y0

            x=0
            y=0

            iteration=0
            maxIteration=2000

            while (x*x + y*y)<4 and iteration<maxIteration:
                xTemp=x*x-y*y+xm
                y=2*x*y+ym
                x=xTemp
                iteration+=1

            arr=iteration/maxIteration
            arr=arr**0.3
            color=palette[floor(arr*(len(palette)-1))]
            pygame.Surface.set_at(screen,(px,py),color)
        pygame.display.update()
    print("done")

x0s=-2
y0s=-1.12
x1s=0.47
y1s=1.12

generate(x0s,y0s,x1s,y1s)

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
                    x0t=mPos1[0]/screenWidth*(x1s-x0s)+x0s
                    y0t=mPos1[1]/screenHeight*(y1s-y0s)+y0s
                elif mPos2==False:
                    mPos2=pygame.mouse.get_pos()
                    x1t=mPos2[0]/screenWidth*(x1s-x0s)+x0s
                    y1t=mPos2[1]/screenHeight*(y1s-y0s)+y0s
                    x0s=x0t
                    y0s=y0t
                    x1s=x1t
                    y1s=y1t
                    mPos1=False
                    mPos2=False
                    print(f'x0s={x0s}\ny0s={y0s}\nx1s={x1s}\ny1s={y1s}')
                    generate(x0s,y0s,x1s,y1s)

        if event.type==pygame.K_EQUALS:
            pygame.image.save(screen, f"picx/{datetime.datetime.now()}.jpg")