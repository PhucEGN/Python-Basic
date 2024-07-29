# nhập một số bất kì và in nó ra // write any number and print it.
def Exercise_1():
    a = input("nhập một số bất kì: ")
    print("số của bạn là: ", a)

# nhập một số bất kì và kiểm tra xem nó là số chẵn hay lẻ // write any number and check if this number is even or odd.
def Exercise_2():
    a = int(input("nhập một số bất kì: "))

    if(a % 2 == 0):
        print("số ",a," là số chẵn")
    if(a % 2 == 1):
        print("số",a,"là số lẻ")

# viết chương trình tính tổng 2 số // write a program to sum two numbers
def Exercise_3():
    a = int(input("nhập số thứ nhất: "))
    b = int(input("nhập số thứ hai: "))

    print("kết quả a + b =",a+b)
    
# chuyển đổi độ C sang độ F tùy theo yêu cầu của người dùng // Convert Celcius to Fahrenheit based on person's request
def Exercise_4():
    print("1. Chuyển độ C sang độ F")
    print("2. Chuyển độ F sang độ C")
    a = int(input("vui lòng chọn 1 hoặc 2:"))
    Temp = float(input("vui lòng nhập nhiệt độ cần chuyển đổi:"))
    
    if(a == 1):
        calc = (Temp * 1.8) + 32
        print("Giá trị chuyển đổi từ độ C sang độ F là:", calc)
    if(a == 2):
        calc = (Temp - 32) * 0.555555
        print("Giá trị chuyển đổi từ độ C sang độ F là:", calc)
           
Exercise_4()