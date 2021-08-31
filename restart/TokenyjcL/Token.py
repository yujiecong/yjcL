#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Token.py
@Author   :yujiecong
@Date     :2021/8/31 15:38 
'''
import restart.Global.Variable
from restart.Enum.Enum import TokenType, ExpressionType



class Token_yjcL:
    @staticmethod
    def getValue(valueDict):
        type_=valueDict["type"]
        value=valueDict["value"]

        if type_==TokenType.String:
            return value
        elif type_==TokenType.Number:
            return value
        elif type_==TokenType.Identifier:
            return restart.Global.Variable.GlobalVariable.__var__[value]

