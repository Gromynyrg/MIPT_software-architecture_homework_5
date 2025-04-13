import requests
from collections import Counter


def get_text(url):
    response = requests.get(url)
    return response.text


def iter_words(text):
    start = 0
    in_word = False
    for i, char in enumerate(text):
        if char.isspace():
            if in_word:
                yield text[start:i]
                in_word = False
        else:
            if not in_word:
                start = i
                in_word = True
    if in_word:
        yield text[start:]


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    words_to_count = set()
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                words_to_count.add(word)

    text = get_text(url)
    word_counts = Counter(iter_words(text))

    frequencies = {word: word_counts.get(word, 0) for word in words_to_count}
    print(frequencies)


if __name__ == "__main__":
    main()
