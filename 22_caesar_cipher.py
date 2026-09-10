"""Caesar cipher encryption and decryption."""


def encrypt(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - 65 + shift) % 26 + 65))
        elif char.islower():
            result.append(chr((ord(char) - 97 + shift) % 26 + 97))
        else:
            result.append(char)
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)


if __name__ == "__main__":
    message = "Hello, World!"
    shift = 3
    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
