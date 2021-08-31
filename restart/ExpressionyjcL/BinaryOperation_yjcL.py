#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :BinaryOperation.py
@Author   :yujiecong
@Date     :2021/8/31 15:40 
'''
from restart.ExpressionyjcL.Expression_yjcL import Expression_yjcL


class BinaryOperation(Expression_yjcL):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def getValue(self):
        pass

