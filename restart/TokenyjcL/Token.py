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
import abc

import restart.Global.Variable
from restart.Enum.Enum import TokenType, ExpressionType


class Token_yjcL(abc.ABC):
    def __init__(self, valueDict):
        self.type_ = valueDict["type"]
        self.value = valueDict["value"]

    @staticmethod
    def getValue(valueDict):
        """

        :param valueDict:
        :return:
        """
        type_ = valueDict["type"]
        value = valueDict["value"]

        if type_ == TokenType.Identifier:
            _v = restart.Global.Variable.GlobalVariable.__var__
            return _v[value]
        else:
            return value
