'''
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None。
函数可以同时返回多个值，但其实就是一个tuple。
***定义默认参数要牢记一点：默认参数必须指向不变对象！如果是可变对象，程序运行时会有逻辑错误
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

'''可变参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
'''
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum

nums = [1,2,3,4,5]
calc(*nums)

'''关键字参数
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
def register(name,age,**kw):
    print("name is :",name," age is :",age ,"other's :",kw)

register('name',45,gen='M')

extr = {'city':'Beijing','job':'tester'}
register('极光',35,city=extr['city'],job=extr['job'])
register('极光',35,**extr)

'''命名关键字参数
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
参数的顺序可以变换，但是关键字一定要正确，如果关键字对应不上，程序运行会报错
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
'''
def person(name,age,*,city,job):
    print(name,age,city,job)
person('zhangsheng',35,city='shanghai',job='tester')

'''如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了'''
def pepeole(name,age,*args,city,job):
    print(name,age,args,city,job)
pepeole('qingtian',25,[1,2,3],city='shanghai',job='engeene')

'''参数组合
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
'''


'''对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
'''
def product(x,y):
    return x * y

product(4,5)

def producttest(*args):
    cal = 1
    for n in args:
        cal = cal * n
    return cal

producttest(5,6,7,9)