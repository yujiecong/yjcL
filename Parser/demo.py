# -*- coding: utf-8 -*-
import ast

import logging

from ply.yacc import yacc
from ply.lex import lex

logger = logging.getLogger()

reserved = {
    'and': 'AND',
    'or': 'OR',
    'None': 'NONE',
    '>': 'GT',
    '<': 'LT',
    '>=': 'GE',
    '<=': 'LE',
    '!=': 'NE',
    'in': 'IN',
    'not': 'NOT',
    '==': 'IE'
}

# Token list
tokens = ['NUMBER', 'LIST', 'FLOAT', 'STR','PLUS', 'MINUS', 'TIMES', 'DIVIDE','LPAREN', 'RPAREN', 'ID'] + list(reserved.values())

def MyLexer():
     # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_GE = r'\>\='
    t_LE = r'\<\='
    t_GT = r'\>'
    t_IE = r'\=\='
    t_LT = r'\<'
    t_STR = r"""\".*?\"|\'.*?\'"""
    t_NE = r'\!\='

    def t_LIST(t):
        r'\[.*\]'
        t.value = ast.literal_eval(t.value)
        return t

    def t_FLOAT(t):
        r'\d+\.+\d+'
        t.value = float(t.value)
        return t

    # A regular expression rule with some action code
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # 单独为保留字写的匹配规则
    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z]*'
        t.type = reserved.get(t.value, 'ID')    # Check for reserved words
        return t


    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

     # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

     # Error handling rule
    def t_error(t):
        logger.error("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer from my environment and return it
    return lex()

precedence = (
    ('left', 'AND', 'OR'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),  # - 作为单目运算符, 这里的优先级是虚的
    ('left', 'LPAREN', 'RPAREN')
)

# 越基本越往下写
def p_expr(p):
    '''
        expr : expr PLUS expr
             | expr MINUS expr
             | expr TIMES expr
             | expr DIVIDE expr
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_compare(p):
    '''
        expr : expr GT expr
             | expr GE expr
             | expr IE expr
             | expr LE expr
             | expr LT expr
             | expr NE expr
    '''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == "!=":
        p[0] = p[1] != p[3]

def p_logic(p):
    '''
        expr : expr OR expr
             | expr AND expr
             | NOT expr
             | expr IN expr
    '''
    if p[2] == "or":
        p[0] = p[1] or p[3]
    elif p[2] == "and":
        p[0] = p[1] and p[3]
    elif p[1] == 'not':
        p[0] = not p[2]
    elif p[2] == 'in':
        p[0] = p[1] in p[3]
    print(list(p))

def p_expr_list(p):
    '''
        expr : list
    '''
    p[0] = p[1]


def p_list(p):
    '''
        list : LIST
    '''
    p[0] = p[1]

def p_expr_num(p):
    '''
        expr : num
    '''
    p[0] = p[1]


def p_num(p):
    '''
        num : NUMBER
    '''
    p[0] = p[1]

def p_expr_float(p):
    '''
        expr : float
    '''
    p[0] = p[1]


def p_float(p):
    '''
        float : FLOAT
    '''
    p[0] = p[1]


def p_expr_str(p):
    '''
        expr : str
    '''
    p[0] = p[1]


def p_str(p):
    '''
        str : STR
    '''
    p[0] = ast.literal_eval(p[1])

def p_expr_none(p):
    '''
        expr : none
    '''
    p[0] = p[1]

def p_none(p):
    '''
        none : NONE
    '''
    p[0] = ast.literal_eval(p[1])

def p_group(p):
    '''
        expr : LPAREN expr RPAREN
    '''
    p[0] = p[2]

def p_expr_uminus(p):
    '''
        expr : MINUS expr %prec UMINUS
    '''
    p[0] = -p[2]

def p_error(p):
    logger.error('Syntax error:{}'.format(p))

lexer = MyLexer()
parser = yacc()

if __name__ == "__main__":
    while True:

        a_string = input("输入：")

        print(a_string)
        lexer.input(a_string)
        for i,l in enumerate(lexer):
            print(str(i+1) + "=>", l)
        print(parser.parse(a_string))