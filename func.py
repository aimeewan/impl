'''
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None。
函数可以同时返回多个值，但其实就是一个tuple。
***定义默认参数要牢记一点：默认参数必须指向不变对象！
参数：必选参数、默认参数、可变参数、关键字参数和命名关键字参数
'''

def add(numbers):
    sum = 0
    n = 1
    for number in range(numbers):
        sum = sum + number
        if(n <= numbers):
            n = n +1
    return sum

add(101)