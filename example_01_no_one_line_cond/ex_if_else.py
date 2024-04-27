
def check_age(age):
    if age >= 21:
        return "Adult enough"
    if age >= 18:
        return "OK"
    return "Too young!"


def main():
    print(check_age(22))
    print(check_age(18))
    print(check_age(16))


if __name__ == "__main__":
    main()
