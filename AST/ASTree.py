import abc
import collections.abc


class ASTreeYJC(collections.abc.Iterable):
    @abc.abstractmethod
    def child(self,childIndex:int):
        pass

    @abc.abstractmethod
    def childrenNum(self) -> int:
        pass

    @abc.abstractmethod
    def children(self):
        pass

    @abc.abstractmethod
    def location(self)->str:
        pass

    @abc.abstractmethod
    def iterator(self):
        pass

    def toString(self):
        pass
