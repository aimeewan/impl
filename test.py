import os
import numpy

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

'''练习‘’‘
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

height=56
high=1.8
BMI=height/(numpy.square(high))
print(BMI)
if BMI<18.5:
    print("过轻")
elif BMI>=18.5 & BMI<25:
    print("正常")