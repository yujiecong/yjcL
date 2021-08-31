#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Assignment_yjcL.py
@Author   :yujiecong
@Date     :2021/8/31 16:53 
'''
from restart.Enum.Enum import StatementType, TokenType, ExpressionType
from restart.ExpressionyjcL.BinaryOperation_yjcL import BinaryOperation_yjcL
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
import restart.Global.Variable
from restart.TokenyjcL.Token import Token_yjcL


class Assignment_yjcL(Statement_yjcL):
    def __init__(self, value):
        self.raw = value
        self.type_ = StatementType.Assignment
        self.identifier=self.raw["identifier"]

        self.expression = self.raw["expression"]
        # {'type': 'Assignment', 'value': ('圆圆是屑', 1)}

    def resolve(self):

        self.key = self.identifier["value"]
        expressionType=self.expression["type"]
        if expressionType!=ExpressionType.BinaryOperation:
            self.item=Token_yjcL.getValue(self.expression)
        else:
            self.item=BinaryOperation_yjcL.getBinaryOperationValue(self.expression)
        restart.Global.Variable.GlobalVariable.__var__[self.key] = self.item

    def __repr__(self):
        return "Assignment %s=%s" % (self.key, self.item)
