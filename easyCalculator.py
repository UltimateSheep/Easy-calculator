import time
import random
import os

print("[ * ] python initializing...\n")
time.sleep(random.random() * 0.5)
print("[ * ] python started\n")
time.sleep(0.5)
print("[ * ] Welcome to sheep's calcuator\n")

g_num = 0
Cleared = True
ignore_clear = False

history = []


def Calculate(_num, _num2, _Operation):
    if _Operation == "+":
        return _num + _num2
    elif _Operation == "-":
        return _num - _num2
    elif _Operation == "/":
        return _num / _num2
    elif _Operation == "*":
        return _num * _num2
    elif _Operation == "^":
        return _num ** _num2
    else:
        return False


def check(_num, _type):

    if _type == "Operator":
        _Operation = str(_num)
        check2 = Calculate(5, 5, _Operation)
        if check2 == False:
            return False
        else:
            return True
    elif _type == "Num":
        num = str(_num)
        try:
            int(num)
            return "int"
        except ValueError:
            try:
                float(num)
                return "float"
            except ValueError:
                return False


def clear():
    global g_num
    global Cleared

    g_num = 0
    Cleared = True
    return


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def menu(_choice):
    choice = _choice
    # false means succesfully and break while loop
    Valid = check(choice, "Num")
    if Valid == False:
        return True
    if choice == "1":
        clear()
        return True
    if choice == "2":
        return False
    if choice == "3":
        clear_terminal()
        for v in history:
            print(f"[ ? ] {v}")
        while True:
            return_menu = input("[ * ] Return to menu? (y/n) : ")
            if str.lower(return_menu) == "y":
                return True
    if choice == "4":
        clear_terminal()
        print("[ ? ] + for summary")
        print("[ ? ] * for multiply")
        print("[ ? ] - for substact")
        print("[ ? ] / for devide")
        print("[ ? ] ^ for power")
        while True:
            return_menu = input("[ * ] Return to menu? (y/n) : ")
            if str.lower(return_menu) == "y":
                opening = False
                return True
    if choice == "5":
        history.clear()
        return True
    if choice == "6":
        return "end"


def Culculator_main():
    while True:
        global Cleared
        global g_num
        global ignore_clear
        num = ""
        num2 = ""
        _num = 0
        _num2 = 0

        if Cleared == True:
            num = input("[ * ] First number : ")

            if check(num, "Num") == False:
                print(f"[ ! ] Please, put in a valid number with ")
                Repeat = input("try agian? (y/n) : ")
                if str.lower(Repeat) == "n":
                    break
                else:
                    continue
            if check(num, "Num") == "float":
                _num = float(num)
            else:
                _num = int(num)
            Operation = input("[ * ] Operator : ")
            if check(Operation, "Operator") == False:
                print("[ ! ] Please, put in a valid Operator\n")
                Repeat = input("try agian? (y/n) : ")
                if str.lower(Repeat) == "n":
                    break
                else:
                    continue

            num2 = input("[ * ] Second number : ")

            if check(num2, "Num") == False:
                print("[ ! ] Please, put in a valid number\n")
                Repeat = input("try agian? (y/n) : ")
                if str.lower(Repeat) == "n":
                    break
                else:
                    continue
            if check(num2, "Num") == "float":
                _num2 = float(num2)
            else:
                _num2 = int(num2)
        else:
            print(f"[ ? ] The previous number is {g_num}")
            num = g_num
            _num = g_num
            if ignore_clear == False:
                _clear = input(f"[ * ] Clear? (y/n/i for ignore) : ")
                if str.lower(_clear) == "y":
                    clear()
                    continue
                elif str.lower(_clear) == "i":
                    ignore_clear = True
            Operation = input("[ * ] Operator : ")
            if check(Operation, "Operator") == False:
                print("[ ! ] Please, put in a valid Operator\n")
                Repeat = input("try agian? (y/n) : ")
                if str.lower(Repeat) == "n":
                    break
                else:
                    continue

            num2 = input("[ * ] Second number : ")
            if check(num2, "Num") == False:
                print("[ ! ] Please, put in a valid number\n")
                Repeat = input("try agian? (y/n) : ")

                if str.lower(Repeat) == "n":
                    break
                else:
                    continue
            if check(num2, "Num") == "float":
                _num2 = float(num2)
            else:
                _num2 = int(num2)
        Calculated = Calculate(_num, _num2, Operation)
        time.sleep(0.5)
        print(f"[ ? ] {num} {Operation} {num2} is {Calculated}")
        g_num = Calculated
        Cleared = False
        history.append(Calculated)
        Continue = input("[ * ] continue? (y/n/m) : ")
        time.sleep(0.5)

        if str.lower(Continue) == "y":
            continue
        elif str.lower(Continue) == "m":
            Opening_menu = True
            while Opening_menu:
                clear_terminal()
                print("[ 1 ] Clear")
                print("[ 2 ] Continue")
                print("[ 3 ] History")
                print("[ 4 ] Help")
                print("[ 5 ] Clear history ")
                print("[ 7 ] end application\n")

                choice = input("[ * ] Your choice : ")
                _menu = menu(choice)
                if _menu == "end":
                    return
                Opening_menu = _menu

        end = input("[ * ] End application? (y/n) : ")

        if str.lower(end) == "y":
            break


def main():
    Culculator_main()


if __name__ == "__main__":
    main()
