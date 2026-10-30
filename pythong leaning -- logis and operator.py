import math
import random


email = "m.r.lionman@hotmail.com"
phone = '043-221-843'
username = ''
AX1 = 'Dog'
AX2 = 'Cat'
AX3 = 'Door'
Alphabet_ENG = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
                ,'u','v','w','x','y','z')



#============== any() / all() / isinstance(object, classinfo) ตรวจ type เช่น  isinstance(XXXX, list) 
#======== bool(1)        # True
# bool("hello")  True
# bool([1, 2])   True
# ----------------
# bool(0)        False
# bool("")       False
# bool([])       False
# bool(None)     False

#print(any([username, phone, username]))
#print(all([username, phone, username]))

#========================
#ควรระวีง if มาครอบ for  จะต้องคิดว่ามันคือการทำงานทีละขั้น if มันอ่านทีละ condition 
# ถ้ามีเงื่อนไขที่ไม่ครอบไว้มันจะเหมือนเราเอา true false หลายๆตัวมาใน condition เดียวมัน 
#เเก้ด้วยการใช้ all() / any()  ครอบไว้เเละบอก condition ไปเลยว่าจะ T or F ซึ่งตรวจเเค่ครั้งเดียว

def Checking_info (X,Y,Z):
    AA = [X,Y,Z]
    if all(isinstance(i,str) for i in AA) :
        for s in AA :
            if bool(s) :
                print(f'true')
            else :
                print(f'false')
                
    else:
        print('Only work with string')

#Checking_info(email,phone,username)


#======================== xxx.endswith('y'), xxx.startswith('y') 
#string.startswith(prefix, start, end) / str.endswith(suffix, start, end)
# collection.append(element)



#++++++++  .append() / .remove() เเละอื่นๆ

# list     [ ]	ได้	       .append(x) เพิ่มท้ายลิสต์
# set      { }	ไม่ได้	    .add(x)
# dict     {k: v}	ไม่ได้	    d[key] = value หรือ .update()
# tuple    ( )	ไม่ได้     (แก้ไขไม่ได้)	สร้าง tuple ใหม่ เช่น t + (x,)
# str      " "	ไม่ได้     (แก้ไขไม่ได้)	ต่อสตริงด้วย s + "x"


# a = ['Dog', 'Door', 'Cat', 'Dog']

# a.remove('Dog')   # ลบตัวแรกที่เจอตามค่า -> ['Door', 'Cat', 'Dog']
# a.pop()           # ลบตัวสุดท้าย และคืนค่าที่ลบออกมา
# a.pop(0)          # ลบตามตำแหน่ง (index) ที่ 0
# del a[1]          # ลบตามตำแหน่ง (index) ที่ 1
# a.clear()         # ลบทั้งหมด -> []

# set	       .remove(x)  (ถ้าไม่มีค่าจะ error) หรือ .discard(x) (ถ้าไม่มีค่าก็ไม่ error)
# dict	   del d[key] หรือ d.pop(key)
# tuple / str	   ลบไม่ได้ เพราะแก้ไขไม่ได้ ต้องสร้างใหม่ เช่น s.replace('a', '')


def S_check (Z,Y,X) :
    DD = [Z,Y,X]
    CC = []
    FF = []
    for i in DD :
        if i.startswith('D') :
            CC.append(i)
            
        else :
            FF.append(i)
    print(f'the value of CC is {CC} \n the value of FF is {FF}')

    
#S_check(AX1,AX2,AX3)


#=======================
# while i < 3 :
# i+=1
# operator ดูใน ภาพตัวอย่าง

def Equal_checking () :
    HH=[]
    GG=[]
    i = 0 
    while i < 10 :
        DD = [random.randint(1,10)]
        for d in DD :
            PP = d % 2
            if PP == 0 :
                HH.append(DD[0])
            else :
                GG.append(DD[0])
        i +=1

    print(f'The even values are {HH} \n The odd value are {GG}')

#Equal_checking()


#==================

def Randint_Path () :
    UU = random.randint(4,12)
    YY = random.randint(0,25)
    FF = []
    OO = []
    YY = []
    UP = []
    i = 0
    while i < 13 :
        TT = random.randint(0,25)
        if TT <= UU :
        
            FF.append(TT)
            YY.append(Alphabet_ENG[TT])

            #GG = [x % 2  for x in (FF)]
        else :
            OO.append(TT)
            UP.append(Alphabet_ENG[TT])
        i += 1
    IO = len(FF)
    print(IO)
    #print(f'The Alpha Group are {FF} \n \twhich translate to {YY} \n The Beta groups are {OO} \n \twhich traslate to {UP}')

# str.split(sep, maxsplit)  ตัวอย่าง s.split(",", 2) >> ['a', 'b', 'c,d,e'] เเบ่งด้วย "," เเละทำเเค่ 2 ตัว


Randint_Path()

