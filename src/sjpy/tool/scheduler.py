from __future__ import annotations

import asyncio
import traceback
from contextlib import suppress
from typing import Any, Awaitable, Callable

from sjpy.asynchronous import await_if_awaitable


class Scheduler:
    def __init__(self, cycle_time: float = 1):
        if cycle_time <= 0:
            raise ValueError("cycle_time must be greater than 0")
        self.cycle_time = cycle_time
        self._tasks: list[Callable[[], Any | Awaitable[None]]] = []
        self._task_lock = asyncio.Lock()
        self._running = asyncio.Event()
        self._schedule_task: asyncio.Task[None] | None = None

    async def add_task(self, task: Callable[[], Any | Awaitable[None]]) -> None:
        async with self._task_lock:
            self._tasks.append(task)

    async def _run(self) -> None:
        while self._running.is_set():
            start_time = asyncio.get_running_loop().time()
            async with self._task_lock:
                tasks = self._tasks.copy()
            for task in tasks:
                try:
                    await await_if_awaitable(task())
                except Exception:
                    traceback.print_exc()

            elapsed = asyncio.get_running_loop().time() - start_time
            await asyncio.sleep(max(0, self.cycle_time - elapsed))

    def stop(self) -> None:
        self._running.clear()
        if self._schedule_task and not self._schedule_task.done():
            self._schedule_task.cancel()

    async def stop_and_wait(self) -> None:
        self.stop()
        if self._schedule_task is not None:
            with suppress(asyncio.CancelledError):
                await self._schedule_task

    def start(self) -> None:
        self._running.set()
        if self._schedule_task is None or self._schedule_task.done():
            self._schedule_task = asyncio.create_task(self._run())


__all__ = ["Scheduler"]

