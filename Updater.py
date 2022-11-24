import importlib.util
import sys
import subprocess
import keyboard
import urllib.request
import requests
import time

def downloader():
    lib1 = 'PIL'
    lib2 = 'colorama'
    lib3 = 'pyfiglet'

    spec1 = importlib.util.find_spec(lib1)
    spec2 = importlib.util.find_spec(lib2)
    spec3 = importlib.util.find_spec(lib3)

    print("Please report any issues during this process on Github at https://github.com/CrashPit/ColorCrypt/issues")

    if spec1 is None:
        print(lib1 +" is not installed")
        while True:
            u = input(f"Would you like to install {lib1}? (Y/N) ").lower()
            if u == 'y':
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PIL'])
                break
            if u == 'n':
                print("You may have to manually install this module if any errors occur. Continuing.")
                break
            else:
                print("Error! Invalid input. ")
                continue
    else:
       print(f"{lib1} is already installed. Continuing.")

    if spec2 is None:
        print(lib2 +" is not installed")
        while True:
            u = input(f"Would you like to install {lib2}? (Y/N) ").lower()
            if u == 'y':
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
                break
            if u == 'n':
                print("You may have to manually install this module if any errors occur. Continuing.")
                break
            else:
                print("Error! Invalid input. ")
                continue
    else:
       print(f"{lib2} is already installed. Continuing.")


    if spec3 is None:
        print(lib3 +" is not installed")
        while True:
            u = input(f"Would you like to install {lib3}? (Y/N) ").lower()
            if u == 'y':
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyfiglet'])
                break
            if u == 'n':
                print("You may have to manually install this module if any errors occur. Continuing.")
                break
            else:
                print("Error! Invalid input. ")
                continue
    else:
       print(f"{lib3} is already installed. Continuing.")

    print("You're all good to go! Press enter to continue...")
    while True:
        if keyboard.is_pressed('enter'):
            return