import enum

class Tax_Base(enum.Enum):   #定义一个枚举类型
    CN_Tax = 0
    US_Tax = 1
    DE_Tex = 2

# Tax_Base = enum.Enum("CountryTax", ('CN_Tax', 'US_Tax', 'DE_Tex')) #定义一个枚举类型

class SalesOrder:
    def __init__(self, CountryNum):
        self.tex  = CountryNum

    def CalculateTex(self):
        if(self.tex == Tax_Base.CN_Tax):
            print('CN_Tax', 15)
        elif(self.tex == Tax_Base.US_Tax):
            print('US_Tax', 25)
        elif(self.tex == Tax_Base.DE_Tex):
            print('DE_Tax', 35)

so = SalesOrder(Tax_Base.CN_Tax)
so.CalculateTex()

# print(Tax_Base.CN_Tax)          #打印索引名
# print(Tax_Base.CN_Tax.value)    #打印索引值

#这种模式的代码看起来貌似没问题，但是一旦需要新增很多国家时，
#将会大量修改程序源代码，包括枚举类型和CalculateTex()函数
#破坏了开放封闭原则
#如果将全球的国家都加入进去，if else将会变得可读性很差
#而且可能会占用内存空间过大，导致整个程序不能在处理器高速缓冲区
#执行代码，降低效率
