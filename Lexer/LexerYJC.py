import re
import typing

from Custom.LineNumberReader import LineNumberReader
from Exceptions.Parse import YjcParseError
from Token.TokenYJC import TokenYJC, IdentifierTokenYJC, NumTokenYJC, StrTokenYJC


class LexerYJC:
    IntegerLiteral = "[0-9]+"
    IdentifierLiteral = "[A-Z_a-z][A-Z_a-z0-9]*|==|<=|>=|&&|\\|\\||\S"
    StringLiteral='"(\\\\"|\\\\\\\\|\\\\n|[^"])*"'
    CommentLiteral="//.*"
    regexPattern =  f"\s*(({CommentLiteral})|({IntegerLiteral})|({StringLiteral})|{IdentifierLiteral})?"
    "在java 的 group 中 0 代表整个串串"
    EntireFlag=0
    "第一个括号里的东西 是空格*个空格 即\\s代表的"
    SpaceFlag=1
    CommentFlag=2
    NumFlag=3
    StrFlag = 4
    IdentifierFlag = 5


    def __init__(self):
        self.patternCompiled=re.compile(self.regexPattern)
        self.queue:typing.List[TokenYJC]
        self.queue=[]
        self.hasMore:bool
        self.hasMore=True

    def setRawString(self,rawString):
        self.reader = LineNumberReader(rawString)

    def read(self):
        if self.fillQueue(0):
            token=self.queue.pop(0)
            return token
        else:
            return TokenYJC.EOF
    def peek(self,i):

        if self.fillQueue(i):
            return self.queue[i]
        else:
            return False


    def fillQueue(self,i:int):
        while i>=len(self.queue):
            if self.hasMore:
                self.readLine()
            else:
                return False
        else:
            return True


    def readLine(self):
        try:
            try:
                line=next(self.reader.lineGenerator)
            except StopIteration:
                line=None

        except IOError as e:
            raise YjcParseError(e.__str__())
        else:
            if line==None:
                self.hasMore=False
                return
            lineNo=self.reader.getLineNumber()
            pos=0
            endPos=len(line)
            tempLine=line[:]
            while pos<endPos:
                matcher = self.patternCompiled.match(tempLine)
                if matcher:
                    self.addToken(lineNo,matcher)
                    pos=matcher.end()+pos
                    tempLine=line[pos:endPos]
                else:
                    raise YjcParseError("Bad Token at line %s"%lineNo)
            self.queue.append(IdentifierTokenYJC(lineNo, TokenYJC.EOL))


    def addToken(self,lineNo:int,matcher:typing.Match):

        matchedOne=matcher.group(self.SpaceFlag)

        if matchedOne:
            if not matcher.group(self.CommentFlag):#如果不是注释
                token_:TokenYJC
                if matcher.group(self.NumFlag):
                    token_=NumTokenYJC(lineNo, int(matchedOne))
                elif matcher.group(self.StrFlag):
                    token_=StrTokenYJC(lineNo, self.toStringLiteral(matchedOne))
                else:
                    token_=IdentifierTokenYJC(lineNo, matchedOne)
                self.queue.append(token_)
    def toStringLiteral(self, matchedString:typing.AnyStr):
        """

        :param matchedString:
        :return:
        """

        stringLength=len(matchedString)
        strPointer=1
        stringBuilder=""
        while strPointer<stringLength:
            singleStr=matchedString[strPointer]
            if singleStr=="\\" and strPointer+1<stringLength:
                singleStrNext=matchedString[strPointer + 1]
                if singleStrNext=='"' or singleStrNext=="\\":
                    strPointer+=1
                    singleStr=matchedString[strPointer]
                elif singleStrNext=="n":
                    strPointer+=1
                    singleStr="\n"

            stringBuilder+=singleStr

        return stringBuilder


