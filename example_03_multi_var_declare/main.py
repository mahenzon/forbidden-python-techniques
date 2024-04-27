def get_point():
    return 4, 5


def main():
    # a, b = 1, 2
    # a = b = 4
    a = 3
    b = 4
    print(a * b)

    print(f"{a=}, {b=}")
    a, b = b, a
    print(f"{a=}, {b=}")

    p = get_point()
    print(p)

    x, y = p
    print(x, y)

    x1, y1 = get_point()
    print(x1, y1)

    line = "foo,bar"
    l1, l2 = line.split(",")
    print(l1)
    print(l2)


if __name__ == "__main__":
    main()
