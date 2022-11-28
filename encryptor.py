# Imports
import random
import math
from PIL import Image
from colorama import Fore

# Converts inputted string to binary
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

# Encryptor function
def encryptor():
    print(Fore.BLUE+"\n--COLOR-CRYPT ENCODER--")

    # Variable init
    while True:
            usrinpt = input(Fore.YELLOW+"\n[~CRYPT~] Input a string to convert to binary: ")
            usrbin = str(' '.join(str(e) for e in toBinary(usrinpt)))
            res = math.ceil(math.sqrt(len(usrbin)))
            if res > 90:
                print(Fore.RED+"[~CRYPT~] Error. Inputted string is too long.")
                continue
            else:
                break


    while True:
        try:
            divi = int(input(Fore.YELLOW+"[~CRYPT~] Input an integer between 1-255 to be the key: "))
            if divi > 255 or divi <= 1:
                print(Fore.RED+"[~CRYPT~] Invalid input. Please input a number between 1 and 255.")
                continue
        except ValueError:
            print(Fore.RED + "[~CRYPT~] Invalid input. Please input a number between 1 and 255.")
        else:
            break


    # Terminal Output
    print(Fore.YELLOW+"[~CRYPT~] The image Resolution is",Fore.LIGHTBLUE_EX+f"{res} by {res} pixels ({res*10} by {res*10} in true pixels).")
    print(Fore.YELLOW+f"[~CRYPT~] The character length of the translated binary is {Fore.LIGHTBLUE_EX+str(len(usrbin.replace(' ', '')))} digits long.")
    print(Fore.YELLOW+"[~CRYPT~] The binary is",Fore.LIGHTBLUE_EX+usrbin)

    # Init Image
    img = Image.new('RGB', (res, res))

    # Binary To Pixel
    yplace = 0
    xplace = 0
    for i in iter(usrbin):
        if xplace == res:
            xplace = 0
            yplace += 1
        if i == '0':
            img.putpixel((xplace,yplace), (random.randint(1,divi),random.randint(1,255),random.randint(1,255)))
            xplace += 1
        if i == '1':
            img.putpixel((xplace,yplace), (random.randint(divi+1,255),random.randint(1,255),random.randint(1,255)))
            xplace += 1
        if i == ' ':
            img.putpixel((xplace, yplace), (0, 0, 0))
            xplace += 1

    imgu = img.resize((res*10, res*10), resample=Image.BOX)
    print(Fore.YELLOW+"[~CRYPT~] Image created successfully! Generated image saved to 'Encryptor Output'.")
    imgu.show()
    imgu.save('./Encryptor Output/encrypted_image.png')
    exit()

