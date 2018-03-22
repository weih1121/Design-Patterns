from Library import lib
import random

class App:
    def __init__(self):
        pass

    def Step2(self):
        if random.randint(0, 9) % 10 < 5:
            print("开车？ 来！笑脸")
        else:
            print("开车？不开，你的操作令人窒息！呕吐,但是勉强...")

    def Step4(self):
        if random.randint(0, 9) % 10 < 5:
            print("输的好惨，还继续吗？")
        else:
            print("赢了一点点，要不要挑战一百连胜？")
            
    def run(self):
        lib_method = lib()

        lib_method.Step1()
        self.Step2()
        lib_method.Step3()
        self.Step4()
        lib_method.Step5()

if __name__ == '__main__':
    app = App()
    app.run()

        
        