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
from restart.Enum.Enum import StatementType
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
import restart.Global.Variable

class Assignment_yjcL(Statement_yjcL):
    def __init__(self,value):
        self.raw=value
        self.type_=StatementType.Assignment
        self.value=self.raw["value"]
        # {'type': 'Assignment', 'value': ('圆圆是屑', 1)}
        self.key=self.value[0]
        self.item=self.value[1]
        restart.Global.Variable.GlobalVariable.__var__[self.key]=self.item
