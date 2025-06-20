import random
import time

def repeated():
    print(80 * "_")
    print()

    while True:
        try:
            level = int(input("Choose difficulty: 1 (Easy), 2 (Medium), 3 (Hard) >>> "))
            if level == 1:
                core = random.randint(1, 10)
                min_num, max_num = 1, 10
                break
            elif level == 2:
                core = random.randint(1, 50)
                min_num, max_num = 1, 50
                break
            elif level == 3:
                core = random.randint(1, 100)
                min_num, max_num = 1, 100
                break
            else:
                print("Please choose only 1, 2 or 3.")
        except:
            print(" Invalid input! Choose only a number (1, 2 or 3).")

    guess = core
    repeat = 0


    while True:
        repeat += 1
        print(f"Repeat \033[35m{repeat}\033[0m")
        print()
        time.sleep(0.4)

        try:
            asking = int(input(f"Guess a Number between {min_num} and {max_num} >>> "))
            if min_num <= asking <= max_num:
                print("\033[32m Good! Continue...\033[0m")
            else:
                print(f"\033[31m Please use numbers between {min_num} and {max_num}.\033[0m")
                continue
        except:
            print("\033[31m Enter just a number!\033[0m")
            continue

        print()
        print(30 * "=")
        time.sleep(1.1)

        if asking == guess:
            print(f"\033[32m Waw! You Win! The number is \033[33m{guess}\033[0m")
            break
        elif asking < guess:
            print("\033[34m Your number is too low.\033[0m")
        else:
            print("\033[33m Your number is too high.\033[0m")

    print()

    
    if repeat <= 3:
        print(f" You are perfect! You found the number in \033[33m{repeat}\033[0m tries.")
    elif repeat <= 6:
        print(f" That's normal. You found the number in \033[33m{repeat}\033[0m tries.")
    else:
        print(f" This is so bad... You needed \033[33m{repeat}\033[0m tries.")

    print()
    print(80 * "_")
    return repeat
    
while True:
    add = input("\nDo you want to continue? Type 'yes' to play again >>> ").lower()
    print()
    time.sleep(1.2)
    if add != "yes":
        print(f"\033[32mGood Bye Bro \033[0m")
        break
    else:
        repeated()