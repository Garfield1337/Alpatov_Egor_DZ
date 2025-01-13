import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize, regexp_tokenize
from pymorphy2 import MorphAnalyzer
from bs4 import BeautifulSoup
from gensim.models import Word2Vec
from sklearn.manifold import TSNE

#Подгружаем стоп-слова
nltk.download('stopwords')
stop = set(stopwords.words('russian'))

#Все функции для очистки датасета и токенизации
#Удаляем стоп-слова
def stopwords(text):
    return " ".join([stop_word for stop_word in str(text).split() if stop_word not in stop])

#Удаляем эмодзи
def emoji(text):
    emoji = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji.sub(r'', text)

#Удаляем URL-ссылки
def url(text):
    urls = re.compile(r'https?://\S+|www\.\S+')
    return urls.sub(r'', text)

#Удалем разметку HTML
def tags(text):
    return BeautifulSoup(text, "lxml").text

#Проводим токенизацию через pymorphy2
def tokenize(sent, pat=r"(?u)\b\w\w+\b", morph=MorphAnalyzer()):
    return [morph.parse(tok)[0].normal_form
            for tok in regexp_tokenize(sent, pat)]

#Загружаем исходный датасет
df = pd.read_csv("файл с путем", encoding='UTF8', sep="\t")

#Переводим все в нижний регистр, удаляем знаки препинания, цифры, применяем функции для очистки
df['text_ready'] = df['review'].str.lower()
df['text_ready'] = df['text_ready'].str.replace(r'\d+', '', regex=True)
df['text_ready'] = df['text_ready'].str.replace('[^\w\s]', '', regex=True)
df['text_ready'] = df["text_ready"].apply(stopwords)
df['text_ready'] = df['text_ready'].apply(url)
df['text_ready'] = df['text_ready'].apply(emoji)
df['text_ready'] = df['text_ready'].apply(tags)

#Удаляем лишнюю колонку и сохраняем готовый файл
df.drop(columns=['review'], inplace=True)
df.to_excel('файл с путем', index=False)

#Применяем функцию токенизации
df['text_token'] = df['text_ready'].apply(tokenize)
sentences = df['text_token']

#Задаем параметры модели для обучения
v_model = Word2Vec(
    min_count=10,
    window=5,
    vector_size=1000,
    negative=5,
    workers=24,
    alpha=0.03,
    min_alpha=0.0007,
    sample=6e-5,
    sg=1)

#Строим словарь, обучаем модель
v_model.build_vocab(sentences)
v_model.train(sentences, total_examples = v_model.corpus_count, epochs=6, report_delay=1)

#Смотрим по схожести слов, разные параметры
print(v_model.wv.most_similar(positive=["классно"], topn=10), sep='\n')
print('')
print(v_model.wv.most_similar(positive=["ткань"], topn=10), sep='\n')
print('')
print(v_model.wv.most_similar_to_given("классный", ["отличный", "замечательный", "крутой"]))
print('')

#Функция для визуализации
def tsne_vis(model, word, list_names):
    #Извлекаем вектор центрального слова, задаем ему красный цвет
    vectors_words = [model.wv.get_vector(word)]
    word_labels = [word]
    color_list = ['red']

    #Извлекаем похожие слова (10 штук), добавляем их, задаем им зеленый цвет
    close_words = model.wv.most_similar(word)
    for word_score in close_words:
        word_vector = model.wv.get_vector(word_score[0])
        vectors_words.append(word_vector)
        word_labels.append(word_score[0])
        color_list.append('green')

    #Добавляем другие слова, которые передаем по списку,задаем черный цвет
    for word1 in list_names:
        word_vector1 = model.wv.get_vector(word1)
        vectors_words.append(word_vector1)
        word_labels.append(word1)
        color_list.append('black')

    #Применяем метод t-SNE
    vectors_words = np.array(vectors_words)
    Y = TSNE(n_components=2, random_state=0, perplexity=min(5, len(vectors_words) - 1), init="pca").fit_transform(
        vectors_words)
    #Результат снижения размерности сохраняяем в фрейм
    df_tsne = pd.DataFrame({"x": Y[:, 0], "y": Y[:, 1], "words": word_labels, "color": color_list})

    fig, _ = plt.subplots(figsize=(9, 9))
    p1 = sns.regplot(data=df_tsne, x="x", y="y", fit_reg=False, marker="o",
                     scatter_kws={"s": 40, "facecolors": df_tsne["color"]})

    for line in range(0, df_tsne.shape[0]):
        p1.text(df_tsne["x"][line], df_tsne["y"][line], " " + df_tsne["words"][line].title(),
                horizontalalignment="left", verticalalignment="bottom", size="medium", color=df_tsne["color"][line],
                weight="normal").set_size(15)

    plt.xlim(Y[:, 0].min() - 50, Y[:, 0].max() + 50)
    plt.ylim(Y[:, 1].min() - 50, Y[:, 1].max() + 50)
    plt.title('t-SNE visualization for {}'.format(word.title()))
    plt.show()


tsne_vis(v_model, "качественный", ["плохой", "ужасный", "нормальный"])