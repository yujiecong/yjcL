#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :ForLoop.py
@Author   :yujiecong
@Date     :2021/9/1 11:57 
'''
import collections
from typing import List, Any

from restart.Enum.Enum import StatementType, ExpressionType, TokenType
from restart.ExpressionyjcL.BinaryOperation import BinaryOperation_yjcL
from restart.Statement_yjcL.Assignment import Assignment_yjcL
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
from restart.TokenyjcL.Token import Token_yjcL


class ForLoop_yjcL(Statement_yjcL):
    statementObjects: List[Statement_yjcL]

    def __init__(self, value):
        self.raw = value
        self.type_ = StatementType.ForLoop
        self.fileContent=self.raw["value"]
        self.forChar=self.raw["for_char"]["value"]
        self.identifier=self.raw["identifier"]["value"]
        self.statementObjects = []

    def resolve(self):
        """

        :return:
        """
        self.expression=self.raw["expression"]
        expressionType=self.expression["type"]


        expressionValue=BinaryOperation_yjcL.getExpressionValue(self.expression)

        if isinstance(expressionValue,collections.Iterable):
            for _ in expressionValue:
                pass
        elif isinstance(expressionValue,int):
            for i in range(expressionValue):
                "为了方便 ,这里不算一个statement"
                assignMent=Assignment_yjcL({'identifier': {'value': self.identifier, 'type': 'IDENTIFIER'}, 'expression': {'value': i, 'type': 'NUMBER'}, 'type': 'Assignment'})
                assignMent.resolve()
                for obj in self.statementObjects:
                    obj.resolve()

    def __repr__(self):
        return "ForLoop_yjcL %s %s in %s"%(
            self.forChar,self.identifier,self.expression["value"]
        )



