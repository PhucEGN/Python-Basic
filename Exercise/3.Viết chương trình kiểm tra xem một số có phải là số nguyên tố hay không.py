# nhập 1 số vào
# chia số đó cho các số từ 1 đến chính nó 
# nếu trong quá trình chia != 1 và chính nó mà có số nguyên thì loại

number = int(input("Nhập một số bất kì:"))

def Tim_So_Nguyen_To():
    global number
    
    for i in range(2,number-1):
        if(number % i == 0):
            return print("Đây là một số nguyên")
    print("Đây là một số nguyên tố")


Tim_So_Nguyen_To()
