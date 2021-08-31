#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :FileContent_yjcL.py
@Author   :yujiecong
@Date     :2021/8/31 16:08 
'''
from restart.SourceCode_yjcL.SourceCode_yjcL import SourceCode_yjcL
from restart.VariableDict import VariableDict


class FileContent_yjcL(SourceCode_yjcL):
    def __init__(self,):
        self.children=[]
        self.__var__ = VariableDict()

    def addChild(self, statement):
        self.children.append(statement)