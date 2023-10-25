with open("f1.txt", "w", encoding="utf-8") as f1:
    while True:
        my_str= input("Введите вашу строку\n для заверщения введите пустую строку")
        if not my_str:
            break
        f1.write(my_str+"\n")
with open("f1.txt", "r", encoding="utf-8") as f1, open("f2.txt","w",encoding="utf-8") as f2:
    lines=f1.readlines()
    for index, my_str in enumerate(lines,start=1):
        if index%2==0:
            f2.write(my_str)
with open("f2.txt","r",encoding="utf-8") as f2:
    first_line=f2.readline()
    words=first_line.split()
    print(f"Количество слов в первой строке файла f2:{len(words)}")