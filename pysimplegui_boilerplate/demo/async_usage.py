import asyncio
from typing import Any

from loguru import logger

from pysimplegui_boilerplate.common.asynchronization import async_function_wrapper
from pysimplegui_boilerplate.common.profiling import async_elapsed_time


@async_elapsed_time()
@async_function_wrapper
async def coroutine1() -> int:
    logger.info("Coroutine 1 starting...")
    await asyncio.sleep(1)
    logger.info("Coroutine 1 finished!")
    return 42


@async_elapsed_time()
@async_function_wrapper
async def coroutine2() -> str:
    logger.info("Coroutine 2 starting...")
    await asyncio.sleep(2)
    logger.info("Coroutine 2 finished!")
    return "Hello, world!"


@async_elapsed_time()
@async_function_wrapper
async def coroutine3() -> None:
    logger.info("Coroutine 3 starting...")
    await asyncio.sleep(1)
    raise ValueError("Something went wrong")


@async_elapsed_time()
@async_function_wrapper
def non_coroutine() -> None:
    logger.warning(
        "Should be raising TypeError after this log, cuz it's not an async function"
    )


async def main() -> None:
    # Run both coroutines concurrently using asyncio.gather()
    results: list[Any] = await asyncio.gather(
        *[coroutine1(), coroutine2(), coroutine3()], return_exceptions=True
    )
    logger.info(f"Results: {results}")


if __name__ == "__main__":
    from pysimplegui_boilerplate.__main__ import startup

    startup()
    # Run the event loop
    asyncio.run(main())
    logger.info(f"Type of `coroutine3()`: {type(coroutine3)}")
