#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :BinaryOperation.py
@Author   :yujiecong
@Date     :2021/8/31 15:40 
'''
import pprint


from restart.Enum.Enum import ExpressionType
from restart.ExpressionyjcL.Expression import Expression_yjcL
from restart.TokenyjcL.Token import Token_yjcL


class BinaryOperation_yjcL(Expression_yjcL):
    def __init__(self, raw):
        """
        {'left': {'type': 'IDENTIFIER', 'value': '圆圆是屑'},
           'op': '+',
           'right': {'type': 'IDENTIFIER', 'value': '聪聪傻逼'},
           'type': 'BinaryOperation'}
        :rtype: object
        :param raw:
        """
        self.raw=raw
        self.left = self.raw["left"]
        self.op = self.raw["op"]
        self.right = self.raw["right"]
        self.type=ExpressionType.BinaryOperation
        # pprint.pprint(self.raw)
        self.value=self.getValue(self.raw)


    def getValue(self,raw):
        """
        递归获取左右子树
        :return:
        """

        "如果左右子树仍然是expression 那么继续递归"
        left=raw["left"]
        right=raw["right"]
        op=raw["op"]
        lType=left["type"]
        rType=right["type"]

        if lType==ExpressionType.BinaryOperation :
            lValue= self.getValue(left)
        else:
            lValue = Token_yjcL.getValue(left)
        if  rType==ExpressionType.BinaryOperation:
            rValue= self.getValue(right)
        else:
            rValue = Token_yjcL.getValue(right)
        # print(left, right)
        # lValue=Token_yjcL.getValue(left)
        # rValue=Token_yjcL.getValue(right)

        resultValue=None
        if op=="+":
            resultValue=lValue+rValue
        elif op=="-":
            resultValue = lValue - rValue
        elif op=="*":
            resultValue = lValue * rValue
        elif op=="/":
            resultValue = lValue / rValue
        elif op==">"or op=="大于":
            resultValue = lValue > rValue
        elif op=="<"or op=="小于":
            resultValue = lValue < rValue
        elif op==">="or op=="大于等于":
            resultValue = lValue >= rValue
        elif op=="<="or op=="小于等于":
            resultValue = lValue <= rValue
        elif op=="==" or op=="相等":
            resultValue = lValue == rValue
        elif op=="!="or op=="不等":
            resultValue = lValue != rValue
        return resultValue

    @staticmethod
    def getExpressionValue(valueDict):

        if valueDict["type"]==ExpressionType.BinaryOperation:
            return BinaryOperation_yjcL(valueDict).value
        else:
            return Token_yjcL.getValue(valueDict)

