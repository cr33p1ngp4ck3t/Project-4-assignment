def main():
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value *= 2
    print(curr_value)  # Print the final value that is 100 or greater

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
