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

    # Variable init - String to encrypt
    while True:
            usrinpt = input(Fore.YELLOW+"\n[~CRYPT~] Input a string to convert to binary: ")
            usrbin = str(' '.join(str(e) for e in toBinary(usrinpt)))
            res = math.ceil(math.sqrt(len(usrbin)))
            if res > 90:
                print(Fore.RED+"[~CRYPT~] Error. Inputted string is too long.")
                continue
            else:
                break

    # Variable init - Key to use
    while True:
        try:
            divi = input(Fore.YELLOW+"[~CRYPT~] Input three integers between 1-255 seperated by ',' to be the key (eg. 125,125,125): ")
            x = divi.split(',')
            usrkey = [int(item) for item in x]
            if len(x) != 3:
                print(Fore.RED+"[~CRYPT~] Invalid input.")
                continue
            for i in usrkey:
                if i > 255 or i <= 0:
                    print(Fore.RED+"[~CRYPT~] Invalid input.")
                    break
            else:
                break
        except ValueError:
            print(Fore.RED+"[~CRYPT~] Invalid input.")
            continue



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
        while True:
            rran = random.randint(1,255)
            gran = random.randint(1,255)
            bran = random.randint(1,255)
            if rran > usrkey[0] and gran > usrkey[1] and bran > usrkey[2]:
                continue
            else:
                break
        if xplace == res:
            xplace = 0
            yplace += 1
        if i == '0':
            img.putpixel((xplace,yplace), (rran,gran,bran))
            xplace += 1
        if i == '1':
            img.putpixel((xplace,yplace), (random.randint(usrkey[0]+1,255),random.randint(usrkey[1],255),random.randint(usrkey[2],255)))
            xplace += 1
        if i == ' ':
            img.putpixel((xplace, yplace), (0, 0, 0))
            xplace += 1

    imgu = img.resize((res*10, res*10), resample=Image.BOX)
    print(Fore.YELLOW+"[~CRYPT~] Image created successfully! Generated image saved to 'Encryptor_Output'.")
    imgu.show()
    imgu.save('./Encryptor_Output/encrypted_image.png')
    exit()

# To-do

# Ensure pixel value is above 3 collective inputted key values when '1'
# Ensure randomization of pixel values when '0', but all 3 pixel values cannot be above key values collectively
