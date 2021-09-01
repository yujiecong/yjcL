#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Assignment.py
@Author   :yujiecong
@Date     :2021/8/31 16:53 
'''
from restart.Enum.Enum import StatementType, TokenType, ExpressionType
from restart.ExpressionyjcL.BinaryOperation import BinaryOperation_yjcL
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
import restart.Global.Variable
from restart.TokenyjcL.Token import Token_yjcL


class Assignment_yjcL(Statement_yjcL):
    def __init__(self, value):

        self.raw = value
        self.type_ = StatementType.Assignment
        self.identifier=self.raw["identifier"]["value"]
        self.expression = self.raw["expression"]

    @staticmethod
    def assign(k,v):
        """

        :param k:
        :param v:
        """
        _v = restart.Global.Variable.GlobalVariable.__var__
        _v[k]=v

    def resolve(self):
        _v=restart.Global.Variable.GlobalVariable.__var__

        self.item=BinaryOperation_yjcL.getExpressionValue(self.expression)

        _v[ self.identifier] = self.item

    def __repr__(self):
        return "Assignment %s=%s" % (self.identifier, self.item)
