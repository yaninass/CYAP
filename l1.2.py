my_string = input("Введите вашу строку ")
glasnie = {'a', 'e', 'u', 'i', 'o', 'A', 'E', 'O', 'U', 'I', 'а', 'А', 'О', 'о', 'Е', 'е', 'у', 'ы', 'э', 'я', 'и', 'ю',
           'У', 'Ы', 'Э', 'Я', 'И', 'Ю'}
how_glasnix = 0
for char in my_string:  # проверяет циклом содержание чара из гласных в строке
    if char in glasnie:
        how_glasnix = how_glasnix + 1
soglasnie={'q','Q','w','W','R','r','t','T','p','P','s','S','D','d','f','F','g','G','h','H','J','j','k','K','L','l','z','Z','x','X','C','c','v','V','b','B','n','N','M','m',
           'й','Й','ц','Ц','к','К','н','Н','г','Г','ш','Ш','щ','Щ','з','З','х','Х','ф','Ф','в','В','п','П','р','Р','л','Л','д','Д','ж',
           'Ж','ч','Ч','с','С','м','М','т','Т','ь','Ь','ъ','Ъ','б','Б'}
how_soglasnix=0
for char in my_string:
    if char in soglasnie:
        how_soglasnix=how_soglasnix+1
print("всего гласных: ", how_glasnix)
print("всего согласных: ", how_soglasnix)
if how_soglasnix == how_glasnix:
    for char in my_string:
        if char in glasnie:
            print(char)
