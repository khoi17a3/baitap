#Xet ket qua hoc tap su dung lenh if...elif...else
diem_TB = eval(input("Nhap diem trung binh"))
if diem_TB >=0 and diem_TB <=10:
    if diem_TB < 5:
        print("Yeu kem!!!")
    elif diem_TB < 6:
        print("Trung binh!!")  
    elif diem_TB < 7:
        print("Trung binh - Kha!")  
    elif diem_TB < 8:
        print("Kha!")
    elif diem_TB < 9:
        print("Gioi!!!")
    else:
        print("Xuat sac!!!!!")
else:
    print("Diem nhap vao khong hop le")


