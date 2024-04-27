class User:
    def __init__(self, age):
        self.age = age

    def increase_age(self):
        self.age += 1
        return self.age


def square(x):
    return x**2


def main():
    values = [1, 3, 5]
    sq_values = [n**2 for n in values]
    print(sq_values)
    sq = lambda x: x**2
    sq_values = [sq(n) for n in values]
    print(sq_values)
    sq_values = list(map(sq, values))
    print(sq_values)
    sq_values = list(map(lambda x: x**2, values))
    print(sq_values)

    sq_values = list(map(square, values))
    print(sq_values)

    names = ["john", "sam", "nick"]
    for name in names:
        print(name.title())

    print("---")
    for name in map(lambda s: s.title(), names):
        print(name)

    print("---")
    for name in map(str.title, names):
        print(name)

    u1 = User(3)
    u2 = User(5)
    for new_age in map(User.increase_age, (u1, u2)):
        print(new_age)


if __name__ == "__main__":
    main()
