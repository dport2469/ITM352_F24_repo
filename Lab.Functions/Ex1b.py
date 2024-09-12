from cryptography.fernet import Fernet

# Generate a key and create a cipher suite
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Get input from the user
user_input = input("Enter a string to encrypt: ")

# Encode the string to bytes, encrypt it, and then print the encrypted result
encoded_text = user_input.encode()  # Encode the string
encrypted_text = cipher_suite.encrypt(encoded_text)  # Encrypt the bytes
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text and decode back to string
decrypted_bytes = cipher_suite.decrypt(encrypted_text)  # Decrypt the bytes
decrypted_text = decrypted_bytes.decode()  # Decode back to string
print("Decrypted:", decrypted_text)