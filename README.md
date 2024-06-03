# Системы и методы компьютерного моделирования
## Практическое задание №6
**Моделирование в обработке естественных языков (NLP)**

Статистические законы Ципфа. Модель BOW («модель мешка слов» – Bag Of Words).
Погружения слов, векторизация. Метод TF-IDF. Применение метода TF-IDF в задаче
классификации текста. Моделирование погружения слов с использованием библиотеки Keras.
Методы CBOW и Skip-gramms. Модели погружений русского языка. Использование
погружений в задачах обработки естественного языка.

- **Создать классы, реализующие вычисление векторов tf-idf. На основе этих классов
выполнить тематическую классификацию новостных сообщений [lenta.ru](https://lenta.ru/)**

**Остапчук Анастасия Витальевна, гр. ПМИ-201**

### Dataset новостей за период 30.05.2024 — 03.06.2024
| id | раздел            | кол-во новостей |
|----|-------------------|:---------------:|
| 1  | Спорт             |       107       |
| 2  | Силовые структуры |       198       |
| 3  | Мир               |       454       |
| 4  | Экономика         |       287       |
| 5  | Из жизни          |       70        |
| 6  | Забота о себе     |       60        |
| 7  | Бывший СССР       |       338       |
| 8  | Наука и техника   |       95        |
| 9  | Ценности          |       81        |
| 10 | Интернет и СМИ    |       101       |
| 11 | Россия            |       424       |
| 12 | Путешествия       |       83        |
| 13 | Моя страна        |       19        |
| 14 | Культура          |       96        |
| 15 | Среда обитания    |        6        |
| 16 | 69-я параллель    |        6        |
|    |                   |                 |
|    | **Всего:**        |    **2425**     |

## Результаты обучения на обучающей выборке

| раздел                  | precision (точность) | recall (полнота) | f1-score | кол-во новостей |
|:------------------------|:--------------------:|:----------------:|:--------:|:---------------:|
| 69-я параллель          |          1           |        1         |    1     |        6        |
| Бывший СССР             |         0.95         |       0.92       |   0.93   |       278       |
| Забота о себе           |         0.96         |        1         |   0.98   |       51        |
| Из жизни                |          1           |        1         |    1     |       63        |
| Интернет и СМИ          |         0.95         |       0.86       |   0.9    |       85        |
| Культура                |         0.93         |        1         |   0.97   |       83        |
| Мир                     |         0.9          |       0.97       |   0.93   |       389       |
| Моя страна              |          1           |        1         |    1     |       17        |
| Наука и техника         |         0.97         |       0.97       |   0.97   |       79        |
| Путешествия             |          1           |        1         |    1     |       70        |
| Россия                  |         0.96         |       0.92       |   0.94   |       364       |
| Силовые структуры       |         0.99         |       0.97       |   0.98   |       169       |
| Спорт                   |          1           |       0.99       |   0.99   |       92        |
| Среда обитания          |          1           |        1         |    1     |        6        |
| Ценности                |          1           |        1         |    1     |       66        |
| Экономика               |         0.98         |       0.98       |   0.98   |       243       |
| **accuracy (точность)** |                      |                  | **0.96*  |    **2061**     |

## Результаты обучения на тестовой выборке (15 %)

| раздел                  | precision (точность) | recall (полнота) | f1-score | кол-во новостей |
|:------------------------|:--------------------:|:----------------:|:--------:|:---------------:|
| Бывший СССР             |         0.85         |       0.75       |   0.8    |       60        |
| Забота о себе           |         0.67         |       0.89       |   0.76   |        9        |
| Из жизни                |         0.86         |       0.86       |   0.86   |        7        |
| Интернет и СМИ          |         0.71         |       0.62       |   0.67   |       16        |
| Культура                |         0.91         |       0.77       |   0.83   |       13        |
| Мир                     |         0.76         |       0.92       |   0.83   |       65        |
| Моя страна              |         0.5          |       0.5        |   0.5    |        2        |
| Наука и техника         |         0.88         |       0.94       |   0.91   |       16        |
| Путешествия             |          1           |       0.92       |   0.96   |       13        |
| Россия                  |         0.89         |       0.68       |   0.77   |       60        |
| Силовые структуры       |         0.78         |        1         |   0.88   |       29        |
| Спорт                   |          1           |        1         |    1     |       15        |
| Ценности                |          1           |       0.93       |   0.97   |       15        |
| Экономика               |         0.86         |       0.84       |   0.85   |       44        |
| **accuracy (точность)** |                      |                  | **0.83** |     **364**     | 
