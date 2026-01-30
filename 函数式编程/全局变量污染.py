
#需求：实现变量a自增
#通过局部变量，不能实现递增


a = 10
def add():
    global a
    a +=1
    print("a:",a)

def print_ten():
    if a==10:
        print("ten!!!")
    else:
        print("全局变量a，不等于10")


add()
add()
add()
print_ten()