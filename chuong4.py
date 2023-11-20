#bai1
number = float(input("Nhập một số: "))

if number > 0:
    square = number ** 2
    print("Bình phương của", number, "là", square)
else:
    print("Số không hợp lệ. Vui lòng nhập một số dương.")

    

#bai2
N = int(input("Nhập một số tự nhiên: "))

print("Các số nguyên từ 1 đến",N, "là:")
for i in range(1, N + 1):
    print(i, end=" ")


#bai3
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n: "))

print("Các số chia hết cho", m, "trong khoảng từ 1 đến", n, "là:")
for i in range(1, n + 1):
    if i % m == 0:
        print(i, end=" ")


#bai4
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

max_num = max(num1, num2, num3)

print("Số lớn nhất trong ba số bạn nhập là: ", max_num)

#bai5
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print("BCNN của hai số nhập là: ", lcm(num1, num2))


#bai6
#Phương trình bậc nhất: ax+b=0
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
x=-b/a
if (a>0):
    print("Ta có PT:",a,"x","+",b,"=0")
    print("x=",x)
else:
    print("PT vô nghiệm")

#Tính số ngay một thang một nam
day=int(input("Nhập ngày:"))
month=int(input("Nhập tháng:"))
year=int(input("Nhập năm:"))
date= datetime(year,month,day)
print ((calendar.monthrange(year,month)))

#tìm ước chung lớn nhat
import math
x=int(input("Nhập số x:"))
y=int(input("Nhập số y:"))
print("UCLN của 2 số trên là:",math.gcd(x,y))   