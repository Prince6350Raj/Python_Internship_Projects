alphabet = [" ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','&', '%', '@', '#']

# alphabet = [" ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', 'e', '&', '%', '@', '#']


direction = input("Type 'encode to encrypt and type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
def encrypt(plain_text,shift_amount):
    cipher_text= ""
    for letter in plain_text:
        position = alphabet.index(letter)
        #new_position = position + shift_amount
        new_position = (position + shift_amount)%len(alphabet)

        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"Encoded message is: {cipher_text}")

def decrypt(cipher_text,shift_amount):
    plain_text= ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        #new_position = position - shift_amount
        new_position = (position - shift_amount)%len(alphabet)
        plain_text += alphabet[new_position]
    print(f"Decoded message is: {plain_text}")

if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)

elif direction == "decode":
    decrypt(cipher_text=text,shift_amount=shift)

else:
    print("You inserted INVALID direction")


