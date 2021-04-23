import pygame as p

WIDTH =HEIGHT = 1024
S_SIZE =512
B_SIZE = 768


def main():
    p.init()
    screen = p.display.set_mode((HEIGHT,WIDTH))
    screen.fill(color='white')
    running =True
    drawGameState(screen)
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        p.display.flip()

def drawGameState(screen):
    drawBoard(screen)
    drawBalls(screen)

def drawBoard(screen):
    color=[p.Color('green'),p.Color('black'),p.Color('white')]
    p.draw.rect(screen, color[1], p.Rect(124, 124, B_SIZE+8, S_SIZE+8))
    p.draw.rect(screen,color[0],p.Rect(128,128,B_SIZE,S_SIZE))
    p.draw.circle(screen,color[1], (144,144), 15)
    p.draw.circle(screen,color[1], (880,144), 15)
    p.draw.circle(screen,color[1], (144,624), 15)
    p.draw.circle(screen,color[1], (880,624), 15)
    p.draw.circle(screen,color[1], (512,624), 15)
    p.draw.circle(screen,color[1], (512,144), 15)
    p.draw.line(screen,color[2], (328,638), (328,130), 3)

def drawBalls(screen):
    pass




main()