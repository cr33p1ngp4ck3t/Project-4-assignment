INCHES_PER_FOOT = 12
def main():
    feet: float = float(input("Enter number of feet \nie: If you are 4'11 then write 4.11\n>> "))
    inches: float = feet * INCHES_PER_FOOT
    print("This is", inches, "inches")
if __name__ == '__main__':
    main()