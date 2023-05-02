from concurrent.futures import Future, ThreadPoolExecutor
from typing import Any

from loguru import logger

from pysimplegui_boilerplate.common.common_function import (
    get_cpu_count,
    get_module_name,
)
from pysimplegui_boilerplate.common.profiling import elapsed_time

# Thread Concurrency Visualization https://www.jetbrains.com/help/pycharm/thread-concurrency-visualization.html

# Set the default max number of concurrent threads = 2 x CPU cores
max_workers = 2 * get_cpu_count()
executor: ThreadPoolExecutor = ThreadPoolExecutor(
    max_workers=max_workers, thread_name_prefix=f"{get_module_name()}_thread"
)


def done_callback(future: Future[Any]) -> None:
    """
    The default callback for Future once it's done. This function must be called after submitting a Future, to prevent
    the ThreadPoolExecutor swallows exception in other threads.

    https://stackoverflow.com/questions/15359295/python-thread-pool-that-handles-exceptions
    https://stackoverflow.com/a/66993893

    :param future: an asynchronous computation
    """
    logger.debug(f"The worker has done its job. Done: {future.done()}")
    exception = future.exception()
    if exception:
        logger.exception(f"The worker has raised an exception. {exception}")


def configure() -> None:
    """
    Configure thread pool.
    """
    logger.warning(
        f"Thread pool executor with {max_workers} workers, executor: {executor}"
    )


# noinspection PyProtectedMember
@elapsed_time("WARNING")
def cleanup() -> None:
    """
    Clean up thread pool.
    """
    logger.warning(
        f"Thread pool executor is being shutdown: {executor}, pending: {executor._work_queue.qsize()} jobs, "
        f"threads: {len(executor._threads)}"
    )
    executor.shutdown()
    # noinspection PyProtectedMember
    logger.warning(
        f"Thread pool executor has been shutdown: {executor}, pending: {executor._work_queue.qsize()} jobs, "
        f"threads: {len(executor._threads)}"
    )
