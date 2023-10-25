subject_dict = {}


def poisk(s):
    num = ''
    for char in s:
        if char.isdigit():
            num += char
        else:
            break
    return int(num) if num else 0


with open("subject.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        subject, para = line.split(":")
        para_counts = [poisk(x) for x in para.split()]
        total_para = sum(para_counts)
        subject_dict[subject.strip()] = total_para
print(subject_dict)
