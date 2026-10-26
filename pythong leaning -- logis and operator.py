
email = "m.r.lionman@hotmail.com"
phone = '043-221-843'
username = ''


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

Checking_info(email,phone,username)