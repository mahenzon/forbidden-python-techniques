def conv(val):
    try:
        return int(val)
    except ValueError:
        return -1


def main():
    numbers = ["1", "5", "a", "7"]
    for num in numbers:
        print(conv(num))


if __name__ == "__main__":
    main()
