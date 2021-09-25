#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Something_ConditionalyjcL.py
@Author   :yujiecong
@Date     :2021/8/31 15:59 
'''

from restart.Enum.Enum import StatementType, ConditionalType
from restart.ExpressionyjcL.BinaryOperation import BinaryOperation_yjcL
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL


class SomethingConditional_yjcL(Statement_yjcL):
    def __init__(self, value):
        self.value = value
        self.type_ = StatementType.Something_Conditional
        self.fileContent = self.value["value"]
        self.statementObjects = []

    def resolve(self):
        """

        :return:
        """

        self.conditionJudge=self.value["condition_judge"]
        condition = BinaryOperation_yjcL.getExpressionValue(self.conditionJudge)

        self.conditionType = self.value["condition_type"]["type"]
        if condition:
            if self.conditionType == ConditionalType.If:
                for obj in self.statementObjects:
                    obj.resolve()
                    # print(obj)
            elif self.conditionType == ConditionalType.While:
                "直到conditionJudge失效才不执行"
                while condition:
                    for obj in self.statementObjects:
                        obj.resolve()

                    condition= BinaryOperation_yjcL.getExpressionValue(self.conditionJudge)
            elif self.conditionType==ConditionalType.ForeverLoop:
                while condition:
                    for obj in self.statementObjects:
                        obj.resolve()


    def __repr__(self):
        return r"""%s %s %s
""" % (self.conditionType, self.conditionJudge, self.fileContent)
