from AST.ASTLeaf import ASTLeafYJC


class NumberLiteralYJC(ASTLeafYJC):
    def __init__(self, token_):
        super(NumberLiteralYJC, self).__init__(token_)

    def value(self) -> int:
        return self.token_().getNumber()
