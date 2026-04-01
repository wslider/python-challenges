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

    return result 

message = ceasar_cipher(text, shift)

def decode_ceasar_cipher(message, shift): 

    decoded_message = "" 

    for char in message: 

        if char.isupper():
            shifted = chr((ord(char) - 65 - shift) % 26 + 65)
            decoded_message += shifted
        
        elif char.islower():
            shifted = chr((ord(char) - 97 - shift) % 26 + 97)
            decoded_message += shifted

        else:
            decoded_message += char
    
    return decoded_message




ceasar_cipher(text, shift)
decode_ceasar_cipher(message, shift)

# Test Case: 

shift = 3
text = "pumpkin spice latte"

print("Original  :", text)

message = ceasar_cipher(text, shift)
print("Encrypted :", message)

decoded_message = decode_ceasar_cipher(message, shift)
print("Decrypted :", decoded_message)

# Confirmation of Test Case Result: 

if decoded_message == text:
    print("\n✅ Success! The decryption worked correctly.")
else:
    print("\n❌ Something went wrong.")