def add_many_number(numbers) -> int:
    total: int = 0
    for number in numbers:
        total += number
    return total


def main():
    numbers :list[int] = [1, 2, 3, 4, 5]
    sum_of_numbers = add_many_number(numbers)
    print("The sum of the numbers is: " + str(sum_of_numbers))

if __name__ == '__main__':
    main()