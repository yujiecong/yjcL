import pprint

from ply import lex
from ply.yacc import yacc

lex.eof = False

reserved={
    "📇":"PRINT",
}
tokens=[
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

]+list(set(reserved.values()))


#加减乘除 对应 喜怒哀乐
t_PLUS    = r'😀'
t_MINUS   = r'😡'
t_TIMES   = r'😭'
t_DIVIDE  = r'😁'

t_EQUAL=r"="
t_LEFT_PAREN=r"\("
t_RIGHT_PAREN=r"\)"

# t_NEWLINE = r';'
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# A regular expression rule with some action code
def t_STRING(t):
    r"""("(\\\\"|\\\\\\\\|\\\\n|[^"])*")|('(\\\\'|\\\\\\\\|\\\\n|[^'])*')"""
    t.value = {
        "value":t.value[1:-1],
        "type":"STRING"
    }
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = {
        "value":int(t.value),
        "type":"NUMBER"
    }
    return t

def t_IDENTIFIER(t):
    r"[\U0001F300-\U0001F64F\U0001F680-\U0001F6FF\u2600-\u2B55]+"
    type_=reserved.get(t.value, 'IDENTIFIER')
    t.value = {
        "value":t.value,
        "type":type_
    }  # Check for reserved words
    t.type=type_

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
    print("屑字符 '%s'" % t.value[0])
    t.lexer.skip(1)



from lexer import *


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)
def p_sourcecode(p):
    """SourceCode : ENDMARKER
                  | FileContent ENDMARKER"""

    if len(p)==3:
        p[0] = {
            "type": "SourceCode",
            "value": p[1]
        }
    else:
        p[0]={
            "type":"SourceCode",
            "value":[]
        }

def p_FileContent(p):
    '''FileContent : FileContent Statement
            | Statement
            | empty'''
    if len(p)==3:
        p[1]["value"].append(p[2])
        p[0]=p[1]
    else:
        p[0]={
            "type":"FileContent",
            "value":[p[1]]
        }


def p_empty(p):
    'empty :'
    p[0]=None

def p_statement(p):
    """Statement : Assignment
                | PrintSomething
                | Expression"""

    p[0]=p[1]


    # print("Statement",p[0])
def p_assignment(p):
    "Assignment : IDENTIFIER EQUAL Expression"
    idDict = p[1]
    exprDict = p[3]
    p[0] = {
        "identifier": idDict,
        "expression":exprDict,
        "type": "Assignment"
    }



def p_binary_opeartion(p):
    """ Expression : Expression PLUS Expression
                | Expression MINUS Expression
                | Expression TIMES Expression
                | Expression DIVIDE Expression"""
    valueDict={}
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

    if len(p)==2:
        valueDict=p[1]
        p[0] = valueDict

    elif len(p)==4:
        if p[1]=="(":
            p[0]=p[2]


def p_expr_uminus(p):
    'Expression : MINUS Expression %prec UMINUS'
    p[2]["value"]=-p[2]["value"]
    p[0] = p[2]


def p_print_Identifier(p):
    """
    PrintSomething : PRINT LEFT_PAREN Expression RIGHT_PAREN
    """
    valueDict=p[3]

    p[0]={
        "value":valueDict,
        'type':"PrintSomething",
        "print_key":p[1]
    }


def p_error(p):
    if p:
        print('屑 {}'.format(p))

__dict__={}
def json2ASObjectTree(ast,objs):
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
        if statementType == "PrintSomething":
            print(statement)
        elif statementType == "Assignment":
            __dict__[statement["identifier"]]=statement["expression"]
        objs.append(statementObject)
    return objs

sourceCode="""
😑😶😏=1
📇(😑😶😏)
"""
lexer = lex.lex()
# lexer.input(sourceCode)
parser = yacc()
astJson = parser.parse(sourceCode)
pprint.pprint(astJson)


