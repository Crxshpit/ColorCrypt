# Imports
import random
import math
from PIL import Image
from colorama import Fore
import time

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def encryptor():
    usrinpt = input(Fore.YELLOW+"\n[~CRYPT~] Input a string to convert to binary: ")
    usrbin = ' '.join(str(e) for e in toBinary(usrinpt)) # .replace(" ", "")
    res = math.ceil(math.sqrt(len(usrbin)))

    # Terminal Output
    print(Fore.YELLOW+f"[~CRYPT~] The image Resolution is",Fore.LIGHTBLUE_EX+f"{res} by {res} pixels")
    print(Fore.YELLOW+f"[~CRYPT~] The character length of the translated binary is",Fore.LIGHTBLUE_EX+str(len(usrbin)))
    print(Fore.YELLOW+"[~CRYPT~] The binary is",Fore.LIGHTBLUE_EX+usrbin)

    # Init Image
    img = Image.new('RGB', (res, res))

    # Binary To Pixel
    yplace = 0
    xplace = 0
    for i in iter(usrbin):
        if xplace == 0:
            yplace += 1
        if i == '0':
            img.putpixel((xplace,yplace), (random.randint(1,125),random.randint(1,255),random.randint(1,255)))
        if i == '1':
            img.putpixel((xplace,yplace), (random.randint(126,255),random.randint(1,255),random.randint(1,255)))
            xplace += 1

    time.sleep(4)

    # Image Save & Exit
    img.save('./Output/encrypted_image.png')
    img.show()
    print(Fore.GREEN+"\n[~CRYPT~] Image outputted successfully! Quitting.")
    exit()