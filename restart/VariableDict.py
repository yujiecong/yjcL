import pprint


class VariableDict(dict):
    def __init__(self):
        super(VariableDict, self).__init__()

    def __setitem__(self, key, value):
        print("你赋值了一个屑变量 %s=%s"%(key,value))
        self.__dict__[key]=value

    def __getitem__(self, item):
        if item not in self.__dict__:
            raise KeyError("不存在的屑变量%s"%item)
        return self.__dict__[item]





    def pprint(self):
        pprint.pprint(self.__dict__)
    def __repr__(self):
        return repr(self.__dict__)
