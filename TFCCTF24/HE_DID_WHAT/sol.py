def fake_flag_generator():
    original_flag = "TFCCTF{fake_flag_haha}"
    generated_flag = ""

    for char in original_flag:
        # Get the ASCII value of the character, add 2, and convert back to character
        new_char = chr(ord(char) + 2)
        generated_flag += new_char

    return generated_flag


def main():
    result = fake_flag_generator()
    print(result)


if __name__ == "__main__":
    main()
