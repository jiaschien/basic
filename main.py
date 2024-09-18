import pygame
import sys
import random

# 全局定义
SCREEN_X = 600
SCREEN_Y = 600


# 蛇类
# 点以25为单位
class Snake(self):
    # 初始化各种需要的属性[开始时默认向右/身体块X5]
    def __init__(self):
        self.direction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
	    self.addnode()

    # 无论何时 都在前端增加蛇块
    def addnode(self):
        left,top = (0,0)
        if self.body:
            left,top = (self.body[0].left, self.body[0].top)
        node = pygame.rect(left,top,25,25)
        if self.direction == pygame.K_LEFT:
            node.left -= 25
        elif self.direction == pygame.K_RIGHT:
            node.right += 25
        elif self.direction == pygame.K_UP:
            node.top -= 25
        elif self.direction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0,node)

    # 删除最后一个块
    def delnode(self):
        self.body.pop()

    # 死亡判断
    def isdead(self):
        # 撞墙


