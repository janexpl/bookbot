def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters


def sort_on(items):
    return items["num"]


def sorted_list(dict):
    elements = []
    for element in dict:
        char = {"char": element, "num": dict[element]}
        elements.append(char)
    elements.sort(key=sort_on, reverse=True)
    return elements
