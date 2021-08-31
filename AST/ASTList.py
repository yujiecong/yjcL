import abc
import collections

import typing

from AST.ASTree import ASTreeYJC
from Token.TokenYJC import TokenYJC


class ASTListYJC(ASTreeYJC):
    def __init__(self,childrenList:typing.List[ASTreeYJC]):
        self._children = childrenList



    def child(self, childIndex: int) ->ASTreeYJC:
        """

        :type childIndex: int
        """
        return self._children[childIndex]


    def childrenNum(self) -> int:
        return len(self._children)


    def children(self) -> collections.Iterable:
        for child in self._children:
            yield child

    def location(self) -> str:
        for child in self._children:
            loc=child.location()
            if loc is not None:
                return loc
        return None

    def toString(self):
        builder="("
        sep=""
        for child in self._children:
            builder+=sep
            sep=" "
            builder+=child.toString()
        return builder+")"

    def iterator(self):
        return

