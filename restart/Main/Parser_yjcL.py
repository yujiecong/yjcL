
from Lexer_yjcL import *
from restart.Enum.Enum import StatementType

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
            | Statement'''
    if len(p)==3:
        p[1]["value"].append(p[2])
        p[0]=p[1]
    else:
        p[0]={
            "type":"FileContent",
            "value":[p[1]]
        }

def p_statement(p):
    """Statement : Assignment
                | PrintSomething
                | Something_Conditional
                | Expression"""

    p[0]=p[1]


    # print("Statement",p[0])
def p_assignment(p):
    "Assignment : IDENTIFIER EQUAL Expression"
    idDict = p[1]
    exprDict = p[3]
    p[0] = {
        "value": (idDict["value"],exprDict["value"]),
        "type": "Assignment"
    }

def p_conditional_expression(p):
    """Something_Conditional : IF Expression  LEFT_BRACKET FileContent RIGHT_BRACKET
                    | WHILE Expression  LEFT_BRACKET FileContent RIGHT_BRACKET
                    """


    condition=p[1]

    p[0] = {
        "type": StatementType.Something_Conditional,
        "value": p[4],
        "condition_type":condition,
        "condition_judge":p[2]
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

    # op=p[2]
    # if op=="+":
    #     valueDict["result"]=p[1]+p[3]
    # if op=="-":
    #     valueDict["result"]=p[1]-p[3]
    # if op == "*":
    #     valueDict["result"] = p[1] * p[3]
    # if op=="/":
    #     valueDict["result"]=p[1]/p[3]

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
    print('屑 {}'.format(p))

