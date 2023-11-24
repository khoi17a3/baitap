#1.1py

print("**    **   ******   **      **      ******")
print("**    **   **       **      **      **  **")
print("********   ******   **      **      **  **")
print("**    **   **       **      **      **  **")
print("**    **   ******   ******  ******  ******")

#1.2.py

# Nhập thông tin hàng hóa
ten_hang = "Sữa hộp Vina Milk"
so_luong = 5
don_gia = 25000

# Tính tiền phải trả
tien_phai_tra = so_luong * don_gia

# Xuất kết quả
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Đơn giá:", don_gia, "vnđ")
print("Tiền phải trả:", "{:,}".format(tien_phai_tra), "vnđ")


#1.3.py

# Nhập thông tin hàng hóa
ten_hang = "Sữa hộp Vina Milk"
so_luong = 5
don_gia = 25000

# Tính tiền phải trả
tien_phai_tra = so_luong * don_gia

# Xuất kết quả
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Đơn giá:", don_gia, "vnđ")
print("Tiền phải trả:", "{:,}".format(tien_phai_tra), "vnđ")

#1.4.py
a=(5-3)//2
b=8-(3*2)-(1+1)
print(a)
print(b)

#1.5.py

so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá: "))
thanh_tien = so_luong * don_gia
print("Thành tiền:", so_luong, "*", don_gia, "=", thanh_tien)

#1.6py

a=int(input("số kẹo alcie có:"))
b=int(input("số kẹo bob có:"))
c=int(input("số kẹo carol có:"))
print("số kẹo thừa sẽ đạp đi:",(a+b+c)%3)

#1.7py

a=float(input("nhập độ C:"))
print("độ F=",1.8*a+32)

#1.8py

a=input("nhập chuỗi s1:")
b=input("nhập chuỗi s2:")
c=input("nhập chuỗi s3:")
d=input("nhập index:")
print("chiều dài chuỗi s1=",len(a))
print("chiều dài chuỗi s2=",len(b))
print("chiều dài chuỗi s3=",len(c))
print("chuỗi s4 =",a[d:])
print("chuỗi s2 lập lại 2 lần",b*2)

#1.9py

a=float(input("lãi xuất năm(%):"))
b=int(input("số tiền gửi:"))
c=int(input("số tháng gửi:"))
d =(b*c)*(a/100/12)
print("tiền lãi=",d)
print("tiền vốn+lãi",d+b)
