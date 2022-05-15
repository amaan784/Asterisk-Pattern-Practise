def increasingOrderUsingForLoops(n):
    """
    Prints in increasing order of asterisks

    eg- If n is 3 then the output should be
    *
    **
    ***

    :param n: pattern size
    """
    print("Increasing Order using for loops-")
    for i in range(n+1):
        for j in range(i):
            print("*", end="")
        print("")
    print("")


def decreasingOrderUsingForLoops(n):
    """
    Prints in decreasing order of asterisks

    eg- If n is 3 then the output should be
    ***
    **
    *

    :param n: pattern size
    """
    print('Decreasing Order using for loops-')
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print("")
    print("")


def increasingOrderUsingStringMultiplication(n):
    """
    Prints in increasing order of asterisks
    Uses a shortcut method of string multiplication

    eg- If n is 3 then the output should be
    *
    **
    ***

    :param n: pattern size
    """
    print("Increasing Order using String Multiplication-")
    for i in range(1, n+1):
        print("*" * i)
    print("")


def decreasingOrderUsingStringMultiplication(n):
    """
    Prints in decreasing order of asterisks
    Uses a shortcut method of string multiplication

    eg- If n is 3 then the output should be
    ***
    **
    *
    :param n: pattern size
    """
    print("Decreasing Order using String Multiplication-")
    for i in range(n, 0, -1):
        print("*" * i)
    print("")


def levelsCalculatorHelper(n):
    """
    Calculates the maximum number of asterisks required for the triangle problems given the user input.
    This will always be an odd number.
    Since we need to make triangles of particular sizes thats the reason we calculate this.

    Basically if user input is 1 then the levels would be 1.
    If 2 then 3
    If 3 then 5
    If 4 then 7
    If 5 then 9

    :param n: user input
    :return: number of levels
    """
    if n == 1:
        levels = 1
    else:
        levels = (n - 1) + n
    return levels


def triangleUsingForLoops(n):
    """
    Prints a triangle depending on n
    To get a perfect looking triangle we only deal with odd numbered values
    Uses for loops

    eg- if n is 3 then the output should be

           *
        *  *  *
     *  *  *  *  *

    :param n: pattern size
    """
    print("triangle using for loops- ")

    levels = levelsCalculatorHelper(n)

    spaces = int(levels/2)

    for i in range(1, levels+1):
        if i % 2 == 1:
            for a in range(spaces):
                print("   ", end="")
            for b in range(i):
                print(" * ", end="")
            for c in range(spaces):
                if c == spaces-1:
                    print("   " * spaces)
                else:
                    print("   " * spaces, end="")
            spaces -= 1
    print("")


def triangleUsingStringMultiplication(n):
    """
    Prints a triangle depending on n
    To get a perfect looking triangle we only deal with odd numbered values
    Uses string multiplication

    eg- if n is 3 then the output should be

           *
        *  *  *
     *  *  *  *  *

    :param n: pattern size
    """
    print("triangle using string multiplication- ")

    levels = levelsCalculatorHelper(n)

    spaces = int(levels/2)

    for i in range(1, levels+1):
        if i % 2 == 1:
            print("   " * spaces, end="")
            print(" * " * i, end="")
            print("   " * spaces)
            spaces -= 1
    print("")


def reverseTriangle(n):
    """
    Prints a reverse triangle depending on n
    To get a perfect looking triangle we only deal with odd numbered values

    eg- if n is 3 then the output should be

      *  *  *  *  *
        *  *  *
           *

    :param n: pattern size
    """
    print("reverse triangle- ")

    levels = levelsCalculatorHelper(n)

    spaces = 1

    for i in range(levels, 0, -1):
        if i % 2 == 1:
            if i == levels:
                print(" * " * i)
            else:
                print("   " * spaces, end="")
                print(" * " * i, end="")
                print("   " * spaces)
                spaces += 1
    print("")


def diamond(n):
    """
       Prints a diamond shape depending on the size of n
       This will be based on the logic and code of the triangle and the reverse triangle
       Its just that we reduce the size of levels by 1 in the reverse triangle

       eg - if n is 3 then
               *
            *  *  *
         *  *  *  *  *
            *  *  *
               *

       :param n: pattern size
    """
    print("diamond shape-")

    levels = levelsCalculatorHelper(n)

    firstHalfSpaces = int(levels / 2)
    secondHalfSpaces = 1

    # normal triangle
    for i in range(1, levels + 1):
        if i % 2 == 1:
            print("   " * firstHalfSpaces, end="")
            print(" * " * i, end="")
            print("   " * firstHalfSpaces)
            firstHalfSpaces -= 1

    # reverse triangle
    for i in range(levels-1, 0, -1):
        if i % 2 == 1:
            print("   " * secondHalfSpaces, end="")
            print(" * " * i, end="")
            print("   " * secondHalfSpaces)
            secondHalfSpaces += 1
    print("")


def ModifiedFloydsTriangle(n):
    """
    Prints a modified version of Floyds triangle

    TBD: change user input format
    
    Eg -
    If user input is 5 then

    1	*	*	*	*	*	*	*	*	1
    2	3	*	*	*	*	*	*	3	2
    4	5	6	*	*	*	*	6	5	4
    7	8	9	10	*	*	10	9	8	7
    11	12	13	14	15	15	14	13	12	11

    :param n: pattern size
    """

    h = int(input("Enter the height (>0): "))

    while h <= 0:
        print("Invalid Entry")
        h = int(input("Enter the height (>0): "))

    x = 1

    for i in range(1,h+1):
        stars = 0
        for j in range(1,i+1):
            print(x, end = "   ")
            x = x + 1
        stars = h - i
        for k in range(stars):
            print("*", end = "   ")
            print("*", end = "   ")
        z = int(x)
        for a in range(i+1,1,-1):
            z = z - 1
            print(z, end = "   ")
        print()


def cross(n):
    """
       Prints a cross shape depending on the size of n

       :param n: pattern size
    """

    print("TBD cross shape")
    pass


def eight(n):
    """
       Prints an eight shape depending on the size of n

       :param n: pattern size
    """

    print("TBD eight shape")
    pass


def box(n):
    """
       Prints a box shape depending on the size of n

       :param n: pattern size
    """

    print("TBD box shape")
    pass


if __name__ == '__main__':
    userInput = int(input("Enter a number to see patterns: "))

    # taking the absolute value
    userInput = abs(userInput)

    # increasingOrderUsingForLoops(userInput)
    # decreasingOrderUsingForLoops(userInput)
    # increasingOrderUsingStringMultiplication(userInput)
    # decreasingOrderUsingStringMultiplication(userInput)
    # triangleUsingForLoops(userInput)
    # triangleUsingStringMultiplication(userInput)
    # reverseTriangle(userInput)
    # diamond(userInput)
    # ModifiedFloydsTriangle(userInput)

    cross(userInput)
    eight(userInput)
    box(userInput)
