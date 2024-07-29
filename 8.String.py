Str = "This is a String"

print("Example 1:")
# lấy ra 1 kí tự trong chuỗi // get character at position 6
print(Str[6])

print("Example 2:")
# lấy ra các kí tự trong Str
for x in Str:
    print(x)

print("Example 3:")
# lấy ra độ dài trong Str
print(len(Str))

print("Example 4:")
# cắt chuỗi // cutting strings
print(Str[0:4])

print("Example 5:")
# viết hoa toàn bộ kí tự
print(Str.upper())

print("Example 6:")
# viết thường toàn bộ kí tự
print(Str.lower())

print("Example 7:")
# tách chuỗi
print(Str.split(" "))

print("Example 8:")
# đặt chuỗi
print(Str.replace("g","abcdef"))