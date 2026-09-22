tasks = []


def main():
    while tasks:
        exec(tasks[0])
        remove_task(0)


def exec(task):
    print(f"executed\t{task[1]}")


def new_task(priority, name):
    tasks.append((priority, name))
    tasks.sort(reverse=True)


def remove_task(index):
    tasks.pop(index)


if __name__ == "__main__":
    new_task(2, "task1")
    new_task(3, "task2")
    main()
