import asyncio

async def main():
    result = await chain.ainvoke({"question": "안녕"})
    print(result)

asyncio.run(main())
