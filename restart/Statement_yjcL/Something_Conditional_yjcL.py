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
import restart.Global.Variable
from restart.Enum.Enum import StatementType
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
from restart.TokenyjcL.Token_yjcL import TokenyjcL


class Something_Conditional_yjcL(Statement_yjcL):
    def __init__(self,value):
        self.raw=value
        self.type_=StatementType.Something_Conditional
        self.subCode=self.raw["value"]
        self.condition_judge=TokenyjcL.getValue(self.raw["condition_judge"])
        self.conditionType=self.raw["condition_type"]["value"]

    def __repr__(self):
        if self.condition_judge:
            return "%s %s 整挺好" % (self.conditionType, self.condition_judge)

        else:
            return "%s %s 是屑" % (self.conditionType, self.condition_judge)