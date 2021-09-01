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
    ForeverLoop="FOREVER_LOOP"

class ExpressionType:
    BinaryOperation="BinaryOperation"
    Expression="Expression"

class StatementType:
    Statement="Statement"
    PrintSomething="PrintSomething"
    Something_Conditional="Something_Conditional"
    Assignment="Assignment"
    ForLoop="ForLoop"

class TokenType:
    String="STRING"
    Identifier="IDENTIFIER"
    Number="NUMBER"
    Float="Float"