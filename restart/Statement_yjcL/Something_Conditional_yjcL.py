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
import pprint

import restart.Global.Variable
from restart.Enum.Enum import StatementType, ConditionalType
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
from restart.TokenyjcL.Token import Token_yjcL


class Something_Conditional_yjcL(Statement_yjcL):
    def __init__(self, value):
        self.value = value
        self.type_ = StatementType.Something_Conditional
        self.subCode = self.value["value"]
        self.statementObjects = []

    def resolve(self):
        """

        :return:
        """
        self.conditionJudge = Token_yjcL.getValue(self.value["condition_judge"])

        self.conditionType = self.value["condition_type"]["type"]

        if self.conditionJudge:
            if self.conditionType == ConditionalType.If:
                for obj in self.statementObjects:

                    obj.resolve()
                    # print(obj)
            elif self.conditionType == ConditionalType.While:
                "直到conditionJudge失效才不执行"
                while self.conditionJudge:
                    for obj in self.statementObjects:

                        obj.resolve()
                        # print(obj)
                    self.conditionJudge= Token_yjcL.getValue(self.value["condition_judge"])

    def __repr__(self):
        return r"""%s %s{
   %s     
}
""" % (self.conditionType, self.conditionJudge, self.subCode)
