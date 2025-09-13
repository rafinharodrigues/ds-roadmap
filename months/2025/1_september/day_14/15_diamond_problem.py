# Exercise: 15. Testar diamond problem e MRO

class A():
    def __init__(self):
        pass

    def action(self):
        print("A")

        
class B(A):
    def __init__(self):
        super().__init__()

    def action(self):
        print("D")


class C(A):
    def __init__(self):
        super().__init__()

    def action(self):
        print("C")


class D(A):
    def __init__(self):
        super().__init__()

    def action(self):
        print("D")


class E(B, C, D):
    def __init__(self):
        super().__init__()

    def action(self):
        print("E")


a = E()
print(a.action())