from collections import Iterable
'''迭代
Python内置的enumerate函数可以把一个list变成索引-元素对
'''


def compare(numbers):
    max = int(numbers[0])
    min = int(numbers[0])
    for n, value in enumerate(number):
        if value < min :
            min = value
        elif value > max :
            max = value
    return max,min
number = [45,23,54,124,243,22,35]
compare(number)

#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

isinstance('abc', Iterable) # str可迭代 
isinstance([1,2,3], Iterable) # list可迭代
isinstance(123, Iterable) # 整数不可迭代

# 测试
if compare([]) != (None, None):  #空未做控制
    print('测试失败!')
elif compare([7]) != (7, 7):
    print('测试失败!')
elif compare([7, 1]) != (1, 7):
    print('测试失败!')
elif compare([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')



