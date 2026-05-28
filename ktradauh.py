def main():
    stock = input("nhap so luon ton kho :")


    if stock >= 50 :
        print("hang day kho")
    elif stock > 10 :
        print("muc an toan")
    else :
        print("sap het hang, can bao cao nhap them")
    
    error_product = 0

    while True :
        quantity_error_product = int(input("nhap so hang loi cua tung quay"))
        if error_product == -1 :
            print("da thong ke xong")
            break
        elif quantity_error_product != -1 :
            error_product = error_product + quantity_error_product 
        
        break
    print(error_product)

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