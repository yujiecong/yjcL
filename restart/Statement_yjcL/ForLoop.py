#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :ForLoop_yjcL.py
@Author   :yujiecong
@Date     :2021/9/1 11:57 
'''
from restart.Enum.Enum import StatementType, ExpressionType, TokenType
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
from restart.TokenyjcL.Token import Token_yjcL


class ForLoop_yjcL(Statement_yjcL):
    def __init__(self, value):
        self.raw = value
        self.type_ = StatementType.ForLoop
        self.statementObjects = []

    def resolve(self):
        """

        :return:
        """

        identifier=self.raw["identifier"]
        expression=self.raw["expression"]
        expressionType=expression["type"]


        if expressionType!=ExpressionType.BinaryOperation:
            expressionValue=Token_yjcL.getValue(identifier)
        else:
            expressionValue=Expression







    def __repr__(self):
        return r"""%s %s{
           %s     
        }
        """ % (self.conditionType, self.conditionJudge, self.subCode)


