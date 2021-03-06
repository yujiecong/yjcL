from ply import lex
from ply.yacc import yacc

lex.eof = False
reserved={
    "打印":"PRINT",
    "print": "PRINT",
    "出": "PRINT",
    "当":"WHILE",
    "while":"WHILE",
    "若":"IF",
    "if":"IF",
    "如果":"IF",
    "要是":"IF",
    "循环":"FOR",
    "遍历":"FOR",
    "for":"FOR",
    "in":"IN",

    "死循环":"FOREVER_LOOP",
    "foreverLoop":"FOREVER_LOOP",


}
tokens=[
    "IDENTIFIER",
    "STRING",
    "ASSIGNMENT",
    "NUMBER",
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "ENDMARKER",
    "LEFT_BRACKET",
    "RIGHT_BRACKET",
    "FLOAT",
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
    "GREAT_THAN",
    "LOWER_THAN",
    "GREAT_EQUAL",
    "LOWER_EQUAL",
    "EQUAL",
    "NOT_EQUAL"


]+list(set(reserved.values()))



t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'


t_GREAT_THAN=r">"
t_LOWER_THAN=r"<"
t_GREAT_EQUAL=r">="
t_LOWER_EQUAL=r"<="
t_EQUAL=r"=="
t_NOT_EQUAL=r"\!="



t_LEFT_BRACKET=r"\{"
t_RIGHT_BRACKET=r"\}"
t_ASSIGNMENT=r"="
t_LEFT_PAREN=r"\("
t_RIGHT_PAREN=r"\)"

# t_NEWLINE = r';'
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# A regular expression rule with some action code
def t_STRING(t):
    r'''("(\\\\"|\\\\\\\\|\\\\n|[^"])*")|('(\\\\'|\\\\\\\\|\\\\n|[^'])*')'''
    t.value = {
        "value":t.value[1:-1],
        "type":"NUMBER"
    }
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = {
        "value":float(t.value),
        "type":"FLOAT"
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
    r"[A-Z_a-z\u4e00-\u9fa5][\u4e00-\u9fa5A-Z_a-z0-9]*"

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




