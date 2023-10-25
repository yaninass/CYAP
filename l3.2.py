with open("student.txt","r",encoding="utf-8") as file:
    lines=file.readlines()
students8=[]
for line in lines:
    data=line.split()
    surname=data[0]
    grades=list(map(int,data[1:]))
    avg_grade=sum(grades)/len(grades)
    if avg_grade>8:
        students8.append(surname)
print("студенты с средним баллом выше 8:")
for student in students8:
    print(student)
