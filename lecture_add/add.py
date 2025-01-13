import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize


input_text = input('Введите текст: ')
words = word_tokenize(input_text)
search_word = input('Введите слово: ').lower()
print(f'Количество вхождений: {words.count(search_word)}, всего: {len(words)}')