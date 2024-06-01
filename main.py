import os.path as path

import numpy as np
from joblib import load

from classes import Vectorizer, Corpus, Document
from classes.state_news import StateNews

model = load(path.join('data', 'classifier.pkl'))
all_labels = model.classes_.tolist()
corpus = Corpus.load(path.join('data', 'corpus.pkl'))
vectorizer = Vectorizer()
while text := input("Введите текст для классификации:\n"):
    news = StateNews(text=text)
    lemmas = vectorizer(text)
    document = Document(corpus=corpus, lemmas=lemmas, news=news)
    tf_idf = np.array([document.tf_idf])
    label = model.predict(tf_idf)[0]
    probability = model.predict_proba(tf_idf)[0][all_labels.index(label)]
    print('Категория:', label)
    print(f'Вероятность: {probability * 100:.2f} %')
    print()
