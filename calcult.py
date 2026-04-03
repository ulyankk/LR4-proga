def readline(file_name):
    f = open(file_name, "r")
    line = f.readline()
    numbers = set(map(int, line.split()))
    f.close()
    return numbers

# Читаем оба файла через ОДНУ И ТУ ЖЕ функцию
set_a = readline("file_one")
set_b = readline("file_two")

print("Множество A:", set_a)
print("Множество B:", set_b)


print("КАЛЬКУЛЯТОР МНОЖЕСТВ")
print("1 - Объединение (A ∪ B)")
print("2 - Пересечение (A ∩ B)")
print("3 - Вычитание (A - B)")
print("4 - Декартово произведение (A × B)")
print("5 - Выборка (по условию из A)")
print("6 - Выход")
# сделаем цикл чтобы система спрашивала че мы хотим пока не выйдем из цикла
flag = True
while flag:
    vibor = input("Твой выбор: ")

    if vibor == "1":
        print("Объединение:", set_a | set_b)
    elif vibor == "2":
        print("Пересечение:", set_a & set_b)
    elif vibor == "3":
        print("Вычитание (A - B):", set_a - set_b)
    elif vibor == "4":
        decart = {(a, b) for a in set_a for b in set_b}
        print("Декартово произведение:", decart)
    elif vibor == "5":
        print("Выборка по условию")
        print("Из какого множества?")
        print("1 - Множество A")
        print("2 - Множество B")
        which = input("Твой выбор (1 или 2): ")

        print("Что делаем?")
        print("1 - Больше чем число")
        print("2 - Меньше чем число")
        oper = input("Твой выбор (1 или 2): ")

        num = int(input("Введи число: "))

        if which == "1":
            source_set = set_a
            set_name = "A"
        elif which == "2":
            source_set = set_b
            set_name = "B"
        else:
            print("Неверный выбор множества")
            continue

        if oper == "1":
            result = {x for x in source_set if x > num}
            print(f"Элементы множества {set_name} больше {num}: {result}")
        elif oper == "2":
            result = {x for x in source_set if x < num}
            print(f"Элементы множества {set_name} меньше {num}: {result}")
        else:
            print("Неверный выбор операции")
    elif vibor == "6":
        flag = False
        print("Выход из программы")
        break
    else:
        print("Неверный выбор")

