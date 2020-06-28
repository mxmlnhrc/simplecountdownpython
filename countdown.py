from time import sleep


def countdown(t):
    print(f"Starting with {t} seconds")
    for i in range(t):

        print(f"Seconds remaining: {t-i}")
        sleep(1)


if __name__ == "__main__":
    x = int(input("Enter a countdown in seconds: "))
    countdown(x)