from enum import Enum,unique
from math import sqrt
from random import randint,random
import pygame

@unique
class Color(Enum):

    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GRAY = (242,242,242)

    @staticmethod
    def random_color():
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)

class Ball(object):

    def __init__(self,x,y,radius,sx,sy,color = Color.random_color()):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self,screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self,other):
        if self.alive and other.alive and self != other:
            dx,dy = abs(self.x-other.x),abs(self.y-other.y)
            if sqrt(dx**2+dy**2) < self.radius + other.radius \
                    and self.radius>other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * round(random()))

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)


def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("大球吃小球")
    screen.fill((255,255,255))
    # x,y = 50,50
    # screen.fill((242,242,242))
    # ball = pygame.image.load('./ball.png')
    # screen.blit(ball,(50,50))
    # pygame.draw.circle(screen,(255,0,0),(100,100),30,0)
    # pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                radius = randint(10,50)
                sx,sy = randint(-10,10),randint(-10,10)
                color = Color.random_color()
                ball = Ball(x,y,radius,sx,sy,color)
                balls.append(ball)
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        pygame.display.flip()
        pygame.time.delay(50)

        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)
        # pygame.draw.circle(screen,(255,0,0),(x,y),20,0)
        # pygame.display.flip()
        # pygame.time.delay(50)
        # x,y = x+5,y+5

if __name__ == "__main__":
    main()