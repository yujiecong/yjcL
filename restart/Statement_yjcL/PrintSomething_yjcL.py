#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :PrintSomething_yjcL.py
@Author   :yujiecong
@Date     :2021/8/31 15:58 
'''
import pprint

from restart.Enum.Enum import StatementType, TokenType, ExpressionType
import restart.Global.Variable
from restart.ExpressionyjcL.BinaryOperation_yjcL import BinaryOperation_yjcL
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL


class PrintSomething_yjcL(Statement_yjcL):
    def __init__(self,value):
        super(PrintSomething_yjcL, self).__init__()
        self.raw=value
        self.type_=StatementType.PrintSomething
        self.resolve()


    def resolve(self):

        printWhat = self.raw["value"] #打印的内容
        printType = printWhat["type"] #打印的字符
        self.printKey=self.raw["print_key"]
        self.printChar=self.printKey["value"]

        if printType==TokenType.String or printType==TokenType.Number:
            self.printValue = printWhat["value"]
        elif printType==TokenType.Identifier:
            printValue = printWhat["value"]
            self.printValue=restart.Global.Variable.GlobalVariable.__var__[printValue]
        elif printType == ExpressionType.BinaryOperation:
            op=BinaryOperation_yjcL(printWhat)

            self.printValue=op.value
            self.children.append(op)

        print(self)

    def __repr__(self):
        return "屑%s >> %s"%(self.printChar,self.printValue)
