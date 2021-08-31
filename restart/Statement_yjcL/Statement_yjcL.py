#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Statement_yjcL.py
@Author   :yujiecong
@Date     :2021/8/31 15:57 
'''
import abc




class Statement_yjcL(abc.ABC):
    def __init__(self):
        self.value=None
        self.type_ = None
        self.children=[]

    @abc.abstractmethod
    def resolve(self):
        pass