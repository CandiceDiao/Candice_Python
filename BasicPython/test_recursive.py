"""
递归函数
"""

class TestRecursive:

    def recursive(self,num):
        print(num)
        if num ==1:
            return
        self.recursive(num-1)
        print("comlplete %d"%num)

    def test_recursive(self):
        self.recursive(3)

