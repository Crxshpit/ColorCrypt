# Imports
from colorama import Fore
from pyfiglet import Figlet
from encryptor import encryptor
from decryptor import decryptor

# Banner
custom_fig = Figlet(font='chunky')
print(Fore.RED+custom_fig.renderText('ColorCrypt'))

print(Fore.YELLOW+'-'*10+"INFO"+'-'*10)
print(Fore.YELLOW+"This is a text to binary image encoder. The text you input will be encoded into binary, and then outputted to an image, with each \npixel containing a binary digit based off the divider key you will input. Only images generated via this program can be decrypted.\nRead the .README for a full manual on how to use, and report any bugs or suggestions at: https://github.com/CrashPit/ColorCrypt")

# Encoder Or Decoder
while True:
  s = input(Fore.YELLOW+"[~CRYPT~] Do you want to use the encoder [A], or the decoder [B]: ").lower()
  if s == 'a':
    encryptor()
    break
  if s == 'b':
    decryptor()
    break
  else:
    print(Fore.RED+"[~CRYPT~] Error! Invalid Input.")
    continue

