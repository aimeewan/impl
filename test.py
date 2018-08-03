import os
import math

print ('Hello Python')

True or False

True and False

'''list是有序集合'''
classmates=['Kate','Jack','Mickle']
print(classmates)
len(classmates)

'''索引下标-1表示取最后一个元素，以此类推，-2倒数第二，-3倒数第三'''
classmates[-1]

'''元组'''
classmates1=('a','b','c')
classmates1

'''练习'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
L[0][0]
L[1][1]
L[2][2]

age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

s = input("birth is:")
birth = int(s)
if birth<20000:
    print("00前")
else :
    print("00后")

'''25-28：过重 28-32：肥胖  高于32：严重肥胖'''

height=200
high=1.8
BMI=height/(manth.pow(high)) '''平方函数'''

print(BMI)
if BMI<18.5:
    print("过轻")
elif BMI>=18.5 & BMI<25:
    print("正常")
elif BMI>=25 & BMI<28:
    print("过重")

'''tuple：
1.有序集合
2.长度不可变
'''

'''list：
1.有序集合
2.长度可变
3.查找和插入的时间随着元素的增加而增加；
4.占用空间小，浪费内存很少。
'''

'''dict：
1.使用键-值（key-value）存储，具有极快的查找速度
2.查找和插入的速度极快，不会随着key的增加而变慢；
3.需要占用大量的内存，内存浪费多。
'''
'''set
1.和dict类似，是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
2.自动过滤重复数据
3.无序
'''
'''str是不可变对象，对于可变对象，比如list，对list进行操作，list内部的内容是会变化的'''

a = {'a':(1,2,3)}
print(a['a'])

b = set((1,2,3))
print(b)

c = {'a':(1,2,[3,4])}
print(c['a'])

d = set((1,2,3))
print(b)

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
        if(n <= number):
            n = n +1
    return sum

add(10)