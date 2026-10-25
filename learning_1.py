import math
import random

#=========== varible


AA = [3.789456123,4.123456789,123.456123789]
BB = (45.666666,37.99999,67.99999)

#=========== decimal, isinstance(ตัวที่ต้องการให้ตรวจ , ขนิดที่กำหนด) เช็ตชนิด

def rounding_1 (X):
    if isinstance(X,list) : 
        CD = [round(i,2) for i in X]
        print(CD)
    else :
        print(f'The varible is not list')

#rounding_1(BB)


#=========== random, randint(เริ่มต้น,จบ) for integer, uniform(เริ่มต้น,จบ) for float

def random_1 (X):
    if isinstance(X,tuple) :
      Random_Listing = [random.uniform(1,5) for i in X]
      print(Random_Listing)
    else :
        print(f'The varible is not list')

#random_1 (BB)


#========== is_integer  วัดเเค่ว่าค่า value ลงตัวหรอมีเศษ

def is_integer_test (X) :
    if all(i.is_integer() for i in X) :
        print('YEAH?!!!!!')
    elif any(i.is_integer() for i in X):
        print('Some is YEAH')
    else:
        print('NONE!!!!')

#is_integer_test(AA)

#========= random number and find it is even or not. / หา range จาก len  for i in range(len(X))
#========= ตัวอย่าง if ก่อน for[0 if i % 2 == 1 else 1 for i in AA] [ค่าถ้าจริง if เงื่อนไข else ค่าถ้าเท็จ for i in AA]
#========= ตัวอย่าง for ก่อน if [i for i in AA if i % 2 == 0] [ค่าถ้าจริง for ตัวแปร in ลำดับ if เงื่อนไข]


def random_even_check (X) :
    if isinstance(X,list) :
        AA = [random.randint(1,100) for i in X]
        CC = [555 if i % 2 == 1 else 666 for i in AA]
        DD = ['คู่' if i == 555 else 'คี่' for i in CC]
        print(f'The first number is {AA} \n testing even for check {CC} \n Reuslt {DD}')
    else :
        AA =tuple([random.randint(1,100) for i in range(len(X))])
        print(f'Tuple number is {AA}')

random_even_check(AA)