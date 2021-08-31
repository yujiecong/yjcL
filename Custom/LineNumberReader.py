
class LineNumberReader:
    def __init__(self,text):
        self.text = text
        self.lineNumber=1
        self.textSpilted=self.text.split("\n")
        self.lineGenerator=self.readLine()
    def readLine(self):

        for text in self.textSpilted:
            if text:
                yield text

                self.lineNumber += 1

    def getLineNumber(self):
        return self.lineNumber
