from enum import Enum
import numpy as np

Token_Type = Enum('Token_Type', ('ORIGIN', 'SCALE', 'ROT', 'IS', 'TO', 'STEP', 'DRAW', 'FOR', 'FROM',   #保留字
                                 'T',   #参数
                                 'SEMICO', 'L_BRACKET','R_BRACKET','COMMA', #分隔符
                                 'PLUS','MINUS','MUL','DIV','POWER',    #运算符
                                 'FUNC',    #函数符
                                 'CONST_ID',    #常数
                                 'NONTOKEN',    #空记号
                                 'ERRTOKEN'))   #出错记号

class Tokens:   #记号类
    #type：记号类别
    #lexeme：输入的字符串/属性
    #value：常数值
    #funcptr：函数指针
    def __init__(self,type,lexeme,value,funcptr):
        self.lexeme=lexeme
        self.value=value
        self.funcptr=funcptr
        if type in Token_Type:
            self.type = type
        else:
            print("Invalid type")     # 后续待填充

Alphabet=dict([('PI',Tokens(Token_Type.CONST_ID,"PI",3.1415926,None)),      ##符号表
           ('E',Tokens(Token_Type.CONST_ID,"E",2.71828,None)),
           ('T',Tokens(Token_Type.T,'T',0.0,None)),
           ('SIN',Tokens(Token_Type.FUNC,'SIN',0.0,np.sin)),   # math.sin / math.sinh
           ('COS',Tokens(Token_Type.FUNC,'COS',0.0,np.cos)),
           ('TAN',Tokens(Token_Type.FUNC,'TAN',0.0,np.tan)),
           ('LN',Tokens(Token_Type.FUNC,'LN',0.0,np.log)),
           ('EXP',Tokens(Token_Type.FUNC,'EXP',0.0,np.exp)),
           ('SQRT',Tokens(Token_Type.FUNC,'SQRT',0.0,np.sqrt)),
           ('ORIGIN',Tokens(Token_Type.ORIGIN,'ORIGIN',0.0,None)),
           ('SCALE',Tokens(Token_Type.SCALE,'SCALE',0.0,None)),
           ('ROT',Tokens(Token_Type.ROT,'ROT',0.0,None)),
           ('IS',Tokens(Token_Type.IS,'IS',0.0,None)),
           ('FOR',Tokens(Token_Type.FOR,'FOR',0.0,None)),
           ('FROM',Tokens(Token_Type.FROM,'FROM',0.0,None)),
            ('TO',Tokens(Token_Type.TO,'TO',0.0,None)),
            ('STEP',Tokens(Token_Type.STEP, 'STEP', 0.0, None)),
            ('DRAW',Tokens(Token_Type.DRAW, 'DRAW', 0.0, None))])