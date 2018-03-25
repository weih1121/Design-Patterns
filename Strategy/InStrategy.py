import abc          #导入抽象类包


class TaxStrategy:
    def __init__(self):
        pass

    @abc.abstractmethod
    def Calculate(self):
        pass

class CN(TaxStrategy):

    def Calculate(self):
        print('CN_TAX', 15)

class US(TaxStrategy):

    def Calculate(self):
        print('US_TAX', 178785)

class DE(TaxStrategy):

    def Calculate(self):
        print('DE_TAX', 101235)       

class SalesOrder:
    def __init__(self):
        self.ts = TaxStrategy()

    def CalculateTex(self, tax):
        self.ts = tax
        self.ts.Calculate()



cn = CN()
us = US()
so = SalesOrder()
so.CalculateTex(us)
