"""
Implementation for Diamond problem
"""
class A:
    def say_hello(self):
        print("Hello from A")

class B(A):
    def say_hello(self):
        print("Hello from B")

class C(A):
    def say_hello(self):
        print("Hello from C")

# Method D inherits from both B and C
class D(B, C):
    pass

d = D()
d.say_hello()  # We don't know do it use B's or C's method
