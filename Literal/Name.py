from AST.ASTLeaf import ASTLeafYJC
from AST.ASTree import ASTreeYJC


class NameYJC(ASTLeafYJC):
    def __init__(self, token_:ASTreeYJC):
        super(NameYJC, self).__init__(token_)
    def name(self):
        return self.token_().getText()
    def value(self) -> int:
        return self.token_().getNumber()
