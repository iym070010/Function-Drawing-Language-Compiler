#!/usr/bin/env python
# encoding: utf-8
'''
@author: 黄龙士
@license: (C) Copyright 2019-2021,China.
@contact: iym070010@163.com
@software: xxxxxxx
@file: semanticfunc.py.py
@time: 2019/11/30 10:47
@desc:
'''

import parserfunc as pf
import scannerclass as sc
import numpy as np
import turtle
import sys
import matplotlib
import matplotlib.pyplot as plt

class semantic(pf.Parsef):
    def initPaint(self):    # 初始化画布
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def Errmsg(self):   #出错处理
        sys.exit(1)

    def CalcCoord(self,x,y):    # 计算点坐标   即比例旋转平移变换 x,y都是二元组
        x = x * self.Scale_x
        y = y * self.Scale_y     ## 进行比例变换
        tmp_x = x * np.cos(self.Rot_angle) + y * np.sin(self.Rot_angle)
        y = y * np.cos(self.Rot_angle) - x * np.sin(self.Rot_angle)
        x= tmp_x        ## 旋转变换
        x = x + self.Origin_x
        y = y + self.Origin_y   ## 进行平移变换
        return x,y


    def DrawLoop(self):
        x,y = self.CalcCoord(self.x_ptr,self.y_ptr)
        self.ax.scatter(x,y)


    def Statement(self):    ## 重写statement ，让每次ForStatement执行完毕后画图
        self.enter("Statement")
        if self.token.type == sc.Token_Type.ORIGIN:
            self.OriginStatement()
        elif self.token.type == sc.Token_Type.SCALE:
            self.ScaleStatement()
        elif self.token.type == sc.Token_Type.ROT:
            self.RotStatement()
        elif self.token.type == sc.Token_Type.FOR:
            self.ForStatement()
            self.DrawLoop()
        # elif self.token.type == sc.Token_Type.CONST_ID or self.token.type == sc.Token_Type.L_BRACKET or \
        #     self.Expression()
        else:   self.SyntaxError(2)
        self.back("Statement")

    # 绘图语言解释器入口（与主程序的外部接口）
    def Parser(self):  # 语法分析器的入口
        self.enter("Parser")
        if (self.scanner.fp == None):  # 初始化词法分析器
            print("Open Source File Error !\n")
        else:
            self.FetchToken()  # 获取第一个记号
            self.Program()  # 递归下降分析
            plt.show()
            self.scanner.CloseScanner()  # 关闭词法分析器
            self.back("Parser")