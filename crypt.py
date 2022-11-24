# Imports
import random
import math
from PIL import Image
from colorama import Fore
from pyfiglet import Figlet
import itertools
import threading
import time
import sys

# Pyfiglet Banner
custom_fig = Figlet(font='graffiti')
print(Fore.RED+custom_fig.renderText('ColorCrypt'))
print(Fore.YELLOW+'-'*10+"INFO"+'-'*10)
print(Fore.YELLOW+"This is a text to binary image encoder. The text you input will be encoded into binary, and then")

# Binary Converter
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

# Var Init
usrinpt = input(Fore.YELLOW+"[~CRYPT~] Input a string to convert to binary: ")
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
done = False
for i in iter(usrbin):

  if xplace == res:
    xplace = 0
    yplace += 1

  if i == '0':
    img.putpixel((xplace,yplace), (random.randint(1,125),random.randint(1,255),random.randint(1,255)))
  if i == '1':
    img.putpixel((xplace,yplace), (random.randint(126,255),random.randint(1,255),random.randint(1,255)))
  xplace += 1

# 100% Working Loading Animation
def animate():
    for c in itertools.cycle(['..', '.']):
        if done:
            break
        sys.stdout.write(Fore.LIGHTGREEN_EX+'\rLoading' + c)
        sys.stdout.flush()
        time.sleep(0.01)
t = threading.Thread(target=animate)
t.start()
time.sleep(4)

# Image Save & Exit
img.save('./Output/encrypted_image.png')
img.show()
done = True
print(Fore.GREEN+"\n[~CRYPT~] Image outputted successfully! Quitting.")
