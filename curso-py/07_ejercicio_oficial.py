def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reverse(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text


def is_palindrome(text):
    text = no_space(text)
    print(text)
    reversed_text = reverse(text)
    print(reversed_text)

    return text.lower() == reversed_text.lower()


print(is_palindrome("Amo la paloma"))
