# Imports
import importlib.util
import sys
import subprocess
import time

# Downloader function
def downloader():
    lib = ['PIL', 'colorama', 'pyfiglet'] # Append future downloadable libraries required

    print("You may have to run the program as administrator for downloads to work. Please report any issues during this process on Github at https://github.com/CrashPit/ColorCrypt/issues")

    for i in lib:
        spec = importlib.util.find_spec(i) # Search system for library
        if spec is None:
            print(i+" is not installed")
            while True:
                u = input(f"Would you like to install {i}? (Y/N) ").lower()
                if u == 'y':
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', i]) # Executes install
                    break
                if u == 'n':
                    print("You may have to manually install this module if any errors occur. Continuing.")
                    break
                else:
                    print("Error! Invalid input. ")
                    continue
        else:
            print(f"{i} is already installed. Continuing.")

    print("You're all good to go! Continuing in 5 seconds...")
    time.sleep(5)
    return
