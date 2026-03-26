shift = 3 
text = "pumpkin spice latte"

def ceasar_cipher(text, shift):

    result = "" 

    # iterate though text string to build the result

    for char in text: 

        #if it is UPPERCASE (unicode starts at 65)
        if char.isupper():
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            result += shifted 

        #elif it is lowercase (unicode start at 65)
        elif char.islower():
            shifted = chr((ord(char) - 97 + shift) % 26 + 97) 
            result += shifted

        #else .. it is a space or something else (add it in)
        else:
            result += char 

    print(result)
    return result 


ceasar_cipher(text, shift)

