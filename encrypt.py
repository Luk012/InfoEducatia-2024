import base64
from hash import hash_string
from password import Password

def xor_encrypt(data, key):
    key_length = len(key)
    data_length = len(data)
    encrypted_bytes = bytearray(data_length)

    for i in range(data_length):
        key_index = i % key_length
        encrypted_bytes[i] = data[i] ^ key[key_index].encode('utf-8')[0]

    return bytes(encrypted_bytes)

def write_encrypted_password():
    encrypted_password = xor_encrypt(Password.encode('utf-8'), hash_string)
    encoded_password = base64.b64encode(encrypted_password).decode('utf-8')
    return encoded_password

def decode_password(encoded_password):
    decoded_password = base64.b64decode(encoded_password)
    decrypted_password = xor_encrypt(decoded_password, hash_string)
    return decrypted_password.decode('utf-8')

encrypted_password = write_encrypted_password()
print("Encrypted password:", encrypted_password)

decrypted_password = decode_password(encrypted_password)
print("Decrypted password:", decrypted_password)
