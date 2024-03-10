"""
异步的从5个URL中获取页面并通过正则表达式的命名捕获组提取网站的标题
"""

import re
import asyncio
import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')

async def fetch_page(session, url):
    async with session.get(url,ssl = False) as response:
        return await response.text()

async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session,url)
        print(re.search(PATTERN,html).group('title'))

def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/',
            'https://nba.hupu.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()

if __name__ == '__main__':
    main()