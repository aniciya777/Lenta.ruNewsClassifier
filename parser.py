import asyncio
import json
from os.path import join
import sys

import aiohttp
import requests
from aiohttp import ClientSession
from bs4 import BeautifulSoup

from models.db_session import global_init, create_session
from models.news import News
from models.chapters import Chapter


def prepare_text(text: str) -> str:
    text = text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.strip()


async def _save_article(url: str, chapter_name: str, session: ClientSession) -> None:
    response = await session.get(url)
    soup = BeautifulSoup(await response.text(), features="html.parser")
    schema = json.loads("".join(soup.find("script", {"type": "application/ld+json"}).contents))
    title = prepare_text(schema['headline'])
    text = prepare_text(schema['articleBody'])

    db_session = create_session()
    new_article = News(title=title, text=text, url=url, chapter=Chapter.get_by_name(chapter_name, db_session))
    db_session.add(new_article)
    db_session.commit()
    print(new_article)


async def save_article(url: str, chapter_name: str, session: ClientSession) -> None:
    try:
        await _save_article(url, chapter_name, session)
    except Exception as e:
        print(e, file=sys.stderr)


async def main() -> None:
    start_page = 1
    async with aiohttp.ClientSession() as session:
        for _ in range(100):
            print(f'Страница {start_page}')
            coroutines = []
            response = requests.get(f'https://lenta.ru/parts/news/{start_page}')
            soup = BeautifulSoup(response.text, features="html.parser")
            for article in soup.find_all('li', class_='parts-page__item'):
                url = article.find('a').get('href')
                url = 'https://lenta.ru' + url
                chapter = article.find('span', class_='card-full-news__rubric')
                if chapter:
                    coroutines.append(save_article(url, chapter.text, session))
            await asyncio.gather(*coroutines)
            start_page += 1


if __name__ == '__main__':
    global_init(join('db', 'news.sqlite'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
