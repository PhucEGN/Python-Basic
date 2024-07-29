List = str(input("nhập danh sách các số được ngăn cách bởi dấu cách: "))
List = List.split(" ")
List = list({int(i) for i in List})
a = 0

def Tim_So_Lon_Nhat():
    global List
    global a
    for i in range(len(List)):
        if(List[a] < List[i]):
            a = a + 1
            return Tim_So_Lon_Nhat()
    print("số lớn nhất:", List[a])
    List.remove(List[a]) 
    a = 0
    return Tim_So_Lon_Thu_Hai()

def Tim_So_Lon_Thu_Hai():
    global a
    global List
    for i in range(len(List)):
        if(List[a] < List[i]):
            a = a + 1
            return Tim_So_Lon_Thu_Hai()
    print("số lớn thứ hai:", List[a])
    
Tim_So_Lon_Nhat()
