answer = input("質問を入力して下さい。")
with open("questionbox.txt", "w", encoding="utf-8") as f:
    f.write(answer)

