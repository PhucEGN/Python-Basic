number = int(input("Nhập giới hạn cần kiểm tra các số nguyên tố: "))
String = ""
for i in range(2,number):
    flag = True
    for x in range(2,i):
        if(i % x == 0):
            flag = False
            break
    if flag:
        String = String + str(i) + " " 
print("Dãy các số nguyên tố là:", String)