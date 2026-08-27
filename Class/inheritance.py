# Inheritance in Python
# defn:-  The Machanism of Deriving a new class from an old one is called inheritance.
# 1) Single Inheritance
'''
class A:
    def m1(self):
        print("Parents")

class B(A):
    def m2(self):
        print("Child")

k = B()
k.m1()
k.m2()
'''

# 2) Multilevel inheritance
'''
class A:
    def m1(self):
        print("Grand Parents")

class B(A):
    def m2(self):
        print("Parent")

class C(B):
    def m3(self):
        print("Chaild")

k = C()
k.m1()
k.m2()
k.m3()
'''
# 3) Multple Inheritance:
'''
class A:
    def m1(self):
        print("Grand Parents")

class B:
    def m2(self):
        print("Parent")

class C(A,B):
    def m3(self):
        print("Chaild")

k = C()
k.m1()
k.m2()
k.m3()

'''
# 4) Hybrid Inheritance
'''
class A:
    def m1(self):
        print("Grand Parent")

class B(A):
    def m2(self):
        print("Parent 1")

class D:
    def m4(self):
        print("Parent 2")

class C(B,D):
    def m3(self):
        print("Chaild")

k = C()
k.m1()
k.m2()
k.m4()
k.m3()
'''

# 5) Hirarchi
class A:
    def m1(self):
        print("Parent 1")
        
class B(A):
    def m2(self):
        print("Chiled 1")

class C(A):
    def m3(self):
        print("Chiled 2")



k = B()
k.m1()
k.m2()

k1 = C()
k1.m1()
k1.m3()
