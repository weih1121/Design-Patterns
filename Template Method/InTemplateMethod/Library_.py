import abc

class lib:
    def __init__(self):
        pass

    def Step1(self):            #稳定
        print("开车啦...！！！")

    def Step3(self):            #稳定
        print("嗯嗯，那走起了！！！")

    def Step5(self):            #稳定
        print("还来？再来就得猝死了...")
    
    @abc.abstractmethod
    def Step2(self):
        pass

    @abc.abstractmethod
    def Step4(self):
        pass
    

    def run(self):
        self.Step1()
        self.Step2()
        self.Step3()
        self.Step4()
        self.Step5()
