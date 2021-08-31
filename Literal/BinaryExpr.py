import typing

from AST.ASTLeaf import ASTLeafYJC
from AST.ASTList import ASTListYJC
from AST.ASTree import ASTreeYJC


class BinaryExprYJC(ASTListYJC):
    LeftHandNum=0
    Operator=1
    RightHandNum=2
    def __init__(self, ASTreeList: typing.List[ASTreeYJC]):
        super(BinaryExprYJC, self).__init__(ASTreeList)

    def left(self) -> ASTreeYJC:
        return self.child(self.LeftHandNum)

    def operator(self) -> str:
        """

        :return:
        """
        return self.child(self.Operator).token().getText()
    def right(self)->ASTreeYJC:
        return self.child(self.RightHandNum)
