import sys, getopt

# https://stackoverflow.com/q/354038/2999220
def is_number(s):
    try:
        float(s)
        try:
            test = int(s)
            return True
        except ValueError:
            return False
    except ValueError:
        return False
# https://stackoverflow.com/q/9246076/2999220
def printchar(char):
    sys.stdout.write(char)
    sys.stdout.flush()
# https://stackoverflow.com/a/21659588/2999220
def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch
    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch
getch = _find_getch()

tmpString = ""
def main(args):
    if len(args) == 0:
        printchar("Input Arabic or Roman number? (a/r): ")
        tmpString = getch()
        print(tmpString)
        
        tmpString = tmpString.upper()
        if tmpString == "A":
            checkAndOutputRomanNumeral(raw_input("Enter Arabic number: "))
        elif tmpString == "R":
            outputArabicNumber(raw_input("Enter Roman number: "))
        else:
            print("\"" + tmpString + "\" isn't 'a' or 'r'!")
    else:
        if args[0] == "-h":
            print("NumeralConverter - github.com/Walkman100/NumeralConverter")
            printUsage()
        elif args[0] == "-a":
            if len(args) > 1: checkAndOutputRomanNumeral(args[1])
            else: checkAndOutputRomanNumeral(raw_input("Enter Arabic number: "))
        elif args[0] == "-r":
            if len(args) > 1: outputArabicNumber(args[1])
            else: outputArabicNumber(raw_input("Enter Roman number: "))
        else:
            print("Unrecognised flag \"" + args[0] + "\"!")
            printUsage()

def printUsage():
    flags = " [-h|-r [roman number]|-a [arabic number]]"
    print("python " + sys.argv[0] + flags)

def checkAndOutputRomanNumeral(input):
    if is_number(input):
        if len(input) < 19:
            outputRomanNumeral(int(input))
        else:
            print("\"" + input + "\" is " + (len(input) - 18 + " digit(s) too long! Maximum size for \"//\" operations is 18 digits"))
    else:
        print("\"" + input + "\" is not an Arabic number!")

def outputRomanNumeral(number):
    if number > 1000:
        for i in range(1, (number // 1000) +1):
            printchar("M")
        number -= (number // 1000) * 1000
    while number > 900:
        number -= 900
        printchar("CM")
    
    while number > 500:
        number -= 500
        printchar("D")
    while number > 400:
        number -= 400
        printchar("CD")
    
    while number > 100:
        number -= 100
        printchar("C")
    while number > 90:
        number -= 90
        printchar("XC")
    
    while number > 50:
        number -= 50
        printchar("L")
    while number > 40:
        number -= 40
        printchar("XL")
    
    while number > 10:
        number -= 10
        printchar("X")
    while number > 9:
        number -= 9
        printchar("IX")
    
    while number > 5:
        number -= 5
        printchar("V")
    while number > 4:
        number -= 4
        printchar("IV")
    
    while number >= 1:
        number -= 1
        printchar("I")
    printchar("\n")

def outputArabicNumber(RomanNumber):
    RomanNumber = RomanNumber.upper()
    for i in range(0, len(RomanNumber)):
        # https://stackoverflow.com/a/1228327/2999220
        if RomanNumber[i] == "I":   RomanNumber = RomanNumber[:i] + '1' + RomanNumber[i + 1:]
        elif RomanNumber[i] == "V": RomanNumber = RomanNumber[:i] + '2' + RomanNumber[i + 1:]
        elif RomanNumber[i] == "X": RomanNumber = RomanNumber[:i] + '3' + RomanNumber[i + 1:]
        elif RomanNumber[i] == "L": RomanNumber = RomanNumber[:i] + '4' + RomanNumber[i + 1:]
        elif RomanNumber[i] == "C": RomanNumber = RomanNumber[:i] + '5' + RomanNumber[i + 1:]
        elif RomanNumber[i] == "D": RomanNumber = RomanNumber[:i] + '6' + RomanNumber[i + 1:]
        elif RomanNumber[i] == "M": RomanNumber = RomanNumber[:i] + '7' + RomanNumber[i + 1:]
        else:
            print("\"" + RomanNumber[i] + "\" is not a valid Roman Numeral character!")
            exit()
    # Now we have the roman number in arabic numbers (so we can use < and >), we just add it all
    ArabicNumber = 0
    RomanNumber = RomanNumber + "0" # Because loops, length calculation and next letter calculation
    for i in range(0, len(RomanNumber)):
        if i < len(RomanNumber) - 1 and RomanNumber[i] >= RomanNumber[i + 1]:
            if RomanNumber[i] == "1":   ArabicNumber += 1
            elif RomanNumber[i] == "2": ArabicNumber += 5
            elif RomanNumber[i] == "3": ArabicNumber += 10
            elif RomanNumber[i] == "4": ArabicNumber += 50
            elif RomanNumber[i] == "5": ArabicNumber += 100
            elif RomanNumber[i] == "6": ArabicNumber += 500
            elif RomanNumber[i] == "7": ArabicNumber += 1000
        elif i < len(RomanNumber) - 1:
            if RomanNumber[i] == "1":   ArabicNumber -= 1
            elif RomanNumber[i] == "2": ArabicNumber -= 5
            elif RomanNumber[i] == "3": ArabicNumber -= 10
            elif RomanNumber[i] == "4": ArabicNumber -= 50
            elif RomanNumber[i] == "5": ArabicNumber -= 100
            elif RomanNumber[i] == "6": ArabicNumber -= 500
            elif RomanNumber[i] == "7": ArabicNumber -= 1000
    print(ArabicNumber)

main(sys.argv[1:])
