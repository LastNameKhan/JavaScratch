alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

character_index = []
def encrypt(text,shift):
    for i in text:
        index_of_char = alphabet.index(i) + shift
        if index_of_char > 26:
            limitexceedchar = index_of_char - 26
            character_index.append(limitexceedchar)
        else:
            character_index.append(index_of_char)
        print(character_index)
        encoded_message = ""
        for i in character_index:
            encoded_message += alphabet[i]
        print(f"The encoded text is {encoded_message}")

decode_character = []
def decrypt(text,shift):
    for i in text:
        index_of_char = alphabet.index(i) - shift
        decode_character.append(index_of_char)
    print(character_index)
    decoded_message = ""
    for i in decode_character:
        decoded_message += alphabet[i]
    print(f"The decoded text is {decoded_message}")


if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("Invalid Input!!!!!")