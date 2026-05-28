def main():
    keyboard_stock = 100

    while True :
        stock_out = int(input("nhap vao so luong muon xuat"))

        if stock_out < 0:
            print("khong duoc nhap so am, vui long nhap lai")
            continue
        elif stock_out > keyboard_stock :
            print("khong du hang, vui long nhap lai")
            continue
        else :
            keyboard_stock = keyboard_stock - stock_out
            print("xuat kho thanh cong")
            print("ton kho con lai:",keyboard_stock)
            break