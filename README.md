# ColorCrypt - String-To-Image Encryption and Decryption Tool
![image](https://user-images.githubusercontent.com/76931137/205531393-652c17d3-8c4a-4ddc-8ca2-e63ae578738a.png)

## Overview

ColorCrypt is a personal project and original idea of mine, with the purpose of taking a given string (no longer than aprox. 1000 characters long for resolution sake) and encrypting it into an image, *pixel* by *pixel*, with the use of binary. Any image generated through this program can also be decrypted using the decoder module included. Please bear in mind **only images generated through this program** can be decrypted within the decoder module. 

**Disclaimer**: ```This scripts way of encryption is by no means secure, and was made with no intent of being used as a commercial or as a method of sensitive data encryption, but rather as a concept and a fun way to send secret messages between friends. The current method of string encoding is inadequate for any transfer of sensitive information in the regard of security as the safety of your encoded text cannot be guaranteed, and highly advised to be cautious of the information you encode and send. With a bit of brain power, it's definately possible for an image to be decoded without the use of the decoding module.```
## How The Encryption Works

- The user inputs a string of letters from the english alphabet, symbols, or numbers, converting the string to binary (ascii bytes). 
- The user is then requested to input a key (an integer in the range of 1-255). This key, or 'divider' is what the script uses to make each outputted pixel in the image represent their corresponding value of either a '1', or a '0' in binary. 
- The resolution of the outputted image is determined by the ceiled square root of the length of the translated binary from the original user inputted string (to ensure there will always be enough or some leftover pixels in the image, simply represented as RGB 0, 0, 0 pure black). 
- For each character ('1', '0' and space ' '), within the translated binary of the originally inputted string, a pixel in the image output corresponds with the character, and its associated value. 
- The way a pixels value is determined is by the red value, and the key. *If* a corresponding character with a pixel is '0', the pixel will represent this by having a **random red value that is less than than or equal to the key** (no lower than 1, the lowest an rgb value can be without being pure black). Alternatively, *if* a corresponding character with a pixel is '1', the pixel will represent this by having a **random red value that is greater than the key** (no higher than 255, the highest an rgb value can go). 
- *If* a corresponding character with a pixel is a *space* (' ') or an *excess space* at the end of an image, then the **pixel will simply be pure black** (rgb 0, 0, 0). 

### Random Example Following The Forumla:

![image](https://user-images.githubusercontent.com/76931137/206077963-24c71215-cb69-424c-8217-70548f67c13a.png)

## How The Decryption Works

Quite simply, as you would expect the decryptor/decoder module is an exact inverse of the encryptor/encoder module.

- The original key used to create the image is **required to sucessfully decrypt the image**, othewise a muddled mess will be outputted with incorrect binary being translated when the incorrect key is used.
- The decryptor iterates over each pixel of the inputted image in the directory 'Decryptor_Input'.
- For each pixel iterated over in the image, and following the formula used in encryption, each pixel will be decoded to either represent a '1', '0' or ' ' (space) and will be appended to an empty string, then being translated to text. 


![image](https://github.com/Crxshpit/ColorCrypt/blob/main/MediaAssets/ColorCryptScreenshot.png)

## Installation
1. Download and install the latest version of Python for your OS (https://www.python.org/downloads)
2. Open command prompt, use `cd (directory of choice, preferably desktop)` then copy paste `git clone https://github.com/Crxshpit/ColorCrypt && cd ColorCrypt`
3. Double click on setup.bat to install requirements.txt, or alternatively run `setup.bat` in the terminal. 
4. After installing requirements.txt, the script should run and prompt you with a terminal window. 
5. Input either `A` or `B` to select the encoder or decoder module, and follow the prompts. 
6. Outputs from the encoder module will go to the directory `Encryptor_Output`, and the input for the decoder module is `Decryptor_Input`. 
7. To use the decoder module, an image encrypted via ColorCrypt needs to be present within the directory `Decryptor_Input` with the name 'Encrypted_Image.png'.
