def chuyen_doi_C_sang_F(do_C)
    do_F = (do_C * 9/5) + 32
    return do_F
do_C = float(input("Nhập nhiệt độ C: "))
do_F = chuyen_doi_C_sang_F(do_C)
print(f"ơ{do_C} độ C tương đương{do_F} độ F. ")