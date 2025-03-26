def main():
    
    dividend : int = int(input("Enter the dividend: "))
    divisor : int = int(input("Enter the divisor: "))

    quotient : int = dividend // divisor
    remainder : int = dividend % divisor

    print("The quotient is: " + str(quotient) + " and the remainder is: " + str(remainder))
if __name__ == '__main__':
    main()