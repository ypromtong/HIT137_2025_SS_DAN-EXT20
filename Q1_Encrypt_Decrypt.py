# Question1 Encryption + Decryption + Verification
import os

ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shift_char(c: str, shift: int, alphabet: str) -> str:
    """Shift character c within alphabet by shift (can be negative)."""
    idx = alphabet.find(c)
    if idx == -1:
        return c
    return alphabet[(idx + shift) % 26]


def encrypt_text(text: str, shift1: int, shift2: int) -> str:
    out = []
    for ch in text:
        # Lowercase rules
        if ch.islower():
            if 'a' <= ch <= 'm':
                k = shift1 * shift2
                out.append(shift_char(ch, k, ALPHABET_LOWER))     # forward
            else:  # n-z
                k = shift1 + shift2
                out.append(shift_char(ch, -k, ALPHABET_LOWER))    # backward

        # Uppercase rules
        elif ch.isupper():
            if 'A' <= ch <= 'M':
                k = shift1
                out.append(shift_char(ch, -k, ALPHABET_UPPER))    # backward
            else:  # N-Z
                k = shift2 ** 2
                out.append(shift_char(ch, k, ALPHABET_UPPER))     # forward

        # Other characters unchanged
        else:
            out.append(ch)

    return "".join(out)


def decrypt_text(text: str, shift1: int, shift2: int) -> str:
    out = []
    for ch in text:
        # Reverse of encryption
        if ch.islower():
            if 'a' <= ch <= 'm':
                k = shift1 * shift2
                out.append(shift_char(ch, -k, ALPHABET_LOWER))    # reverse forward
            else:
                k = shift1 + shift2
                out.append(shift_char(ch, k, ALPHABET_LOWER))     # reverse backward

        elif ch.isupper():
            if 'A' <= ch <= 'M':
                k = shift1
                out.append(shift_char(ch, k, ALPHABET_UPPER))     # reverse backward
            else:
                k = shift2 ** 2
                out.append(shift_char(ch, -k, ALPHABET_UPPER))    # reverse forward
        else:
            out.append(ch)

    return "".join(out)


def encrypt_file(shift1: int, shift2: int,
                 input_file="raw_text.txt",
                 output_file="encrypted_text.txt") -> None:
    with open(input_file, "r", encoding="utf-8") as f:
        raw = f.read()

    encrypted = encrypt_text(raw, shift1, shift2)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted)


def decrypt_file(shift1: int, shift2: int,
                 input_file="encrypted_text.txt",
                 output_file="decrypted_text.txt") -> None:
    with open(input_file, "r", encoding="utf-8") as f:
        enc = f.read()

    decrypted = decrypt_text(enc, shift1, shift2)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decrypted)


def verify_decryption(original_file="raw_text.txt",
                      decrypted_file="decrypted_text.txt") -> None:
    with open(original_file, "r", encoding="utf-8") as f:
        original = f.read()

    with open(decrypted_file, "r", encoding="utf-8") as f:
        decrypted = f.read()

    if original == decrypted:
        print("✅ Verification successful: decrypted text matches original.")
    else:
        print("❌ Verification failed: decrypted text does NOT match original.")


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number (integer).")


def main():
    print("Q1 - Encrypt / Decrypt / Verify")
    shift1 = get_int("Enter shift1 (integer): ")
    shift2 = get_int("Enter shift2 (integer): ")

    # 1) Encrypt
    encrypt_file(shift1, shift2)

    # 2) Decrypt
    decrypt_file(shift1, shift2)

    # 3) Verify
    verify_decryption()


if __name__ == "__main__":
    # Basic file check (friendly error)
    if not os.path.exists("raw_text.txt"):
        print("❌ Missing file: raw_text.txt (put it in the same folder as this script).")
    else:
        main()
