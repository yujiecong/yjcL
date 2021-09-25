import time
import traceback

from PySide2.QtCore import QObject, Signal, QThread
from PySide2.QtWidgets import QApplication, QWidget


class WorkThread(QObject):
    finished_Signal = Signal()
    started_Signal = Signal()

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.func = None
        self.threadResult = None
        self.errorInfo = None


    def setThreadFunc(self, func):
        self.func = func

    def start(self):
        # print("start WorkThread :",self.thread().currentThread())
        self.started_Signal.emit()

    def startThreadFunc(self):
        """

        @param args:
        @param kwargs:
        @return:
        """
        print("In WorkThread :", self.thread().currentThread())
        if callable(self.func):
            try:
                self.threadResult = self.func()
            except Exception:
                self.errorInfo = traceback.format_exc()
            finally:
                self.finished_Signal.emit()


def ahiodhaiso():
    print('asdasd')


app = QApplication()
print(app.thread().currentThread())
class adoasd(QWidget):

    startThread=Signal()
    def __init__(self):
        super(adoasd, self).__init__(None)
        print(self.thread().currentThread())
        self.thr = QThread()
        self.wt = WorkThread()
        # self.startThread.connect(self.thr.start)
        self.wt.moveToThread(self.thr)
        self.thr.started.connect(self.wt.startThreadFunc)
        self.thr.start()
        # self.startThread.emit()



        def finished():
            self.thr.quit()
            self.thr.wait()
            self.wt.deleteLater()
            self.thr.deleteLater()
        self.wt.finished_Signal.connect(finished)
        self.thr.start()
w=adoasd()
w.show()
app.exec_()
