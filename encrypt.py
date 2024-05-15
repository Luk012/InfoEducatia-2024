import base64

class PasswordEncryptor:
    def __init__(self, password):
        self.password = password

    def xor_encrypt(self, data, key):
        key_bytes = key.encode('utf-8')  
        key_length = len(key_bytes)
        encrypted_bytes = bytearray(len(data))

        for i in range(len(data)):
            key_index = i % key_length
            encrypted_bytes[i] = data[i] ^ key_bytes[key_index]

        return bytes(encrypted_bytes)

    def write_encrypted_password(self, hash_string):
        encrypted_password = self.xor_encrypt(self.password.encode('utf-8'), hash_string)
        return base64.b64encode(encrypted_password).decode('utf-8')

    def decode_password(self, encoded_password, hash_string):
        decoded_password = base64.b64decode(encoded_password)
        decrypted_password = self.xor_encrypt(decoded_password, hash_string)
        return decrypted_password.decode('utf-8')
