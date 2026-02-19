import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_multiple(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)


# 사용
urls = [
    "https://api.exchangerate-api.com/v4/latest/USD",
    "https://date.nager.at/api/v3/PublicHolidays/2024/KR",
]

results = asyncio.run(fetch_multiple(urls))
