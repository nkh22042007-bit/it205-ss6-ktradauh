def main() :
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