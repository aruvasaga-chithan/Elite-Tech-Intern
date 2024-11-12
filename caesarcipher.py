#Encrypt anf Decrypt message using caesar cipher algorithm
#AuTHOR:A.ARUVASAGA CHITHAN
#En(x) = (x + n) mod 26

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Corrected this line
    return encrypted_text  # Fixed the return indentation

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:  # Loop to allow multiple operations
        choice = int(input("\n ----------------------------\n 1. Encrypt message \n 2. Decrypt message \n 3. Exit \n---------------------------- \n Enter your choice: "))
        if choice == 3:
            print("Exiting...")
            break
        
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))    

        if choice == 1:
            print("Encrypted message:", encrypt(message, shift))
        elif choice == 2:  # Fixed comparison here
            print("Decrypted message:", decrypt(message, shift))
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
