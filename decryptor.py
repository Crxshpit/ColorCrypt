# Imports
from PIL import Image
from colorama import Fore
import time

# Encryptor function
def decryptor():
    print(Fore.BLUE+"\n--COLOR-CRYPT DECRYPTOR--")

    # Attempting image open
    while True:
            print(Fore.YELLOW+"\n[~CRYPT~] Put the image you wish to decrypt into the folder 'Decryptor_Input'. The image must be named 'encrypted_image.png'. Checking for image in 10 seconds...")
            time.sleep(10)
            try:
                img = Image.open('Decryptor_Input/encrypted_image.png')
                imgheight = int(img.height)
                imgwidth = int(img.width)
                if imgheight > 900 or imgwidth > 900:
                   print(Fore.RED+"[~CRYPT~] Image resolution too large (maximum 900x900).")
                   continue
                else:
                    print(Fore.GREEN+"[~CRYPT~] Image located successfully!")
                    break
            except:
                print(Fore.RED+"[~CRYPT~] Image not found in directory. Make sure the image name is 'encrypted_image.png' and try again.")
                continue

    # Invalid input error catching
    while True:
        try:
            key = int(input(Fore.YELLOW+"[~CRYPT~] Input the image key (must be an integer between 1-255): "))
            if key > 255 or key <= 1:
                print(Fore.RED+"[~CRYPT~] Invalid input. Please input a number between 1 and 255.")
                continue
        except ValueError:
            print(Fore.RED+"[~CRYPT~] Invalid input. Please input a number between 1 and 255.")
        else:
            break

    # Terminal Output
    print(Fore.YELLOW+"[~CRYPT~] The image Resolution is",Fore.LIGHTBLUE_EX+f"{int(imgwidth/10)} by {int(imgheight/10)} pixels ({imgwidth} by {imgheight} in true pixels).")

    res = int((imgwidth/10)*(imgheight/10))

    # Binary To Pixel
    yplace = 0
    xplace = 0
    binraw = ""
    for i in range(res):

        if xplace == imgwidth: # Move down to next layer
            xplace = 0
            yplace += 10

        # Retrieve the red value from the raw rgb
        rgb = str(img.getpixel((xplace, yplace)))
        xl = rgb.split(',', 1)[0]
        r = xl.strip('(')

        if int(r) == 0:
            binraw += ' '
            xplace += 10
            continue
        if int(r) >= key+1:
            binraw += '1'
            xplace += 10
        if int(r) <= key:
            binraw += '0'
            xplace += 10

    # Removes whitespace at end of binary
    binx = binraw.split()
    bin = ' '.join(binx)

    binconvert = "".join([chr(int(binary, 2)) for binary in bin.split(" ")]) # Converts the binary to text

    # Final Output
    print(Fore.GREEN+f"[~CRYPT~] Image decryption successful! Decrypted string: {Fore.LIGHTBLUE_EX+binconvert}")
    print("[~CRYPT~] Task successful. Quitting")

