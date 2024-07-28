# a là biến toàn cục nhưng khi khai báo biến a trong hàm Func() thì a sẽ là biến cục bộ 
a = "Tạm biệt"
def Func():
    a = "Xin chào" 
    print(a)
Func()
print(a)