from pyfiglet import Figlet
from pystyle import *

import os

from config import *

import time


Info = Colors.blue + "[*]" + Colors.reset
Error = Colors.red + "[-]" + Colors.reset


def osint_navigator():
    print(navigator)

    try:
        choice = int(input(f"{Info} Введите пункт меню: "))

        if choice == 0:
            print("\nДо свидания!\n")
            time.sleep(1)
            

        elif choice == 1:
            print(email_osint)

            input(f"{Info} Введите Enter для выхода... ")
            main()
        
        elif choice == 2:
            print(number_osint)
            
            input(f"{Info} Введите Enter для выхода... ")
            main()

        elif choice == 3:
            print(database_osint)

            input(f"{Info} Введите Enter для выхода... ")
            main()
        
        elif choice == 4:
            print(ip_osint)

            input(f"{Info} Введите Enter для выхода... ")
            main()
        
        elif choice == 5:
            print(account_osint)

            input(f"{Info} Введите Enter для выхода... ")
            main()
        
        elif choice == 6:
            print(image_osint)

            input(f"{Info} Введите Enter для выхода... ")
            main()
        
        elif choice == 7:
            print(telegrambots_osint)

            input(f"{Info} Введите Enter для выхода... ")
            main()

        elif choice == 8:
            print(browser_osint)

            input(f"{Info} Введите Enter для выхода... ")
            main()
        
        else:
            print(f"\n{Error} Такого пункта меню нет!")
            time.sleep(1)
            retry()
        
    except ValueError:
        print(f"\n{Error} Введите корректное значение!")
        time.sleep(1)
        retry()


def retry():
    os.system('cls' if os.name == 'nt' else 'clear')
    main()


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    t = Figlet(font='slant')
    Print = t.renderText('OsintNavigator')
    Write.Print(Print, Colors.red_to_purple, interval=0.002)
    print()

    osint_navigator()


def main():
    display_banner()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nДо свидания!")