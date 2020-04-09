true_number = [0,5,1,7]

while True:
    a = input("数字を入力してください。qで終了します。")
    
    try:
        a = int(a)
    except ValueError:
        print("数字を入力してください。qで終了します。")
        
    if a in true_number:
        print("正解")
    elif a == "q":
        break
    else:
        print("不正解")
        print("数字を入力してください。qで終了します。")
    
