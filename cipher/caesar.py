class CaesarCipher:

    @staticmethod
    def encrypt(text, shift):

        result = ""

        for char in text:

            if char.isalpha():

                offset = ord('A') if char.isupper() else ord('a')

                result += chr(
                    (ord(char) - offset + shift) % 26
                    + offset
                )

            else:
                result += char

        return result

    @staticmethod
    def decrypt(text, shift):

        return CaesarCipher.encrypt(
            text,
            -shift
        )