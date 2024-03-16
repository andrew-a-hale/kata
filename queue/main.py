import random

from que import AsyncTaskQueue, TaskFactory, TaskQueue


def main():
    queue()
    task_queue()


def task_queue():
    tq = AsyncTaskQueue(3)
    [tq.push(TaskFactory()) for _ in range(10)]
    while tq.tasks > 0:
        tq.pop()


def queue():
    q = AsyncTaskQueue(3)
    [q.push(random.randint(a=1, b=10)) for _ in range(10)]
    q.pop()
    q.pop()
    q.pop()
    print(q)


if __name__ == "__main__":
    main()
