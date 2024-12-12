"""
Fixing for Diamond problem
"""
class A:
    def say_hello(self):
        print("Hello from A")

class B(A):
    def say_hello(self):
        print("Hello from B")
        super().say_hello() #In this case it'll call the siblings method

class C(A):
    def say_hello(self):
        print("Hello from C")
        super().say_hello() #It'll call the parents method

class D(B, C):
    def say_hello(self):
        print("Hello from D")
        super().say_hello()  # Call method from the parent class in the Method Resolution Order

d = D()
d.say_hello()
