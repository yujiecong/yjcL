from Token.TokenYJC import TokenYJC


class YjcParseError(SyntaxError):
    def getLocation(self, token:TokenYJC):
        if token==TokenYJC.EOF:
            return "the last line"
        else:
            return "SyntaxError %s at line %s"%(token.getText(),token.getLineNumber())