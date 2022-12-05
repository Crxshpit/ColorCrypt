# ColorCrypt - String-To-Image Encryption Tool
![image](https://user-images.githubusercontent.com/76931137/205531393-652c17d3-8c4a-4ddc-8ca2-e63ae578738a.png)

## Overview

ColorCrypt is a personal project and original idea of mine, with the purpose of taking a given string (no longer than aprox. 1000 characters long for resolution sake) and encrypting it into an image, *pixel* by *pixel*, with the use of binary. Any image generated through this program can also be decrypted using the decoder module included. Please bear in mind **only images generated through this program** can be decrypted within the decoder module. 

**Disclaimer**: This scripts way of encryption is by no means secure, and was made with no intent of being used as a commercial or as a method of sensitive data encryption, but rather as a concept and a fun way to send secret messages between friends. The current method of string encoding is inadequate for any transfer of sensitive information in the regard of security as the safety of your encoded text cannot be guaranteed, and highly advised to be cautious of the information you encode. With a bit of brain power, it's definately possible for an image to be decoded without the use of the decoding module. 

## How The Encryption Works

- The user inputs a string of letters from the english alphabet, symbols, or numbers, converting the string to binary (ascii bytes). 
- The user is then requested to input a key (an integer in the range of 1-255). This key, or 'divider' is what the script uses to make each outputted pixel in the image represent their corresponding value of either a '1', or a '0' in binary. 
- The resolution of the outputted image is determined by the ceiled square root of the length of the translated binary from the original user inputted string (to ensure there will always be enough or some leftover pixels in the image, simply represented as RGB 0, 0, 0 pure black). 
- For each character: '1', '0' and space (' '), within the translated binary of the originally inputted string, a pixel in the image output corresponds with the character, and its associated value. 
- The way a pixels value is determined is by the red value, and the key. If a corresponding character with a pixel is '0', the pixel will represent this by having a random red value that is less than than or equal to the key (no lower than 1, the lowest an rgb value can be without being pure black). Alternatively, if a correesponding character with a pixel is '1', the pixel will represent this by having a random red value that is greater than the key (no higher than 255, the highest an rgb value can go). 
- If a corresponding character with a pixel is a space (' '), then the pixel will simply be pure black (rgb 0, 0, 0). 
