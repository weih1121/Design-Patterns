class Singlaton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == '__main__':
    a = Singlaton('a')
    b = Singlaton('b')
    print(id(a))
    print(id(b))

     