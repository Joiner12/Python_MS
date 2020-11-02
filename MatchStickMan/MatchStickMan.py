# -*- coding:utf-8 -*-

"""

"""
import pygame
import os
import sys
import math

# 音频模块


class AudioBlock():
    def __init__(self):
        print("load audio file...")

# 图形模块


class ShapeBlock():
    def __init__(self):
        print("load shape class...")


# 主模块
class Msm():
    def __init__(self):
        sb = ShapeBlock()
        print("start show...")


# 定义颜色常量
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


def MsmDemo():
    pygame.init()
    screen = pygame.display.set_mode([1080, 960])
    pygame.display.set_caption("matchstick man")
    done = False
    clock = pygame.time.Clock()
    draw_a_boy(screen, 20, 20)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # motion
        pos = pygame.mouse.get_pos()
        # x = pos[0]
        # y = pos[1]
        x = screen.get_rect().centerx
        y = screen.get_rect().centery

        # pygame.mouse.set_visible(False)

        screen.fill(white)

        # draw_a_boy(screen,x,1)
        StikerStand(screen, x, 100)
        TitleIn(screen)

        # 设置帧率为60
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()


def draw_a_boy(screen, x, y):
    pygame.draw.ellipse(screen, black, [x, y-5, 10, 10])
    pygame.draw.line(screen, red, [5+x, 5+y], [5+x, 15+y], 2)
    pygame.draw.line(screen, red, [5+x, 5+y], [x-5, 15+y], 2)
    pygame.draw.line(screen, red, [5+x, 5+y], [15+x, 15+y], 2)
    pygame.draw.line(screen, black, [5+x, 15+y], [x-5, 25+y], 2)
    pygame.draw.line(screen, black, [5+x, 15+y], [15+x, 25+y], 2)


def StikerStand(screen, x, y):
    if True:

        pygame.draw.ellipse(screen, black, [x-50, y-100, 100, 100])   # head
        # 脖子
        pygame.draw.line(screen, red, [x, y], [x, y+60], 4)  # neck
        # 躯干
        pygame.draw.line(screen, green, [x, y+30], [x, y+60], 8)
        # 左手

        pygame.draw.line(screen, red, [x, y+30], [x-40, y+20], 4)
        pygame.draw.line(screen, red, [x-40, y+20], [x-60, y+10], 4)

        # 右手
        pygame.draw.line(screen, red, [x, y+30], [x+40, y+20], 4)
        pygame.draw.line(screen, red, [x+40, y+50], [x+60, y+10], 4)

        # 左脚
        pygame.draw.line(screen, red, [x, y+90], [x-30, y+80], 4)
        pygame.draw.line(screen, red, [x-30, y+80], [x-30, y+120], 4)
        # 右脚
        pygame.draw.line(screen, red, [x, y+90], [x+30, y+80], 4)
        pygame.draw.line(screen, red, [x+30, y+110], [x+30, y+120], 4)
    else:
         # pygame.draw.line(screen, red, [300, 620], [300, 650], 4)  # neck
        pygame.draw.ellipse(screen, black, [250, 520, 100, 100])   # head
        # 脖子
        pygame.draw.line(screen, red, [300, 620], [300, 650], 4)  # x,y|x,y+30
        # 躯干
        pygame.draw.line(screen, green, [300, 650], [
                         300, 710], 8)  # x,y+30|x,y+60
        # 左手
        pygame.draw.line(screen, red, [300, 650], [
                         260, 670], 4)  # x,y+30 x-40,y+20
        pygame.draw.line(screen, red, [260, 670], [240, 660], 4)
        # 右手
        pygame.draw.line(screen, red, [300, 650], [340, 670], 4)
        pygame.draw.line(screen, red, [340, 670], [360, 660], 4)
        # 左脚
        pygame.draw.line(screen, red, [300, 710], [270, 730], 4)
        pygame.draw.line(screen, red, [270, 730], [270, 760], 4)
        # 右脚
        pygame.draw.line(screen, red, [300, 710], [330, 730], 4)
        pygame.draw.line(screen, red, [330, 730], [330, 760], 4)


def TitleIn(screen):
    font = pygame.font.Font(None, 40)
    text = font.render("MatchStiker", True, green)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = 40  # screen.get_rect().centery
    screen.blit(text, text_rect)


if __name__ == "__main__":
    MsmDemo()
