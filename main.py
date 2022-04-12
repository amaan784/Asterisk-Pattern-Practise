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
    if n == 1:
        levels = 1
    else:
        levels = (n - 1) + n

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
    if n == 1:
        levels = 1
    else:
        levels = (n - 1) + n

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
    if n == 1:
        levels = 1
    else:
        levels = (n - 1) + n

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

       :param n: pattern size
    """
    pass


def cross(n):
    pass


def eight(n):
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

    diamond(userInput)
    cross(userInput)
    eight(userInput)

