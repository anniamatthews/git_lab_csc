import sys

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        # Convert to uppercase and check if it's a letter
        if char.isalpha():
            # For uppercase letters
            encrypted_text += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
    return encrypted_text

def print_encoded_message(encoded_message):
    block_count = 0
    for i in range(0, len(encoded_message), 5):
        # Print blocks of five letters
        print(encoded_message[i:i+5], end=" ")
        block_count += 1
        # Break line after ten blocks
        if block_count == 10:
            print()
            block_count = 0
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar_cipher.py <shift>")
        return

    try:
        shift = int(sys.argv[1])
    except ValueError:
        print("Shift must be an integer")
        return

    if shift < 1 or shift > 25:
        print("Shift must be between 1 and 25")
        return

    message = input("Enter the message to encode: ")
    # Remove non-alphabetic characters and convert to uppercase
    message = ''.join(filter(str.isalpha, message)).upper()
    encrypted_message = caesar_cipher(message, shift)
    print("Encoded message:")
    print_encoded_message(encrypted_message)

if __name__ == "__main__":
    main()