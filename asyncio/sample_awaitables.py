import asyncio


async def nested():
    return 42


async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    print(nested())  # will print coroutine object

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


if __name__ == "__main__":
    asyncio.run(main())
