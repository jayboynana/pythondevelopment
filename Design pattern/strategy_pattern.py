from abc import abstractmethod,ABCMeta

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def doOperation(self,inNum1,inNum2):
        pass

class OperationAdd(Strategy):
    def doOperation(self,inNum1,inNum2):
        return inNum1 + inNum2

class OperationSubtract(Strategy):
    def doOperation(self,inNum1,inNum2):
        return inNum1 - inNum2

class OperationMultiply(Strategy):
    def doOperation(self,inNum1,inNum2):
        return inNum1 * inNum2

class OperationDivide(Strategy):
    def doOperation(self,inNum1,inNum2):
        return inNum1 / inNum2

class Context():
    _strategy = None
    def __init__(self,inStrategy):
        self._strategy = inStrategy
    def executeStrategy(self,inNum1,inNum2):
        return self._strategy.doOperation(inNum1,inNum2)

if __name__ == '__main__':
    aContext = Context(OperationAdd())
    print("10 + 5 = {0}".format(aContext.executeStrategy(10,5)))
    print(f"执行{[name for name in dir(aContext) if not name.startswith('__') and not name.startswith('_')]}")
    aContext = Context(OperationSubtract())
    print("10 - 5 = {0}".format(aContext.executeStrategy(10, 5)))
    aContext = Context(OperationMultiply())
    print("10 * 5 = {0}".format(aContext.executeStrategy(10, 5)))
    aContext = Context(OperationDivide())
    print("10 / 5 = {0}".format(aContext.executeStrategy(10, 5)))
