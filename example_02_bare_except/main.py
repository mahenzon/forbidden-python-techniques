
def square_input_nums():
    while True:
        try:
            val = input("Enter number: ")
        except KeyboardInterrupt:
            print()
            print("Bye bye!")
            return
        try:
            print("Value", val, "squared:", int(val)**2)
        except ValueError:
            print("Error! Try again.")


def main():
    square_input_nums()


if __name__ == "__main__":
    main()
