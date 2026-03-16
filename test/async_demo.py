import asyncio


async def func():
    print ("Hello, World!")
    await asyncio.sleep(5)
    print("Goodbye, World!")

asyncio.run(func())

