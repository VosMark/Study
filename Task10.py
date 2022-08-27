if __name__ == "__main__":
    while True:
        try:
            number = float (input("Enter a number \ n"))
            print(f"The absolute value of {number} is {abs(number)}")
            break
        except ValueError:
            print ("Cannot return absolute value for the specified input")