#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME: 2020/5/13 16:35
# @Author: K
# @File: LearnTurtle.py
from turtle import *

# width(4)
# forward(200)
# right(90)
# pencolor('red')
# forward(100)
# right(90)
#
# pencolor('green')
# forward(200)
# right(90)
#
# pencolor('blue')
# forward(100)
# right(90)
#
# done()

# def drawStar(x, y):
# 	pu()
# 	goto(x, y)
# 	pd()
#
# 	seth(0)
# 	for i in range(5):
# 		fd(40)
# 		rt(144)
#
# for x in range(0, 250, 50):
# 	drawStar(x, 0)
#
# done()

# colormode(255)
#
# lt(90)
#
# lv = 14
# l = 120
# s = 45
#
# width(lv)
#
# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)
#
# penup()
# bk(l)
# pendown()
# fd(l)
#
# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()
#
#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0 * l
#
#     lt(s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)
#
#     # restore the previous pen width
#     width(w)
#
# speed("fastest")
#
# draw_tree(l, 4)
#
# done()

# import time
#
# ht()
#
# speed(0)
#
# penup()
#
# goto(0, 120)
#
# pendown()
#
# for i in range(12):
#
#     right(90)
#
#     forward(10)
#
#     backward(10)
#
#     left(90)
#
#     for j in range(4):
#
#         circle(-120, 6)
#
#         right(90)
#
#         forward(5)
#
#         backward(5)
#
#         left(90)
#
#     circle(-120, 6)
#
# penup()
#
# goto(0, 0)
#
# pendown()
#
# def pin(p, long, angle):
#
#     p.left(90 - angle)
#
#     p.forward(long)
#
# def undopin(p):
#
#     for _ in range(2):
#
#         p.undo()
#
# fen = clone()
#
# miao =  clone()
#
# miaolong = 100
#
# fenlong = 60
#
# miaoang = 0
#
# fenang = 0
#
# while True:
#
#     pin(fen, fenlong, fenang)
#
#     for i in range(60):
#
#         pin(miao, miaolong, miaoang + (i * 6))
#
#         time.sleep(0.93)
#
#         undopin(miao)
#
#     undopin(fen)
#
#     fenang += 6