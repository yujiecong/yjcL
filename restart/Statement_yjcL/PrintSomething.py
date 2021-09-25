#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :PrintSomething.py
@Author   :yujiecong
@Date     :2021/8/31 15:58 
'''
import pprint

from restart.Enum.Enum import StatementType, TokenType, ExpressionType
import restart.Global.Variable
from restart.ExpressionyjcL.BinaryOperation import BinaryOperation_yjcL
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL
from restart.TokenyjcL.Identifier import Identifier_yjcL
from restart.TokenyjcL.Number import Number_yjcL
from restart.TokenyjcL.String import String_yjcL
from restart.TokenyjcL.Token import Token_yjcL


class PrintSomething_yjcL(Statement_yjcL):
    def __init__(self,value):
        super(PrintSomething_yjcL, self).__init__()
        self.raw=value
        self.type_=StatementType.PrintSomething



    def resolve(self):

        printWhat = self.raw["value"] #打印的内容
        printType = printWhat["type"] #打印的字符
        self.printKey=self.raw["print_key"]
        self.printChar=self.printKey["value"]

        self.printValue=BinaryOperation_yjcL.getExpressionValue(printWhat)

        print(self)
        # self.children.append(printedClass)

    def __repr__(self):
        return "PrintSomething 屑%s >> %s"%(self.printChar,self.printValue)
