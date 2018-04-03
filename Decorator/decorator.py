class foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")

class foo_decorator(object):
    def __init__(self, decora):
        self._decora = decora

    def f1(self):
        print("decorated f1()")
        self._decora.f1()

    def __getattr__(self, name):
        return getattr(self._decora, name)

u = foo()
v = foo_decorator(u)
print(v.f1())
print(v.f2())