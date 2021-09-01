import json
import pprint

from Parser_yjcL import *
from restart.Enum.Enum import TokenType, ConditionalType
from restart.FileContent_yjcL.FileContent_yjcL import FileContent_yjcL
from restart.Statement_yjcL.Assignment_yjcL import Assignment_yjcL
from restart.Statement_yjcL.ForLoop_yjcL import ForLoop_yjcL
from restart.Statement_yjcL.PrintSomething_yjcL import PrintSomething_yjcL
from restart.Statement_yjcL.Something_Conditional_yjcL import Something_Conditional_yjcL
from restart.Statement_yjcL.Statement_yjcL import Statement_yjcL


class yjcLAST():
    def __init__(self, sourceCode):
        self.sourceCode = sourceCode
        self.lexer = lex.lex()
        self.lexer.input(sourceCode)

    def printTokens(self):
        for i, l in enumerate(self.lexer):
            print(str(i + 1) + "=>", l)

    def parseToken(self, token: dict):
        type_ = token["type"]
        if type_ == TokenType.Identifier:
            return self.__var__[token["value"]]
        elif type_ == TokenType.Number or type_ == TokenType.String:
            return token["value"]

    def parse(self):
        """

        :return:
        """
        parser = yacc()
        self.astJson = parser.parse(self.sourceCode)
        with open("ast.json", 'w', encoding="utf8") as f:
            json.dump(self.astJson, f, sort_keys=True, indent=4)

        self.fileContent = FileContent_yjcL()
        self.fileContent.children=self.json2ASObjectTree(self.astJson["value"],[])
        self.exec()

        # pprint.pprint(self.astJson)

    def json2ASObjectTree(self, ast,objs,recursion=False):
        """
        根据json构建对象树 递归定义
        :return:
        """

        statements = ast["value"]
        # pprint.pprint(statements)
        for statement in statements:
            # pprint.pprint(statement)
            statementType = statement["type"]
            statementObject = None
            if statementType == StatementType.PrintSomething:
                statementObject = PrintSomething_yjcL(statement)
            elif statementType == StatementType.Assignment:
                statementObject = Assignment_yjcL(statement)
            elif statementType == StatementType.Something_Conditional:
                # pprint.pprint(statement)
                statementObject = Something_Conditional_yjcL(statement)
                statementObject.statementObjects=self.json2ASObjectTree(statementObject.subCode, [], recursion=True)
            elif statementType==StatementType.ForLoop:
                statementObject=ForLoop_yjcL(statement)
            objs.append(statementObject)
        return objs

    def exec(self):
        """
        根据ast给出的statement执行代码
        :return:
        """
        for statement in self.fileContent:
            statement.resolve()
            # print(statement)



if __name__ == "__main__":
    with open("demo.yjcl", encoding="utf8") as f:
        data = f.read()
    astree = yjcLAST(data)
    astree.parse()
    # print(__var__)
