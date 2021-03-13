# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:52:50 2020

@author: USER
"""

number = 10
day = "three"
"I ate %d apples" %number


"I ate {0} apples. So I was sick for {1} days".format(number, day)

"{0:<10}".format("hi")

add = lambda a, b : a+b
result = add(3,4)
print(result)


number = input("숫자를 입력하세요: ")
print("입력한 숫자 : ", number)

with open("foo.txt", "w") as f:
    f.write("Lite is too short, you need python")
    
    
    
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
type(a)

a.setdata(4, 2)

print(a.add())


class OneCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    
class MoreCal(OneCal):
    pass

a = MoreCal(4,2)
a.add()


