import abc
import collections

from AST.ASTree import ASTreeYJC
from Token.TokenYJC import TokenYJC


class ASTLeafYJC(ASTreeYJC):
    def __init__(self, token: TokenYJC):
        self._empty = []
        self._token = token

        pass


    def child(self, childIndex: int):
        pass


    def childrenNum(self) -> int:
        return 0


    def children(self) -> collections.Iterable:
        for emp in self._empty:
            yield emp


    def location(self) -> str:
        return "at line "+self._token.getLineNumber()


    def token_(self):
        return self._token

    def toString(self):
        return self._token.getText()
