import requests
from collections import Counter
from typing import Dict, List, Set


def fetch_text(url: str) -> str:
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return ""


def load_unique_words(filepath: str) -> Set[str]:
    words = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if word:
                    words.add(word)
    except FileNotFoundError:
        print(f"Файл {filepath} не найден")
    return words


def count_all_word_frequencies(text: str, words_to_count: Set[str]) -> Dict[str, int]:
    text_words = text.split()
    all_frequencies = Counter(text_words)
    return {word: all_frequencies.get(word, 0) for word in words_to_count}


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"
    words_to_count = load_unique_words(words_file)
    print(f"Найдено уникальных слов: {len(words_to_count)}")
    text = fetch_text(url)
    frequencies = count_all_word_frequencies(text, words_to_count)

    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    print("\nРезультаты (слово: частота):")
    for word, count in sorted_frequencies:
        if count > 0:
            print(f"  {word}: {count}")

    print(f"\nВсего слов найдено: {sum(frequencies.values())}")


if __name__ == "__main__":
    main()