def hello_world():
    print("Hello World")


def print_loop(times: int = 5) -> None:
    for i in range(times):
        hello_world()


if __name__ == "__main__":
    print_loop()
