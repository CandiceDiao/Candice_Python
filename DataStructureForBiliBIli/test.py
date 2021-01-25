class A:
    def __init__(self,name,age):
        self.name = name
        self.__age = age


class B(A):
    def print_private(self):
        print(self.name)

b= B("zhangsan",10)
b.print_private()
