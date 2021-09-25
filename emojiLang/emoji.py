import ast
import json
import pprint
import re

from ply import lex
from ply.yacc import yacc

lex.eof = False

reserved = {
    "📇": "PRINT",
}
tokens = [
             "IDENTIFIER",
             "STRING",
             "EQUAL",
             "NUMBER",
             "LEFT_PAREN",
             "RIGHT_PAREN",
             "ENDMARKER",
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
         ] + list(set(reserved.values()))

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_EQUAL = r"="
t_LEFT_PAREN = r"\("
t_RIGHT_PAREN = r"\)"

# t_NEWLINE = r';'
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# A regular expression rule with some action code
def t_STRING(t):
    r"""("(\\\\"|\\\\\\\\|\\\\n|[^"])*")|('(\\\\'|\\\\\\\\|\\\\n|[^'])*')"""
    t.value = {
        "value": t.value[1:-1],
        "type": "STRING"
    }
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = {
        "value": int(t.value),
        "type": "NUMBER"
    }
    return t


def t_IDENTIFIER(t):
    r"""[\U00010000-\U0010ffff]+"""
    type_ = reserved.get(t.value, 'IDENTIFIER')
    t.value = {
        "value": t.value,
        "type": type_
    }  # Check for reserved words
    t.type = type_
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_eof(t):
    if lex.eof:
        return None
    t = lex.LexToken()
    t.type = 'ENDMARKER'
    t.value = 'EOF'
    t.lineno = -1
    t.lexpos = 0
    lex.eof = True
    return t


# Error handling rule
def t_error(t):
    print("屑字符 '%s' Unicode=%s" % (t.value[0],t.value[0].encode("utf8")))
    t.lexer.skip(1)


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)


def p_sourcecode(p):
    """SourceCode : ENDMARKER
                  | FileContent ENDMARKER"""

    if len(p) == 3:
        p[0] = {
            "type": "SourceCode",
            "value": p[1]
        }
    else:
        p[0] = {
            "type": "SourceCode",
            "value": []
        }


def p_file_content(p):
    '''FileContent : FileContent Statement
                   | Statement
           '''
    if len(p) == 3:
        p[1]["value"].append(p[2])
        p[0] = p[1]
    else:
        p[0] = {
            "type": "FileContent",
            "value": [p[1]]
        }


def p_statement(p):
    """Statement : Assignment
                | PrintSomething
                | Expression"""
    # print(p[1])
    p[0] = p[1]

    # print("Statement",p[0])


def p_assignment(p):
    "Assignment : IDENTIFIER EQUAL Expression"
    idDict = p[1]
    exprDict = p[3]
    p[0] = {
        "identifier": idDict,
        "expression": exprDict,
        "type": "Assignment"
    }


def p_binary_opeartion(p):
    """ Expression : Expression PLUS Expression
                | Expression MINUS Expression
                | Expression TIMES Expression
                | Expression DIVIDE Expression"""

    valueDict = {}
    valueDictLeft = p[1]
    valueDictRight = p[3]

    valueDict["left"] = valueDictLeft
    valueDict["right"] = valueDictRight
    valueDict["op"] = p[2]
    valueDict["type"] = "BinaryOperation"

    p[0] = valueDict


def p_expression(p):
    """Expression : NUMBER
                 | STRING
                 | IDENTIFIER
                 | LEFT_PAREN Expression RIGHT_PAREN
                 """
    # print(p[1])
    if len(p) == 2:
        valueDict = p[1]
        p[0] = valueDict

    elif len(p) == 4:
        if p[1] == "(":
            p[0] = p[2]


def p_expr_uminus(p):
    'Expression : MINUS Expression %prec UMINUS'
    p[2]["value"] = -p[2]["value"]
    p[0] = p[2]


def p_print_something(p):
    """
    PrintSomething : PRINT LEFT_PAREN Expression RIGHT_PAREN
    """
    valueDict = p[3]

    p[0] = {
        "value": valueDict,
        'type': "PrintSomething",
        "print_key": p[1]
    }


def p_error(p):
    if p:
        print('syntax error {}'.format(p))


__emojiDict__ = {}


class TokenType:
    String = "STRING"
    Identifier = "IDENTIFIER"
    Number = "NUMBER"


class TokenEmoji:
    @staticmethod
    def getValue(valueDict):
        type_ = valueDict["type"]
        value = valueDict["value"]
        if type_ == TokenType.String:
            return value
        elif type_ == TokenType.Number:
            return value
        elif type_ == TokenType.Identifier:
            return __emojiDict__[value]


class BinaryOperation():
    def __init__(self, raw):
        self.raw = raw
        self.left = self.raw["left"]
        self.op = self.raw["op"]
        self.right = self.raw["right"]
        self.type = "BinaryOperation"
        self.value,self.string = self.getValue(self.raw)

    def getValue(self, raw):
        """如果左右子树仍然是expression 那么继续递归"""
        left = raw["left"]
        right = raw["right"]
        op = raw["op"]
        lType = left["type"]
        rType = right["type"]
        resultValue = None
        resultStr=None
        if lType == "BinaryOperation":
            lValue,lStr = self.getValue(left)
        else:
            lValue = TokenEmoji.getValue(left)
            lStr=left["value"]

        if rType == "BinaryOperation":
            rValue,rStr= self.getValue(right)
        else:
            rValue = TokenEmoji.getValue(right)
            rStr=right["value"]
        if op == "+":

            resultValue = lValue + rValue
            resultStr=f"{lStr}+{rStr}"
        elif op == "-":
            resultValue = lValue - rValue
            resultStr=f"{lStr}-{rStr}"
        elif op == "*":
            resultValue = lValue * rValue
            resultStr=f"{lStr}*{rStr}"
        elif op == "/":
            resultValue = lValue / rValue
            resultStr=f"{lStr}/{rStr}"
        return resultValue,resultStr

    @staticmethod
    def getBinaryOperationValue(valueDict):
        bo=BinaryOperation(valueDict)
        return bo.value,bo.string


def json2ASObjectTree(ast):
    """
    解析json语法树
    :return:
    """
    statements = ast["value"]
    for statement in statements:
        statementType = statement["type"]
        # pprint.pprint(statement)
        if statementType == "PrintSomething":
            statementValue=statement["value"]
            printType = statementValue["type"]
            if printType=="BinaryOperation":
                v,s = BinaryOperation.getBinaryOperationValue(statementValue)
                print(f"{s} = {v}")
            else:
                k=statementValue["value"]
                print(f"{k} = {__emojiDict__[k]}")
        elif statementType == "Assignment":
            exp = statement["expression"]
            if exp["type"] == "BinaryOperation":
                v,s = BinaryOperation.getBinaryOperationValue(exp)
                __emojiDict__[statement["identifier"]["value"]] = v
            else:
                __emojiDict__[statement["identifier"]["value"]] = exp["value"]



# sourceCode = """
# 😷=1
# 😖=2
# 😓=😷/(😷+(😷*😖*(😷+😖-(😷+😖+(😷+😖)))))
# 📇(😓)
# """

sourceCode = """
🥭🥭🥭=15
🥭=🥭🥭🥭/3
🍌🍌🍌🍌🍌🍌🍌🍌=13-🥭
🍌🍌🍌🍌=🍌🍌🍌🍌🍌🍌🍌🍌/2
🍌=🍌🍌🍌🍌/4
🍌🍌🍌=🍌*3
🥒🥒=8+🍌🍌🍌🍌
🥒=🥒🥒/2

📇(🥭)
📇(🥒)
📇(🍌)
📇(🥭+🍌🍌🍌+🥒)
"""
lexer = lex.lex()
lexer.input(sourceCode)
# for token in lexer:
#     print(token)
parser = yacc()
astJson = parser.parse(sourceCode)
json2ASObjectTree(astJson["value"])

# source="""
# a=1
# print(a)
# print(b)
# print(c)"""
# astree=ast.parse(source)
# pprint.pprint(ast.dump(astree))

# with open("source.py") as file:
#     for line in file:
#         lexer.input(line)

# string="abasd=112+(123+1231+(123+1231+(123+1231+(123+1231))))"
# ExpressionPattern="[A-Z_a-z\u4e00-\u9fa5][\u4e00-\u9fa5A-Z_a-z0-9]*=\d+\+\d+"
# print(re.match(ExpressionPattern,string))
