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
    # base path
    os.chdir(os.path.dirname(__file__))
    pygame.init()
    screen = pygame.display.set_mode([900, 600])
    pygame.display.set_caption("matchstick man")
    bg = pygame.image.load(r'./Src/Background/bg-1.png')

    # 在绘制完所有图像后，再统一调用update方法

    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.blit(bg, (0, 0))
        # motion
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x = screen.get_rect().centerx
        y = screen.get_rect().centery
        # screen.fill(white)
        StikerStand(screen, mouse_x, mouse_y)
        TitleIn(screen)
        pygame.display.update()

    pygame.quit()


def StikerStand(screen, x, y):
    if True:
        pygame.draw.ellipse(screen, black, [x-50, y-100, 100, 100])   # head
        # 脖子
        pygame.draw.line(screen, red, [x, y], [x, y+30], 4)  # neck
        # 躯干
        pygame.draw.line(screen, green, [x, y+30], [x, y+90], 8)
        # 左手
        pygame.draw.line(screen, red, [x, y+30], [x-40, y+50], 4)
        pygame.draw.line(screen, red, [x-40, y+50], [x-60, y+40], 4)
        # 右手
        pygame.draw.line(screen, red, [x, y+30], [x+40, y+50], 4)
        pygame.draw.line(screen, red, [x+40, y+50], [x+60, y+40], 4)
        # 左脚
        pygame.draw.line(screen, red, [x, y+90], [x-30, y+110], 4)
        pygame.draw.line(screen, red, [x-30, y+110], [x-30, y+140], 4)
        # 右脚
        pygame.draw.line(screen, red, [x, y+90], [x+30, y+110], 4)
        pygame.draw.line(screen, red, [x+30, y+110], [x+30, y+140], 4)


def TitleIn(screen):
    font = pygame.font.Font(None, 40)
    text = font.render("MatchStiker", True, green)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = 40  # screen.get_rect().centery
    screen.blit(text, text_rect)


if __name__ == "__main__":
    MsmDemo()
