#!/usr/bin/env python
# encoding: utf-8
'''
@author: 黄龙士
@license: (C) Copyright 2019-2021,China.
@contact: iym070010@163.com
@software: xxxxxxx
@file: parsermain.py
@time: 2019/11/26 22:31
@desc:
'''

import scannerfunc as sf
# import parserfunc as pf
import semanticfunc as paint
import os

file_name = 'test.txt'
scanner = sf.scanner(file_name)
semantic = paint.semantic(scanner)
semantic.initPaint()
semantic.Parser()
# parser = pf.Parsef(scanner)
# parser.Parser()

# os.system("pause")
