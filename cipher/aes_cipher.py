from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


class AESCipher:

    def __init__(self, key):

        self.key = key.ljust(32)[:32].encode()

    def encrypt(self, plaintext):

        cipher = AES.new(
            self.key,
            AES.MODE_CBC
        )

        ciphertext = cipher.encrypt(
            pad(
                plaintext.encode(),
                AES.block_size
            )
        )

        encrypted = (
            cipher.iv +
            ciphertext
        )

        return base64.b64encode(
            encrypted
        ).decode()

    def decrypt(self, encrypted_text):

        data = base64.b64decode(
            encrypted_text
        )

        iv = data[:16]

        ciphertext = data[16:]

        cipher = AES.new(
            self.key,
            AES.MODE_CBC,
            iv
        )

        plaintext = unpad(
            cipher.decrypt(ciphertext),
            AES.block_size
        )

        return plaintext.decode()