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
| 1  | Спорт             |       98        |
| 2  | Силовые структуры |       163       |
| 3  | Мир               |       414       |
| 4  | Экономика         |       242       |
| 5  | Из жизни          |       62        |
| 6  | Забота о себе     |       52        |
| 7  | Бывший СССР       |       296       |
| 8  | Наука и техника   |       86        |
| 9  | Ценности          |       68        |
| 10 | Интернет и СМИ    |       87        |
| 11 | Россия            |       372       |
| 12 | Путешествия       |       69        |
| 13 | Моя страна        |       18        |
| 14 | Культура          |       89        |
| 15 | Среда обитания    |        6        |
| 16 | 69-я параллель    |        4        |
|    |                   |                 |
|    | **Всего:**        |    **2126**     |

## Результаты обучения на обучающей выборке

| раздел                  | precision (точность) | recall (полнота) | f1-score | кол-во новостей |
|:------------------------|:--------------------:|:----------------:|:--------:|:---------------:|
| 69-я параллель          |          1           |        1         |    1     |        4        |
| Бывший СССР             |         0.95         |       0.89       |   0.92   |       246       |
| Забота о себе           |         0.96         |        1         |   0.98   |       48        |
| Из жизни                |          1           |        1         |    1     |       52        |
| Интернет и СМИ          |         0.94         |       0.84       |   0.89   |       69        |
| Культура                |         0.9          |        1         |   0.95   |       76        |
| Мир                     |         0.9          |       0.97       |   0.94   |       355       |
| Моя страна              |          1           |        1         |    1     |       15        |
| Наука и техника         |         0.97         |       0.99       |   0.98   |       75        |
| Путешествия             |          1           |        1         |    1     |       55        |
| Россия                  |         0.96         |       0.9        |   0.93   |       315       |
| Силовые структуры       |         0.97         |       0.98       |   0.97   |       135       |
| Спорт                   |          1           |       0.99       |   0.99   |       88        |
| Среда обитания          |          1           |        1         |    1     |        5        |
| Ценности                |          1           |        1         |    1     |       60        |
| Экономика               |         0.97         |       0.98       |   0.97   |       209       |
|                         |                      |                  |          |                 |
| **accuracy (точность)** |                      |                  | **0.95** |    **1807**     |

## Результаты обучения на тестовой выборке (15 %)

| раздел                  | precision (точность) | recall (полнота) | f1-score | кол-во новостей |
|:------------------------|:--------------------:|:----------------:|:--------:|:---------------:|
| 69-я параллель          |          0           |      *NaN*       |    0     |        0        |
| Бывший СССР             |         0.85         |       0.8        |   0.82   |       50        |
| Забота о себе           |         0.67         |        1         |   0.8    |        4        |
| Из жизни                |         0.64         |       0.9        |   0.75   |       10        |
| Интернет и СМИ          |         0.9          |       0.5        |   0.64   |       18        |
| Культура                |         0.77         |       0.77       |   0.77   |       13        |
| Мир                     |         0.81         |       0.92       |   0.86   |       59        |
| Моя страна              |          1           |       0.33       |   0.5    |        3        |
| Наука и техника         |          1           |       0.73       |   0.84   |       11        |
| Путешествия             |          1           |       0.71       |   0.83   |       14        |
| Россия                  |         0.83         |       0.84       |   0.83   |       57        |
| Силовые структуры       |         0.93         |       0.96       |   0.95   |       28        |
| Спорт                   |          1           |        1         |    1     |       10        |
| Среда обитания          |        *NaN*         |        0         |    0     |        1        |
| Ценности                |          1           |        1         |    1     |        8        |
| Экономика               |         0.76         |       0.85       |   0.8    |       33        |
|                         |                      |                  |          |                 |
| **accuracy (точность)** |                      |                  | **0.83** |     **319**     | 
