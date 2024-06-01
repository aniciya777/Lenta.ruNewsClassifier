import os

import pandas as pd

from models.db_session import global_init, create_session
from models.chapters import Chapter


if __name__ == '__main__':
    global_init(os.path.join('db', 'news.sqlite'))
    db_session = create_session()
    arr = []
    for chapter in db_session.query(Chapter).all():
        arr.append((chapter.id, chapter.name, len(chapter.news)))
    df = pd.DataFrame(arr, columns=['id', 'раздел', 'кол-во новостей'])
    print(df.to_markdown(index=False, tablefmt='github'))
