import asyncio
import random
import time


class Queue:
    def __init__(self):
        self.queue = []
        self.len = 0

    def push(self, value):
        self.queue.append(value)
        self.len += 1

    def pop(self):
        self.len -= 1
        return self.queue.pop(self.len - 1)

    def __str__(self):
        return ", ".join([str(x) for x in self.queue])


class TaskQueue:
    def __init__(self):
        self.queue = []
        self.tasks = 0
        self.active_tasks = 0
        self.capacity = 3

    def push(self, taskFactory):
        self.queue.append(taskFactory)
        self.tasks += 1

    def pop(self):
        if self.active_tasks < self.capacity:
            self.tasks -= 1
            self.active_tasks += 1
            self.queue.pop().task.execute(self.tasks)
            self.active_tasks -= 1


class TaskFactory:
    def __init__(self):
        self.task = Task(time.sleep, random.random())


class Task:
    def __init__(self, callable, *args, **kwargs):
        self.callable = callable
        self.args = args
        self.kwargs = kwargs

    def execute(self, id):
        print(f"task start ! -- id: {id}")
        self.callable(*self.args, **self.kwargs)
        print(f"task ended ! -- id: {id}")


class AsyncTaskQueue:
    def __init__(self, capacity):
        self.queue = asyncio.Queue(maxsize=capacity)

    def push(self, taskFactory):
        self.queue.put(taskFactory)

    def pop(self):
        self.queue.get().send()
