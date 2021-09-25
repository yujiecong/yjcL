#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Enum.py
@Author   :yujiecong
@Date     :2021/8/31 13:39 
'''

class Source:
    SourceCode="SourceCode"

class ConditionalType:
    If="IF"
    While="WHILE"

class ExpressionType:
    BinaryOperation="BinaryOperation"
    Expression="Expression"

class StatementType:
    Statement="Statement"
    PrintSomething="PrintSomething"
    Something_Conditional="Something_Conditional"
    Assignment="Assignment"
    BinaryOperation="BinaryOperation"

class TokenType:
    String="STRING"
    Identifier="IDENTIFIER"
    Number="NUMBER"



综合=7+9+13.5+7+9+12.6+9.3+13.5+5.5+8.75+4.75

学分=3+3+3+2.5+2.5+2.5+2+2+2+2+3

# print((综合/学分+5)*9)

# 3.632727272727273
print(0.2*85+77.69*0.7+3.6)
