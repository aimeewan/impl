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

'''
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

'''递归函数
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
递归函数的优点是定义简单，逻辑清晰
!!!!使用递归函数需要注意防止栈溢出,由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出,解决递归调用栈溢出的方法是通过尾递归优化
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
'''
def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

fact(5)

